import click
import re

from packaging import version
from configparser import ConfigParser
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from pathlib import Path
from git import Repo

from qube.create.github_support import is_git_repo


def bump_template_version(new_version: str, pipeline_dir: Path) -> None:
    """
    Update the version number for all files that are whitelisted or forced in blacklisted files.
    This is specified in the config file.

    INFO on valid versions: All versions must match the format like 1.0.0 or 1.1.0-SNAPSHOT; these are the only valid
    version formats QUBE allows. A valid version therefore contains a three digits (in the range from 0 to however large it will grow)
    separated by two dots.
    Optional is the -SNAPSHOT at the end (for JVM templates especially). NOTE that versions like 1.2.3.4 or 1.2 WILL NOT be recognized as valid versions as
    well as no substring of them will be recognized.

    :param new_version: The new version number that should replace the old one in a qube project
    :param pipeline_dir: The default value is the current working directory, so we´re initially assuming the user
                         bumps the version from the projects top level directory. If this is not the case this parameter
                         shows the path where the projects top level directory is and bumps the version there
    """
    parser = ConfigParser()
    parser.read(f'{pipeline_dir}/qube.cfg')
    current_version = parser.get('bumpversion', 'current_version')
    sections = ['bumpversion_files_whitelisted', 'bumpversion_files_blacklisted']

    # if pipeline_dir was given as handle use cwd since we need it for git add
    qube_cfg_path = f'{str(pipeline_dir)}/qube.cfg' if str(pipeline_dir).startswith(str(Path.cwd())) else \
                    f'{str(Path.cwd())}/{pipeline_dir}/qube.cfg'

    # keep path of all files that were changed during bump version
    changed_files = [qube_cfg_path]

    click.echo(click.style(f'Changing version number.\nCurrent version is {current_version}.'
                           f'\nNew version will be {new_version}\n', fg='blue'))

    # for each section (whitelisted and blacklisted files) bump the version (if allowed)
    for section in sections:
        for file, path in parser.items(section):
            not_changed, file_path = replace(f'{pipeline_dir}/{path}', new_version, section)
            # only add file if the version(s) in the file were bumped
            if not not_changed:
                path_changed = file_path if file_path.startswith(str(Path.cwd())) else f'{str(Path.cwd())}/{file_path}'
                changed_files.append(path_changed)

    # update new version in qube.cfg file
    parser.set('bumpversion', 'current_version', new_version)
    with open(f'{pipeline_dir}/qube.cfg', 'w') as configfile:
        parser.write(configfile)

    # check if a project is a git repository and if so, commit bumped version changes
    if is_git_repo(pipeline_dir):
        repo = Repo(pipeline_dir)

        # git add
        click.echo(click.style('Staging template.', fg='blue'))
        repo.git.add(changed_files)

        # git commit
        click.echo(click.style('Committing changes to local git repository.', fg='blue'))
        repo.index.commit(f'Bump version from {current_version} to {new_version}')


def replace(file_path: str, subst: str, section: str) -> (bool, str):
    """
    Replace a version with the new version unless the line is explicitly excluded (marked with <<QUBE_NO_BUMP>>).
    Or, in case of blacklisted files, it ignores all lines with version numbers unless they´re explicitly marked
    for bump with tag <<QUBE_FORCE_BUMP>>.

    :param file_path: The path of the file where the version should be updated
    :param subst: The new version that replaces the old one
    :param section: The current section (whitelisted or blacklisted files)
    :return: Whether a file has been changed during bumped and the path of changed file
    """
    # flag that indicates whether no changes were made inside a file
    file_is_unchanged = True
    path_changed = ''

    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                # update version if tags were found (and were in the right section)
                if ('<<QUBE_NO_BUMP>>' not in line and not section == 'bumpversion_files_blacklisted') or '<<QUBE_FORCE_BUMP>>' in line:
                    tmp = re.sub(r'(?<!\.)\d+(?:\.\d+){2}(?:-SNAPSHOT)?(?!\.)', subst, line)
                    new_file.write(tmp)
                    if tmp != line:
                        if file_is_unchanged:
                            click.echo(click.style(f'Updating version number in {file_path}', fg='blue'))
                            file_is_unchanged = False
                            path_changed = file_path
                        click.echo(click.style(
                            f'- {line.strip().replace("<!-- <<QUBE_FORCE_BUMP>> -->","")}\n', fg='red') + click.style(
                            f'+ {tmp.strip().replace("<!-- <<QUBE_FORCE_BUMP>> -->","")}', fg='green'))
                        click.echo()
                else:
                    new_file.write(line)

    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)

    return file_is_unchanged, path_changed


def can_run_bump_version(new_version: str, project_dir: str, downgrade: bool) -> bool:
    """
    Ensure that all requirements are met, so that the bump version command can be run successfully.
    This included the following requirements:
    1.) The new version matches the format (?<!\.)\d+(?:\.\d+){2}(?:-SNAPSHOT)?(?!\.) # noqa: W605
    2.) The new version is greater than the current one
    3.) The project is a QUBE project

    :param new_version: The new version
    :param project_dir: The directory of the project
    :param downgrade: Flag that indicates whether the user wants to downgrade the project version or not
    :return: True if bump version can be run, false otherwise.
    """
    # parse the current version from the cfg file
    parser = ConfigParser()
    parser.read(f'{project_dir}/qube.cfg')
    current_version = parser.get('bumpversion', 'current_version')

    # ensure that the entered version number matches correct format
    if not re.match(r'(?<!\.)\d+(?:\.\d+){2}(?:-SNAPSHOT)?(?!\.)', new_version):
        click.echo(click.style('Invalid version specified!\nEnsure your version number has the form '
                               'like 0.0.0 or 15.100.239-SNAPSHOT', fg='red'))
        return False

    # ensure the version is bumped within a project created by QUBE
    elif not Path(f'{project_dir}/qube.cfg').is_file():
        click.echo(click.style('Did not found a qube.cfg file. Make sure you are in the right directory '
                               'or specify the path to your projects bump_version.cfg file', fg='red'))
        return False

    # ensure the new version is greater than the current one
    # equal versions wont be accepted for bump-version
    elif new_version == current_version:
        click.echo(click.style(f'The new version {new_version} cannot be equal to the current version {current_version}.', fg='red'))
        return False

    # ensure the new version is greater than the current one, if not the user wants to explicitly downgrade it
    elif not downgrade:
        current_version_r = current_version.replace('-SNAPSHOT', '')
        new_version_r = new_version.replace('-SNAPSHOT', '')
        is_greater = False

        # when the current version and the new version are equal, but one is a -SNAPSHOT version return true
        if version.parse(current_version_r) == version.parse(new_version_r) and ('-SNAPSHOT' in current_version or '-SNAPSHOT' in new_version):
            is_greater = True
        # else check if the new version is greater than the current version
        elif version.parse(current_version_r) < version.parse(new_version_r):
            is_greater = True

        # the new version is not greater than the current one
        if not is_greater:
            click.echo(click.style(
                f'New version {".".join(str(n) for n in new_version)} is not greater than the current version {".".join(str(n) for n in current_version)}.\n'
                f'\nNew version must be greater than the old one.', fg='red'))

        return is_greater
    return True

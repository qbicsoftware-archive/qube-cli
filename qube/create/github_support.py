import click
import os

from cryptography.fernet import Fernet
from distutils.dir_util import copy_tree
from subprocess import Popen, PIPE
from github import Github, GithubException
from git import Repo, exc
from pathlib import Path


def create_push_github_repository(project_name: str, project_description: str, template_creation_path: str, github_username: str) -> None:
    """
    Creates a Github repository for the created template and pushes the template to it.
    Prompts the user for the required specifications.

    :param project_name: Name of the created project
    :param project_description: Description of the created project
    :param template_creation_path: Path to the already created template
    :param github_username: The users Github username
    """
    if not is_git_accessible():
        return

    # load username from template creator
    github_username = github_username
    # the personal access token for GitHub
    access_token = handle_pat_authentification()

    is_github_org: bool = click.prompt('Do you want to create an organization repository? [y, n]',
                                       type=bool,
                                       default='No')
    if is_github_org:
        github_org: str = click.prompt('Please enter the name of the Github organization: ',
                                       type=str)
    private: bool = click.prompt('Do you want your repository to be private?  [y, n]',
                                 type=bool,
                                 default='No')

    # Login to Github
    click.echo(click.style('Logging into Github.', fg='blue'))
    authenticated_github_user = Github(access_token)
    user = authenticated_github_user.get_user()

    # Create new repository
    click.echo(click.style('Creating Github repository.', fg='blue'))
    if is_github_org:
        org = authenticated_github_user.get_organization(github_org)
        repo = org.create_repo(project_name, description=project_description, private=private)
        github_username = github_org
    else:
        repo = user.create_repo(project_name, description=project_description, private=private)

    click.echo(click.style('Creating labels and default Github settings.', fg='blue'))
    create_github_label(repo=repo, label="dependabot")

    repository = f'{os.getcwd()}/{project_name}'

    # NOTE: github_username is the organizations name, if an organization repository is to be created

    # git clone
    click.echo(click.style('Cloning empty Github repoitory.', fg='blue'))
    cloned_repo = Repo.clone_from(f'https://{github_username}:{access_token}@github.com/{github_username}/{project_name}', repository)

    # Copy files which should be included in the initial commit -> basically the template
    copy_tree(template_creation_path, repository)

    # git add
    click.echo(click.style('Staging template.', fg='blue'))
    cloned_repo.git.add(A=True)

    # git commit
    cloned_repo.index.commit(f'Created {project_name} using COOKIETEMPLE.')

    click.echo(click.style('Pushing template to Github origin master.', fg='blue'))
    cloned_repo.remotes.origin.push(refspec='master:master')

    # git create development branch
    click.echo(click.style('Creating development branch.', fg='blue'))
    cloned_repo.git.checkout('-b', 'development')

    # git push to origin development
    click.echo(click.style('Pushing template to Github origin development.', fg='blue'))
    cloned_repo.remotes.origin.push(refspec='development:development')

    # did any errors occur?
    click.echo(click.style(f'Successfully created a Github repository at https://github.com/{github_username}/{project_name}', fg='green'))


def handle_pat_authentification() -> str:
    """
    Try to read the encrypted Personal Access Token for GitHub.
    If this fails (maybe there was no generated key before) then encrypt and return the PAT afterwards.
    :return: The decrypted PAT
    """

    # check if the key and encrypted PAT already exist
    if os.path.exists(f'{Path.home()}/.qb_keys') and os.path.exists(f'{Path.home()}/qube_conf.cfg'):
        pat = decrypt_pat()

        return pat

    else:
        click.echo(click.style('Could not find personal access token!\n', fg='red'))
        click.echo(click.style('Please navigate to Github -> Your profile -> Developer Settings -> Personal access token -> Generate a new Token', fg='blue'))
        click.echo(click.style('Please only tick \'repo\'. Note that the token is a hidden input to QUBE.', fg='blue'))
        click.echo(click.style('For more information please read'
                               ' https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line', fg='blue'))
        click.echo(click.style('QUBE saves your personal access token encrypted on your disk', fg='blue'))
        access_token = click.prompt('Please enter your GitHub access token: ',
                                    type=str,
                                    hide_input=True)
        access_token_b = access_token.encode('utf-8')

        # encrypt the given PAT and save the encryption key and encrypted PAT in separate files
        click.echo(click.style('Encrypting personal access token', fg='blue'))
        key = Fernet.generate_key()
        fer = Fernet(key)
        encrypted_pat = fer.encrypt(access_token_b)

        with open(f'{Path.home()}/qube_conf.cfg', 'ab') as f:
            f.write(encrypted_pat)

        with open(f'{Path.home()}/.qb_keys', 'wb') as f:
            f.write(key)

        pat = decrypt_pat()

        return pat


def decrypt_pat() -> str:
    """
    Decrypt the encrypted PAT.
    :return: The decrypted Personal Access Token for GitHub
    """

    # read key and encrypted PAT from files
    with open(f'{Path.home()}/.qb_keys', 'rb') as f:
        key = f.readline()

    with open(f'{Path.home()}/qube_conf.cfg', 'rb') as f:
        f.readline()  # skip Github username
        encrypted_pat = f.readline()

    # decrypt the PAT and decode it to string
    click.echo(click.style('Decrypting personal access token', fg='blue'))
    fer = Fernet(key)
    decrypted_pat = fer.decrypt(encrypted_pat).decode('utf-8')

    return decrypted_pat


def load_github_username() -> str:
    """
    Load the Github username from the local cfg file stored locally in the users home.
    If not found, prompt for it and save it in the cfg file. The username is the first entry in the cfg file.

    :return: The users Github username
    """

    if not os.path.exists(f'{Path.home()}/qube_conf.cfg'):
        click.echo(click.style('Could not load Github username. Creating a new config file!', fg='red'))
        github_username = click.prompt('Please enter your Github account username: ',
                                       type=str)
        github_username_b = github_username.encode('utf-8')

        # write the username to the cfg file
        with open(f'{Path.home()}/qube_conf.cfg', 'wb') as f:
            f.write(github_username_b)
            f.write(b'\n')
        return github_username

    # load Github username from the cfg if it exists
    with open(f'{Path.home()}/qube_conf.cfg', 'rb') as f:
        github_username = f.readline().decode('utf-8')

        return github_username.replace('\n', '')


def is_git_accessible() -> bool:
    """
    Verifies that git is accessible and in the PATH.

    :return: True if accessible, false if not
    """
    git_installed = Popen(['git', '--version'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    (git_installed_stdout, git_installed_stderr) = git_installed.communicate()
    if git_installed.returncode != 0:
        click.echo(click.style('Could not find \'git\' in the PATH. Is it installed?', fg='red'))
        click.echo(click.style('Run command was: git', fg='red'))
        return False

    return True


def create_github_label(repo, label: str) -> None:
    """
    Create a Github label and add it to the repository.
    :param repo: The repository where the label needs to be added
    :param label: The name of the new label
    """
    try:
        repo.create_label(name=label, color="1BB0CE")
    except GithubException:
        click.echo(click.style(f'Unable to create label {label} due to permissions', fg='red'))


def is_git_repo(path: Path) -> bool:
    """
    Check if directory is a git repo
    :param path: The directory to check
    :return: true if path is git repo false otherwise
    """
    try:
        _ = Repo(path).git_dir
        return True
    except exc.InvalidGitRepositoryError:
        return False

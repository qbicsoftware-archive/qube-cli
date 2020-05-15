import sys
from pathlib import Path

import click
from ruamel.yaml import YAML

from qube.lint.TemplateLinter import TemplateLinter
from qube.lint.domains.cli import CliJavaLint
from qube.lint.domains.gui import GuiJavaLint
from qube.lint.domains.lib import LibJavaLint
from qube.lint.domains.portlet import PortletGroovyLint
from qube.lint.domains.service import ServiceJavaLint


def lint_project(project_dir: str) -> TemplateLinter:
    """
    Verifies the integrity of a project to best coding standards and practices.
    """
    # Detect which template the project is based on
    template_handle = get_template_handle(project_dir)

    switcher = {
        'cli-java': CliJavaLint,
        'lib-java': LibJavaLint,
        'gui-java': GuiJavaLint,
        'service-java': ServiceJavaLint,
        'portlet-groovy': PortletGroovyLint
    }

    lint_obj = switcher.get(template_handle, lambda: 'Invalid')(project_dir)
    # Run the linting tests
    try:
        # Disable check files? Some templates use their very own set of files, which do not adhere to QBiC's common files standards.
        disable_check_files_templates = []
        if template_handle in disable_check_files_templates:
            disable_check_files = True
        else:
            disable_check_files = False

        # Run non project specific linting
        click.echo(click.style('Running general linting', fg='blue'))
        lint_obj.lint_project(super(lint_obj.__class__, lint_obj), label='General Linting', custom_check_files=disable_check_files)

        # Run the project specific linting
        click.echo(click.style(f'Running {template_handle} linting', fg='blue'))
        lint_obj.lint(f'{template_handle} Linting')
    except AssertionError as e:
        click.echo(click.style(f'Critical error: {e}', fg='red'))
        click.echo(click.style('Stopping tests...', fg='red'))
        return lint_obj

    # Print the results
    lint_obj.print_results()

    # Exit code
    if len(lint_obj.failed) > 0:
        click.echo(click.style('Sorry, some tests failed - exiting with a non-zero error code...\n'))


def get_template_handle(dot_qube_path: str = '.qube.yml') -> str:
    """
    Reads the .qube file and extracts the template handle
    :param dot_qube_path: path to the .qube.yml file
    :return: found template handle
    """
    path = Path(f'{dot_qube_path}/.qube.yml')
    if not path.exists():
        click.echo(click.style('.qube.yml not found. Is this a QUBE project?', fg='red'))
        sys.exit(1)
    yaml = YAML(typ='safe')
    dot_qube_content = yaml.load(path)

    return dot_qube_content['template_handle']

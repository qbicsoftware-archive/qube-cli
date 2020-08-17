import sys
from pathlib import Path
from ruamel.yaml import YAML
from rich import print

from qube.lint.TemplateLinter import TemplateLinter
from qube.lint.domains.cli import CliJavaLint
from qube.lint.domains.gui import GuiJavaLint
from qube.lint.domains.lib import LibJavaLint
from qube.lint.domains.portlet import PortletGroovyLint
from qube.lint.domains.service import ServiceJavaLint


def lint_project(project_dir: str, is_create: bool = False) -> TemplateLinter:
    """
    Verifies the integrity of a project to best coding and practices.
    Runs a set of general linting functions, which all templates share and afterwards runs template specific linting functions.
    All results are collected and presented to the user.
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

    try:
        lint_obj = switcher.get(template_handle)(project_dir)
    except TypeError:
        print(f'[bold red]Unable to find linter for handle {template_handle}! Aborting...')
        sys.exit(1)

    # Run the linting tests
    try:
        # Run non project specific linting
        print('[bold blue]Running general linting')
        lint_obj.lint_project(super(lint_obj.__class__, lint_obj), is_subclass_calling=False)

        # Run the project specific linting
        print(f'[bold blue]Running {template_handle} linting')

        # for every python project that is created autopep8 will run one time
        # when linting en existing python qube project, autopep8 should be now optional,
        # because (for example) it messes up Jinja syntax (if included in project)
        lint_obj.lint()
    except AssertionError as e:
        print(f'[bold red]Critical error: {e}')
        print('[bold red] Stopping tests...')
        return lint_obj

    # Print the results
    lint_obj.print_results()

    # Exit code
    if len(lint_obj.failed) > 0:
        print(f'[bold red] {len(lint_obj.failed)} tests failed! Exiting with non-zero error code.')
        sys.exit(1)


def get_template_handle(dot_qube_path: str = '.qube.yml') -> str:
    """
    Reads the .qube file and extracts the template handle
    :param dot_qube_path: path to the .qube file
    :return: found template handle
    """
    path = Path(f'{dot_qube_path}/.qube.yml')
    if not path.exists():
        print('[bold red].qube.yml not found. Is this a qube project?')
        sys.exit(1)
    yaml = YAML(typ='safe')
    dot_qube_content = yaml.load(path)

    return dot_qube_content['template_handle']

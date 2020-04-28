"""Console script for qube."""
import logging
import os
import re
import sys
from pathlib import Path

import click

import qube
from qube.bump_version.bump_version import bump_template_version, can_do_bump_version
from qube.create.create import choose_domain
from qube.info.info import show_info
from qube.lint.lint import lint_project
from qube.list.list import list_available_templates
from qube.sync.sync import snyc_template
from qube.util.click_util import CustomHelpOrder

WD = os.path.dirname(__file__)


def main():
    click.echo(click.style(fr"""
 _______           ______   _______
(  ___  )|\     /|(  ___ \ (  ____ \
| (   ) || )   ( || (   ) )| (    \/
| |   | || |   | || (__/ / | (__
| |   | || |   | ||  __ (  |  __)
| | /\| || |   | || (  \ \ | (
| (_\ \ || (___) || )___) )| (____/\
(____\/_)(_______)|/ \___/ (_______/
        """, fg='blue'))

    click.echo(click.style('Run ', fg='blue') + click.style('qube --help ', fg='green') + click.style('for an overview of all commands', fg='blue'))
    click.echo()

    qube_cli()


@click.group(cls=CustomHelpOrder)
@click.version_option(qube.__version__,
                      message=click.style(f'QUBE Version: {qube.__version__}', fg='blue'))
@click.option(
    '-v', '--verbose',
    is_flag=True,
    default=False,
    help='Verbose output (print debug statements)'
)
def qube_cli(verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG, format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@qube_cli.command(help_priority=1, short_help='Create a new project using one of QBiC\'s templates')
@click.option('--domain', type=click.Choice(['cli', 'lib', 'gui', 'portlet', 'service']))
def create(domain: str) -> None:
    """
    Create a new project using one of our templates
    """
    choose_domain(domain)


@qube_cli.command(help_priority=2, short_help='Lint your existing QUBE project to verify that it adheres to all standards')
@click.argument('project_dir', type=click.Path(),
                default=Path(f'{Path.cwd()}'))
def lint(project_dir) -> None:
    """
    Lint your existing QUBE project
    """
    lint_project(project_dir)


@qube_cli.command(help_priority=3, short_help='List all currently existing QUBE templates')
def list() -> None:
    """
    List all available QUBE templates
    """
    list_available_templates()


@qube_cli.command(help_priority=4, short_help='Show detailed information on a specific template or set of templates')
@click.argument('handle', type=str)
def info(handle: str) -> None:
    """
    Get detailed info on a QUBE template
    """
    show_info(handle)


@qube_cli.command('bump-version', help_priority=5, short_help='Bump the version of your QUBE project')
@click.argument('new_version', type=str)
@click.argument('project_dir', type=click.Path(),
                default=Path(f'{Path.cwd()}'))
def bump_version(new_version, project_dir) -> None:
    """
    Bump the version of an existing QUBE project
    """
    # if the path entered ends with a trailing slash remove it for consistent output
    if str(project_dir).endswith('/'):
        project_dir = Path(str(project_dir).replace(str(project_dir)[len(str(project_dir)) - 1:], ''))

    # check if the command met all requirements for successful bump
    if can_do_bump_version(new_version, project_dir):
        bump_template_version(new_version, project_dir)
    else:
        sys.exit(0)


@qube_cli.command(help_priority=6, short_help='Sync your existing QUBE project with the most recent template')
def sync() -> None:
    """
    Sync your project with the latest template release
    """
    snyc_template()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

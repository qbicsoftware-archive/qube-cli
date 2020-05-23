import os
import sys
import click

from rich.style import Style
from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD

from qube.info.levensthein_dist import most_similar_command
from qube.list.list import load_available_templates
from qube.util.dict_util import is_nested_dictionary
from qube.custom_qube_cli.suggest_similar_commands import load_available_handles

WD = os.path.dirname(__file__)
TEMPLATES_PATH = f'{WD}/../create/templates'


def show_info(handle: str) -> None:
    """
    Displays detailed information of a domain/language/template

    :param handle: domain/language/template handle (examples: cli or cli-python)
    """
    # list of all templates that should be printed according to the passed handle
    templates_to_print = []
    available_templates = load_available_templates(f'{TEMPLATES_PATH}/available_templates.yml')

    specifiers = handle.split('-')
    domain = specifiers[0]
    global template_info

    # only domain specified
    if len(specifiers) == 1:
        try:
            template_info = available_templates[domain]
        except KeyError:
            handle_non_existing_command(handle)
    # domain, subdomain, language
    elif len(specifiers) > 2:
        try:
            sub_domain = specifiers[1]
            language = specifiers[2]
            template_info = available_templates[domain][sub_domain][language]
        except KeyError:
            handle_non_existing_command(handle)
    # domain, language OR domain, subdomain
    else:
        try:
            second_specifier = specifiers[1]
            template_info = available_templates[domain][second_specifier]
        except KeyError:
            handle_non_existing_command(handle)

    # Add all templates under template_info to list
    flatten_nested_dict(template_info, templates_to_print)

    for template in templates_to_print:
        template[2] = set_linebreaks(template[2])

    table = Table(title=f'[bold]Info on QUBE\'s {handle} template(s)', title_style="blue", header_style=Style(color="blue", bold=True), box=HEAVY_HEAD)
    table.add_column("Name", justify="left", style="green", no_wrap=True)
    table.add_column("Handle", justify="left")
    table.add_column("Short Description", justify="left")
    table.add_column("Available Libraries", justify="left")
    table.add_column("Version", justify="left")

    for template in templates_to_print:
        table.add_row(f'[bold]{template[0]}', template[1], template[2], template[3], template[4])

    console = Console()
    console.print(table)


def flatten_nested_dict(template_info_, templates_to_print) -> None:
    """
    Flatten an arbitrarily deep nested dict and creates a list of list containing all available
    templates for the specified doamin/subdomain and/or language
    :param template_info_: The dict containing the yaml parsed info for all available templates the user wants to
                           gather some information
    """
    if is_nested_dictionary(template_info_):
        for templ in template_info_.values():
            if not is_nested_dictionary(templ):
                templates_to_print.append([templ['name'], templ['handle'], templ['long description'],
                                           templ['available libraries'], templ['version']])
            else:
                flatten_nested_dict(templ, templates_to_print)
    else:
        # a single template to append was reached
        templates_to_print.append([template_info_['name'], template_info_['handle'], template_info_['long description'],
                                   template_info_['available libraries'], template_info_['version']])


def set_linebreaks(desc: str) -> str:
    """
    Sets newlines after max 45 characters (or the latest space to avoid non-sense separation)
    :param desc: The parsed long description for the sepcific template
    :return: The formatted string with inserted newlines
    """

    linebreak_limit = 50
    last_space = -1
    cnt = 0
    idx = 0

    while idx < len(desc):
        if cnt == linebreak_limit:
            # set a line break at the last space encountered to avoid separating words
            desc = desc[:last_space] + '\n' + desc[last_space + 1:]
            cnt = 0
        elif desc[idx] == ' ':
            last_space = idx
        cnt += 1
        idx += 1

    return desc


def non_existing_handle() -> None:
    """
    Handling key not found access error for non existing template handles.
    Displays an error message and terminates QUBE.

    """

    click.echo(click.style('Handle does not exist. Please enter a valid handle.\n Use ', fg='red')
               + click.style('qube list', fg='green')
               + click.style(' to display all template handles.', fg='red'))
    sys.exit(1)


def handle_non_existing_command(handle: str):
    """
    Handle the case, when an unknown handle was entered and try to find a similar handle.
    :param handle: The non existing handle
    """
    available_handles = load_available_handles()
    most_sim = most_similar_command(handle, available_handles)
    if most_sim:
        # found exactly one similar command
        if len(most_sim) == 1:
            click.echo(click.style(f'Unknown handle \'{handle}\'. See ', fg='red') + click.style('qube list ', fg='green') +
                       click.style('for all valid handles.\n', fg='red'))
            click.echo(click.style('Will use best match ', fg='red') + click.style(f'{most_sim[0]}.\n', fg='green'))
            # use best match if exactly one similar handle was found
            show_info(most_sim[0])
        else:
            # found multiple similar commands
            nl = '\n'
            click.echo(click.style(f'Unknown handle \'{handle}\'. See ', fg='red') + click.style('qube list ', fg='green') +
                       click.style(f'for all valid handles.\nMost similar commands are:{nl}{nl.join(most_sim)}', fg='red'))
        sys.exit(1)

    else:
        # found no similar commands
        non_existing_handle()

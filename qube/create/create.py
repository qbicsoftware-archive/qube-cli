import click

from qube.create.domains.GuiCreator import GuiCreator
from qube.create.domains.PortletCreator import PortletCreator
from qube.create.domains.ServiceCreator import ServiceCreator
from qube.create.domains.LibCreator import LibCreator
from qube.create.domains.CliCreator import CliCreator


def choose_domain(domain: str):
    """
    Prompts the user for the template domain.
    Prompts the user whether or not to create a Github repository

    :param domain: Template domain
    """

    if not domain:
        domain = click.prompt('Choose between the following domains ',
                              type=click.Choice(['cli', 'lib', 'gui', 'service', 'portlet']),
                              show_choices=True)

    switcher = {
        'cli': CliCreator,
        'lib': LibCreator,
        'gui': GuiCreator,
        'service': ServiceCreator,
        'portlet': PortletCreator
    }

    creator_obj = switcher.get(domain.lower(), lambda: 'Invalid domain!')()
    creator_obj.create_template()

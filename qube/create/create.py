from qube.create.domains.CliCreator import CliCreator
from qube.create.domains.GuiCreator import GuiCreator
from qube.create.domains.LibCreator import LibCreator
from qube.create.domains.PortletCreator import PortletCreator
from qube.create.domains.ServiceCreator import ServiceCreator

from qube.custom_cli.questionary import qube_questionary_or_dot_qube


def choose_domain(domain: str or None, dot_qube: dict = None):
    """
    Prompts the user for the template domain.
    Creates the .qube file.
    Prompts the user whether or not to create a Github repository

    :param domain: Template domain
    :param dot_qube: Dictionary created from the .qube.yml file. None if no .qube.yml file was used.
    """
    if not domain:
        domain = qube_questionary_or_dot_qube(function='select',
                                              question='Choose the project\'s domain',
                                              choices=['cli', 'lib', 'gui', 'service', 'portlet'],
                                              default='cli',
                                              dot_qube=dot_qube,
                                              to_get_property='domain')

    switcher = {
        'cli': CliCreator,
        'lib': LibCreator,
        'gui': GuiCreator,
        'service': ServiceCreator,
        'portlet': PortletCreator
    }

    creator_obj = switcher.get(domain.lower())()
    creator_obj.create_template(dot_qube)

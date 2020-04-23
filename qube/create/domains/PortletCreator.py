import os
import click
from pathlib import Path
from dataclasses import dataclass

from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct


@dataclass
class TemplateStructPortlet(QubeTemplateStruct):
    """
    Intended Use: This class holds all attributes specific for SERVICE projects
    """

    """______GROOVY______"""
    main_class_prefix: str = ''
    version: str = '1.0.0-SNAPSHOT'
    use_openbis_client = 'no'
    use_openbis_raw_api = 'no'
    use_qbic_databases = 'no'
    use_vaadin_charts = 'no'


class PortletCreator(TemplateCreator):

    def __init__(self):
        self.portlet_struct = TemplateStructPortlet(domain='portlet')
        super().__init__(self.portlet_struct)
        self.WD = os.path.dirname(__file__)
        self.WD_Path = Path(self.WD)
        self.TEMPLATES_PORTLET_PATH = f'{self.WD_Path.parent}/templates/portlet'

        '"" TEMPLATE VERSIONS ""'
        self.PORTLET_GROOVY_TEMPLATE_VERSION = super().load_version('portlet-groovy')

    def create_template(self):
        """
        Handles the CLI domain. Prompts the user for the language, general and domain specific options.
        """

        self.portlet_struct.language = click.prompt('Choose between the following languages',
                                                    type=click.Choice(['groovy']),
                                                    show_choices=True)

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration()

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'groovy': self.portlet_groovy_options,
        }
        switcher.get(self.portlet_struct.language.lower(), lambda: 'Invalid language!')()

        # create the chosen and configured template
        super().create_template_without_subdomain(f'{self.TEMPLATES_PORTLET_PATH}')

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.PORTLET_GROOVY_TEMPLATE_VERSION,
        }
        self.portlet_struct.template_version, self.portlet_struct.template_handle = switcher_version.get(
            self.portlet_struct.language.lower(), lambda: 'Invalid language!'), f'portlet-{self.portlet_struct.language.lower()}'

        super().process_common_operations()

    def portlet_groovy_options(self):
        self.portlet_struct.main_class_prefix = click.prompt('Main class prefix:',
                                                             type=str,
                                                             default='Sample')
        self.portlet_struct.use_openbis_client = click.prompt('Please choose whether to use the openbis client or not',
                                                              type=click.Choice(['yes', 'no']),
                                                              default='no')
        self.portlet_struct.use_openbis_raw_api = click.prompt('Please choose whether to use the openbis raw api or not',
                                                               type=click.Choice(['yes', 'no']),
                                                               default='no')
        self.portlet_struct.use_qbic_databases = click.prompt('Please choose whether to use qbics databases',
                                                              type=click.Choice(['yes', 'no']),
                                                              default='no')
        self.portlet_struct.use_vaadin_charts = click.prompt('Please choose whether to use vaadin charts',
                                                             type=click.Choice(['yes', 'no']),
                                                             default='no')

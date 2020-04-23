import os
import click
from pathlib import Path
from dataclasses import dataclass

from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct


@dataclass
class TemplateStructService(QubeTemplateStruct):
    """
    Intended Use: This class holds all attributes specific for Service projects
    """

    """______JAVA______"""
    main_class_prefix: str = ''
    version: str = '1.0.0-SNAPSHOT'


class ServiceCreator(TemplateCreator):

    def __init__(self):
        self.service_struct = TemplateStructService(domain='service')
        super().__init__(self.service_struct)
        self.WD = os.path.dirname(__file__)
        self.WD_Path = Path(self.WD)
        self.TEMPLATES_SERVICE_PATH = f'{self.WD_Path.parent}/templates/service'

        '"" TEMPLATE VERSIONS ""'
        self.SERVICE_JAVA_TEMPLATE_VERSION = super().load_version('service-java')

    def create_template(self):
        """
        Handles the SERVICE domain. Prompts the user for the language, general and domain specific options.
        """

        self.service_struct.language = click.prompt('Choose between the following languages',
                                                    type=click.Choice(['java']),
                                                    show_choices=True)

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration()

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'java': self.service_java_options,
        }
        switcher.get(self.service_struct.language.lower(), lambda: 'Invalid language!')()

        # create the chosen and configured template
        super().create_template_without_subdomain(f'{self.TEMPLATES_SERVICE_PATH}')

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.SERVICE_JAVA_TEMPLATE_VERSION,
        }
        self.service_struct.template_version, self.service_struct.template_handle = switcher_version.get(
            self.service_struct.language.lower(), lambda: 'Invalid language!'), f'service-{self.service_struct.language.lower()}'

        super().process_common_operations()

    def service_java_options(self):
        self.service_struct.main_class_prefix = click.prompt('Main class prefix:',
                                                             type=str,
                                                             default='Sample')

import os
import click
from pathlib import Path
from dataclasses import dataclass

from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct


@dataclass
class TemplateStructLib(QubeTemplateStruct):
    """
    Intended Use: This class holds all attributes specific for LIB projects
    """

    """______JAVA______"""
    version: str = '1.0.0-SNAPSHOT'


class LibCreator(TemplateCreator):

    def __init__(self):
        self.lib_struct = TemplateStructLib(domain='lib')
        super().__init__(self.lib_struct)
        self.WD = os.path.dirname(__file__)
        self.WD_Path = Path(self.WD)
        self.TEMPLATES_LIB_PATH = f'{self.WD_Path.parent}/templates/lib'

        '"" TEMPLATE VERSIONS ""'
        self.LIB_JAVA_TEMPLATE_VERSION = super().load_version('lib-java')

    def create_template(self):
        """
        Handles the CLI domain. Prompts the user for the language, general and domain specific options.
        """

        self.lib_struct.language = click.prompt('Choose between the following languages',
                                                type=click.Choice(['java']),
                                                show_choices=True)

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration()

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'java': self.lib_java_options,
        }
        switcher.get(self.lib_struct.language.lower(), lambda: 'Invalid language!')()

        # create the chosen and configured template
        super().create_template_without_subdomain(f'{self.TEMPLATES_LIB_PATH}')

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.LIB_JAVA_TEMPLATE_VERSION,
        }
        self.lib_struct.template_version, self.lib_struct.template_handle = switcher_version.get(
            self.lib_struct.language.lower(), lambda: 'Invalid language!'), f'lib-{self.lib_struct.language.lower()}'

        super().process_common_operations()

    def lib_java_options(self) -> None:
        """
        There are currently no lib-java specific cookiecutter properties
        """
        pass

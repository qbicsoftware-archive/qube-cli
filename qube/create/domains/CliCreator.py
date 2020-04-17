import os
import click
from pathlib import Path
from dataclasses import dataclass

from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct


@dataclass
class TemplateStructCli(QubeTemplateStruct):
    """
    Intended Use: This class holds all attributes specific for CLI projects
    """

    """______JAVA______"""
    main_class_prefix: str = ''
    version: str = '1.0.0-SNAPSHOT'


class CliCreator(TemplateCreator):

    def __init__(self):
        self.cli_struct = TemplateStructCli(domain='cli')
        super().__init__(self.cli_struct)
        self.WD = os.path.dirname(__file__)
        self.WD_Path = Path(self.WD)
        self.TEMPLATES_CLI_PATH = f'{self.WD_Path.parent}/templates/cli'

        '"" TEMPLATE VERSIONS ""'
        self.CLI_JAVA_TEMPLATE_VERSION = super().load_version('cli-java')

    def create_template(self):
        """
        Handles the CLI domain. Prompts the user for the language, general and domain specific options.
        """

        self.cli_struct.language = click.prompt('Choose between the following languages',
                                                type=click.Choice(['java']),
                                                show_choices=True)

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration()

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'java': self.cli_java_options,
        }
        switcher.get(self.cli_struct.language.lower(), lambda: 'Invalid language!')()

        # create the chosen and configured template
        super().create_template_without_subdomain(f'{self.TEMPLATES_CLI_PATH}')

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.CLI_JAVA_TEMPLATE_VERSION,
        }
        self.cli_struct.template_version, self.cli_struct.template_handle = switcher_version.get(
            self.cli_struct.language.lower(), lambda: 'Invalid language!'), f'cli-{self.cli_struct.language.lower()}'

        super().process_common_operations()

    def cli_java_options(self):
        self.cli_struct.main_class_prefix = click.prompt('Main class prefix:',
                                                         type=str,
                                                         default='Sample')

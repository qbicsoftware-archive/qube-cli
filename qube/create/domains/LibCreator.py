import os
from pathlib import Path
from dataclasses import dataclass

from qube.create.github_support import prompt_github_repo
from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct
from qube.custom_cli.questionary import qube_questionary_or_dot_qube
from qube.common.version import load_qube_template_version


@dataclass
class TemplateStructLib(QubeTemplateStruct):
    """
    Lib-JAVA
    """
    main_class_prefix: str = ''


class LibCreator(TemplateCreator):

    def __init__(self):
        self.lib_struct = TemplateStructLib(domain='lib')
        super().__init__(self.lib_struct)
        self.WD_Path = Path(os.path.dirname(__file__))
        self.TEMPLATES_LIB_PATH = f'{self.WD_Path.parent}/templates/lib'

        '"" TEMPLATE VERSIONS ""'
        self.LIB_JAVA_TEMPLATE_VERSION = load_qube_template_version('lib-java', self.AVAILABLE_TEMPLATES_PATH)

    def create_template(self, dot_qube: dict or None):
        """
        Handles the CLI domain. Prompts the user for the language, general and domain specific options.
        """
        self.lib_struct.language = qube_questionary_or_dot_qube(function='select',
                                                                question='Choose the project\'s primary language',
                                                                choices=['java'],
                                                                default='java',
                                                                dot_qube=dot_qube,
                                                                to_get_property='language')

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration(dot_qube)

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'java': self.lib_java_options,
        }
        switcher.get(self.lib_struct.language)(dot_qube)

        self.lib_struct.is_github_repo, \
            self.lib_struct.is_repo_private, \
            self.lib_struct.is_github_orga, \
            self.lib_struct.github_orga \
            = prompt_github_repo(dot_qube)

        if self.lib_struct.is_github_orga:
            self.lib_struct.github_username = self.lib_struct.github_orga
        # create the chosen and configured template
        super().create_template_without_subdomain(self.TEMPLATES_LIB_PATH)

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.LIB_JAVA_TEMPLATE_VERSION
        }
        self.lib_struct.template_version, self.lib_struct.template_handle = switcher_version.get(
            self.lib_struct.language), f'lib-{self.lib_struct.language.lower()}'

        # perform general operations like creating a GitHub repository and general linting
        super().process_common_operations(domain='lib', language=self.lib_struct.language, dot_qube=dot_qube)

    def lib_java_options(self, dot_qube: dict or None) -> None:
        """ Prompts for lib-java specific options and saves them into the QubeTemplateStruct """
        pass

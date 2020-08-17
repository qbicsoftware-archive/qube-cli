import os
from pathlib import Path
from dataclasses import dataclass

from qube.create.github_support import prompt_github_repo
from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct
from qube.custom_cli.questionary import qube_questionary_or_dot_qube
from qube.common.version import load_qube_template_version


@dataclass
class TemplateStructGui(QubeTemplateStruct):
    """
    GUI-JAVA
    """
    main_class_prefix: str = ''


class GuiCreator(TemplateCreator):

    def __init__(self):
        self.gui_struct = TemplateStructGui(domain='gui')
        super().__init__(self.gui_struct)
        self.WD_Path = Path(os.path.dirname(__file__))
        self.TEMPLATES_GUI_PATH = f'{self.WD_Path.parent}/templates/gui'

        '"" TEMPLATE VERSIONS ""'
        self.GUI_JAVA_TEMPLATE_VERSION = load_qube_template_version('gui-java', self.AVAILABLE_TEMPLATES_PATH)

    def create_template(self, dot_qube: dict or None):
        """
        Handles the CLI domain. Prompts the user for the language, general and domain specific options.
        """

        self.gui_struct.language = qube_questionary_or_dot_qube(function='select',
                                                                question='Choose the project\'s primary language',
                                                                choices=['java'],
                                                                default='java',
                                                                dot_qube=dot_qube,
                                                                to_get_property='language')

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration(dot_qube)

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'java': self.gui_java_options,
        }
        switcher.get(self.gui_struct.language)(dot_qube)

        self.gui_struct.is_github_repo, \
            self.gui_struct.is_repo_private, \
            self.gui_struct.is_github_orga, \
            self.gui_struct.github_orga \
            = prompt_github_repo(dot_qube)

        if self.gui_struct.is_github_orga:
            self.gui_struct.github_username = self.gui_struct.github_orga
        # create the chosen and configured template
        super().create_template_without_subdomain(self.TEMPLATES_GUI_PATH)

        # switch case statement to fetch the template version
        switcher_version = {
            'java': self.GUI_JAVA_TEMPLATE_VERSION
        }
        self.gui_struct.template_version, self.gui_struct.template_handle = switcher_version.get(
            self.gui_struct.language), f'gui-{self.gui_struct.language.lower()}'

        # perform general operations like creating a GitHub repository and general linting
        super().process_common_operations(domain='gui', language=self.gui_struct.language, dot_qube=dot_qube)

    def gui_java_options(self, dot_qube: dict or None) -> None:
        """ Prompts for gui-java specific options and saves them into the QubeTemplateStruct """
        self.gui_struct.main_class_prefix = qube_questionary_or_dot_qube(function='text',
                                                                         question='Main class prefix',
                                                                         default='Qbic',
                                                                         dot_qube=dot_qube,
                                                                         to_get_property='main_class_prefix')

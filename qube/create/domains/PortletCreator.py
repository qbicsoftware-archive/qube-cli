import os
from pathlib import Path
from dataclasses import dataclass

from qube.create.github_support import prompt_github_repo
from qube.create.TemplateCreator import TemplateCreator
from qube.create.domains.QubeTemplateStruct import QubeTemplateStruct
from qube.custom_cli.questionary import qube_questionary_or_dot_qube
from qube.common.version import load_qube_template_version


@dataclass
class TemplateStructPortlet(QubeTemplateStruct):
    """
    PORTLET-GROOVY
    """
    main_class_prefix: str = ''
    use_openbis_client: str = 'no'
    use_openbis_raw_api: str = 'no'
    use_qbic_databases: str = 'no'
    use_vaadin_charts: str = 'no'


class PortletCreator(TemplateCreator):

    def __init__(self):
        self.portlet_struct = TemplateStructPortlet(domain='portlet')
        super().__init__(self.portlet_struct)
        self.WD_Path = Path(os.path.dirname(__file__))
        self.TEMPLATES_Portlet_PATH = f'{self.WD_Path.parent}/templates/portlet'

        '"" TEMPLATE VERSIONS ""'
        self.PORTLET_GROOVY_TEMPLATE_VERSION = load_qube_template_version('portlet-groovy', self.AVAILABLE_TEMPLATES_PATH)

    def create_template(self, dot_qube: dict or None):
        """
        Handles the PORTLET domain. Prompts the user for the language, general and domain specific options.
        """

        self.portlet_struct.language = qube_questionary_or_dot_qube(function='select',
                                                                    question='Choose the project\'s primary language',
                                                                    choices=['groovy'],
                                                                    default='groovy',
                                                                    dot_qube=dot_qube,
                                                                    to_get_property='language')

        # prompt the user to fetch general template configurations
        super().prompt_general_template_configuration(dot_qube)

        # switch case statement to prompt the user to fetch template specific configurations
        switcher = {
            'groovy': self.portlet_groovy_options,
        }
        switcher.get(self.portlet_struct.language)(dot_qube)

        self.portlet_struct.is_github_repo, \
            self.portlet_struct.is_repo_private, \
            self.portlet_struct.is_github_orga, \
            self.portlet_struct.github_orga \
            = prompt_github_repo(dot_qube)

        if self.portlet_struct.is_github_orga:
            self.portlet_struct.github_username = self.portlet_struct.github_orga
        # create the chosen and configured template
        super().create_template_without_subdomain(self.TEMPLATES_Portlet_PATH)

        # switch case statement to fetch the template version
        switcher_version = {
            'groovy': self.PORTLET_GROOVY_TEMPLATE_VERSION
        }
        self.portlet_struct.template_version, self.portlet_struct.template_handle = switcher_version.get(
            self.portlet_struct.language), f'portlet-{self.portlet_struct.language.lower()}'

        # perform general operations like creating a GitHub repository and general linting
        super().process_common_operations(domain='portlet', language=self.portlet_struct.language, dot_qube=dot_qube)

    def portlet_groovy_options(self, dot_qube: dict or None) -> None:
        """ Prompts for portlet-groovy specific options and saves them into the QubeTemplateStruct """
        self.portlet_struct.main_class_prefix = qube_questionary_or_dot_qube(function='text',
                                                                             question='Main class prefix',
                                                                             default='Qbic',
                                                                             dot_qube=dot_qube,
                                                                             to_get_property='main_class_prefix')
        self.portlet_struct.use_openbis_client = 'yes' if qube_questionary_or_dot_qube(function='confirm',
                                                                                       question='Do you want to use the openbis client?',
                                                                                       default='no',
                                                                                       dot_qube=dot_qube,
                                                                                       to_get_property='use_openbis_client') else 'no'
        self.portlet_struct.use_openbis_raw_api = 'yes' if qube_questionary_or_dot_qube(function='confirm',
                                                                                        question='Do you want to use the openbis raw API?',
                                                                                        default='no',
                                                                                        dot_qube=dot_qube,
                                                                                        to_get_property='use_openbis_raw_api') else 'no'
        self.portlet_struct.use_qbic_databases = 'yes' if qube_questionary_or_dot_qube(function='confirm',
                                                                                       question='Do you want to use QBiCs databases?',
                                                                                       default='no',
                                                                                       dot_qube=dot_qube,
                                                                                       to_get_property='use_qbic_databases') else 'no'
        self.portlet_struct.use_vaadin_charts = 'yes' if qube_questionary_or_dot_qube(function='confirm',
                                                                                      question='Do you want to use Vaadin charts?',
                                                                                      default='no',
                                                                                      dot_qube=dot_qube,
                                                                                      to_get_property='use_vaadin_charts') else 'no'

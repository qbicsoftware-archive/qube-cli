from dataclasses import dataclass


@dataclass
class QubeTemplateStruct:
    """
    First section declares the variables that all template have in common
    """
    domain: str = ''  # the domain of the template: Currently available: CLI, GUI
    language: str = ''  # the language the project will be mainly written in
    project_slug: str = ''  # the project name QUBE uses for almost all further processing
    project_short_description: str = ''  # a small description of the project
    template_version: str = ''  # the version of the provided QUBE template
    template_handle: str = ''  # the handle of the specific template, indicating which template is currently used
    full_name: str = ''  # the main author's name
    email: str = ''  # the main author's email
    copyright_holder: str = 'QBiC'

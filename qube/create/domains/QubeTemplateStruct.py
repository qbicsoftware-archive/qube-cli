from dataclasses import dataclass


@dataclass
class QubeTemplateStruct:
    """
    First section declares the variables that all template have in common
    """
    domain: str = ""  # the domain of the template: Currently available: CLI, GUI
    language: str = ""  # the language the project will be mainly written in
    project_slug: str = ""  # the project name QUBE uses for almost all further processing
    template_version: str = ""  # the version of the provided QUBE template
    template_handle: str = ""  # the handle of the specific template, indicating which template is currently used

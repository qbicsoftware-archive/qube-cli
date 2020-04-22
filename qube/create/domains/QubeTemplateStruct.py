from dataclasses import dataclass


@dataclass
class QubeTemplateStruct:
    """
    First section declares the variables that all template have in common
    """
    domain: str = ''  # Domain of the template such as CLI
    language: str = ''  # Language the project is primarily based on
    project_name: str = ''  # Project name, which may not necessarily by URL safe
    project_slug: str = ''  # Project name QUBE uses for almost all further processing
    project_short_description: str = ''  # A small description of the project
    template_version: str = ''  # Version of the provided QUBE template
    template_handle: str = ''  # Internal template handle e.g. cli-java
    full_name: str = ''  # Main author's name
    email: str = ''  # Main author's email
    copyright_holder: str = 'QBiC'  # Default QBiC
    github_username: str = ''  # The users Github username, therefore not qbicsoftware!

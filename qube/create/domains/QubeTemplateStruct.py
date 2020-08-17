from dataclasses import dataclass


@dataclass
class QubeTemplateStruct:
    """
    First section declares the variables that all template have in common
    """
    cookietemple_version: str = ''  # Version of cookietemple, which was used for creating the project
    full_name: str = ''  # Name of the template creator/organization
    email: str = ''  # Email of the creator
    project_name: str = ''  # Project's name the template is created for
    project_short_description: str = ''  # A short description of the project
    version: str = ''  # Version of the project; of the form: [0-9]*\.[0-9]*\.[0-9]*
    domain: str = ''  # Domain of the template
    language: str = ''  # Primary language
    project_slug: str = ''  # Project name cookietemple uses for almost all further processing
    project_slug_no_hyphen: str = ''  # Required for some Python project specific things, since - don't play nice with Python
    template_version: str = ''  # Version of the provided cookietemple template
    template_handle: str = ''  # Handle of the specific template, indicating which template is currently used
    github_username: str = ''  # Github username
    is_github_repo: bool = False  # Whether the user wants to create a GitHub repo automatically
    is_repo_private: bool = False  # Whether to create a private Github repository
    is_github_orga: bool = False  # Whether Github repository is part of an organization
    github_orga: str = ''  # Name of the GitHub organization
    copyright_holder: str = 'QBiC'  # Default QBiC
    license: str = ''  # License of the project

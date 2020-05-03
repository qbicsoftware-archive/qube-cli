import os

from qube.list.list import load_available_templates
from qube.util.dict_util import is_nested_dictionary

TEMPLATES_PATH = f'{os.path.dirname(__file__)}/../create/templates'

# QUBE main commands
MAIN_COMMANDS = ['create', 'lint', 'list', 'info', 'bump_version', 'sync']

# the fraction a given command could differ from the "right one" to be counted as this command by QUBE
SIMILARITY_FACTOR = (1 / 3)


def load_available_handles() -> set:
    """
    Load all available template handles.

    :return: A set of all available handles
    """
    available_templates = load_available_templates(f'{TEMPLATES_PATH}/available_templates.yml')
    unsplitted_handles = set()
    all_handles = set()
    nested_dict_to_handle_set(available_templates, unsplitted_handles)
    all_handles.update(unsplitted_handles)
    split_handles(unsplitted_handles, all_handles)

    return all_handles


def nested_dict_to_handle_set(available_templates, unsplitted_handles: set) -> None:
    """
    Extract the handles from loaded yml file.

    :param available_templates: The loaded yml file as a (nested) dict
    :param unsplitted_handles: The set to save the handles
    """
    if is_nested_dictionary(available_templates):
        for templ in available_templates.values():
            if not is_nested_dictionary(templ):
                unsplitted_handles.add(templ['handle'])
            else:
                nested_dict_to_handle_set(templ, unsplitted_handles)
    else:
        # a single template to append was reached
        unsplitted_handles.add(available_templates['handle'])


def split_handles(unsplitted_handles, all_handles) -> None:
    """
    Split handles into all possible combinations.

    :param unsplitted_handles: A set of unsplitted handles
    :param all_handles: All handles Cookietemple currently supports
    """
    for handle in unsplitted_handles:
        parts = handle.split('-')

        if len(parts) == 2:
            all_handles.add(parts[0])
        elif len(parts) == 3:
            all_handles.add(parts[0])
            all_handles.add(f'{parts[0]}-'+parts[1])

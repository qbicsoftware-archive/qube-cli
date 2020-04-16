import click

from qube.create.domains.CliCreator import CliCreator


def choose_domain(domain: str):
    """
    Prompts the user for the template domain.
    Creates the .cookietemple file.
    Prompts the user whether or not to create a Github repository
    :param domain: Template domain
    """

    if not domain:
        domain = click.prompt('Choose between the following domains ',
                              type=click.Choice(['cli', 'gui']),
                              show_choices=True)

    switcher = {
        'cli': CliCreator,
    }

    creator_obj = switcher.get(domain.lower(), lambda: 'Invalid domain!')()
    creator_obj.create_template()

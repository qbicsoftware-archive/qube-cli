.. _create:

================
Create a project
================

| Creating projects from templates is the heart of QUBE.
| To learn more about our templates please visit :ref:`available_templates`.

The creation of a new project can be invoked by::

    qube create

which will guide you through the creation process of your (customized) project via prompts.
They usually follow the pattern of domain (e.g. cli, gui, ...), subdomain (if applicable, e.g. website), language (e.g. Java), general prompts (e.g. name, email, ...) followed by template specific prompts (e.g. testing frameworks, ...).
| The template will be created at the current working directory, where QUBE has been called.
| It is also possible to directly create a specific template using its handle::

    qube create --handle <HANDLE>

| After the template has been created, linting (see :ref:`lint`) is automatically performed to verify that the template creation process was successful.
| Finally, you will be asked whether or not you want to automatically push your new project to Github.

Github support
-----------------

| QUBE uses `GitPython <https://gitpython.readthedocs.io/en/stable/>`_ and `PyGithub <https://pygithub.readthedocs.io/en/latest/introduction.html>`_ to automatically create a repository, add, commit and push all files.
  Moreover, issue labels and a development branch are created.
| When running :code:`qube create` for the first time, you may be prompted for your Github username, which will be saved locally in :code:`~/qube_conf.cfg`.
  Afterwards, if the answer to "Do you want to create a Github repository and push to it" was "yes", you will be prompted for your Github Personal Access Token.
| Please refer to the `official documentation <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_ on how to create one.
  QUBE only requires 'repo' access, so you only need to tick this box.
| QUBE then encrypts the Personal Access Token, adds the encrypted token to the :code:`qube_conf.cfg` file and saves the key locally in a hidden place. This is safer than Github's official way, which recommends the usage of environment variables or Github Credentials, which both save the token in plaintext.
| If you create a second project using QUBE at a later stage, you will not be prompted again for your Github username, nor your Personal Access Token. Both information will automatically be extracted and loaded on the fly.

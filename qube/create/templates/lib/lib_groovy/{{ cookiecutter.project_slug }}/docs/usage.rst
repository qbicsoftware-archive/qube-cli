=====
Usage
=====

To use {{ cookiecutter.project_slug }} in a project::

    add it to the POM of the project that you like to include this project:
    ``<groupId>life.qbic</groupId>
      	<artifactId>{{ cookiecutter.project_slug }}</artifactId>
      	<version>{{ cookiecutter.version }}</version>``

    Include the library into your code by importing the respective classes into your project:
    ``import package.path.to.class_name``

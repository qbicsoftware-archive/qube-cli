lib-groovy
---------

Purpose
^^^^^^^^

| lib-groovy is by design more open end than the other templates.
  The goal of a cli-lib project is not to be run as a standalone, but rather to be included as a library in other JVM based projects.

Design
^^^^^^^^

lib-groovy follows the standard Maven project layout.

.. code:: bash

    ├── AUTHORS.rst
    ├── CHANGELOG.rst
    ├── CODEOFCONDUCT.rst
    ├── .dependabot
    │   └── config.yml
    ├── docs
    │   ├── authors.rst
    │   ├── changelog.rst
    │   ├── codeofconduct.rst
    │   ├── conf.py
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   ├── requirements.txt
    │   └── usage.rst
    ├── .github
    │   ├── ISSUE_TEMPLATE
    │   │   ├── bug_report.md
    │   │   ├── feature_request.md
    │   │   └── general_question.md
    │   ├── pull_request_template.md
    │   └── workflows
    │       ├── build_docs.yml
    │       ├── build_package.yml
    │       ├── java_checkstyle.yml
    │       └── run_tests.yml
    ├── .gitignore
    ├── LICENSE
    ├── pom.xml
    ├── qube.cfg
    ├── .qube.yml
    ├── README.rst
    ├── .readthedocs.yml
    ├── src
    │   ├── main
    │   │   ├── groovy
    │   │   │   └── life
    │   │   │       └── qbic
    │   │   │           └── package-info.java
    │   │   └── resources
    │   │       └── .gitignore
    │   └── test
    │       ├── groovy
    │       │   └── life
    │       │       └── qbic
    │       │           └── package-info.java
    │       └── resources
    │           └── log4j2.xml
    ├── .travis.settings.xml
    └── .travis.yml

If you are unfamiliar with specific files/file types, you may find them in our :ref:`noobs`.


Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Unlike all of QBiC's JVM based projects, lib-groovy does not use QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_ for now.
2. `spock <http://spockframework.org/spock/docs/1.3/index.html/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
3. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
4. Four Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`build_package.yml`, which builds the `Maven <https://maven.apache.org/>`_ based project.
    3. :code:`java_checkstyle.yml`, which runs `Checkstyle <https://checkstyle.sourceforge.io/>`_ using `Google's Styleguides <https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml>`_.
    4. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    5. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    6. :code:`pr_to_master_from_development_only.yml` which fails if the PR does not come from a release or hotfix branch

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-groovy based projects.

cli-java
----------

Purpose
^^^^^^^^

| cli-java is the template of choice for `picocli <https://picocli.info/>`_ based command line applications, which require a JVM and the related ecosystem (e.g. due to requirement to use OpenBIS).
| These applications result in jars and can therefore only be started when a JDK is present. They do not ship with custom JREs!
| Therefore, if you are not bound to the JVM ecosystem, it may be a better idea to go for Python based projects, since Python is installed and available on every Unix machine.
| QUBE currently does not offer a cli-python template, but you may make use of `COOKIETEMPLE's cli-python <https://cookietemple.com>`_.

Design
^^^^^^^^

This template follows the standard Maven project layout.

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
    │   │   ├── java
    │   │   │   └── life
    │   │   │       └── qbic
    │   │   │           └── cli
    │   │   │               ├── SampleCommand.java
    │   │   │               ├── SampleEntryPoint.java
    │   │   │               └── SampleTool.java
    │   │   └── resources
    │   │       ├── log4j2.xml
    │   │       └── tool.properties
    │   └── test
    │       ├── java
    │       │   └── life
    │       │       └── qbic
    │       │           └── cli
    │       │               ├── SampleIntegrationTest.java
    │       │               └── SampleTest.java
    │       └── resources
    │           ├── log4j2.xml
    │           └── tool.properties
    ├── .travis.settings.xml
    └── .travis.yml


If you are unfamiliar with specific files/file types, you may find them in our :ref:`noobs`.

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Like all of QBiC's JVM based projects, cli-java uses QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_.
2. cli-java uses `picocli <https://picocli.info/>`_ to expose the commandline parameters to the user.
3. `junit4 <https://junit.org/junit4/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
4. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
5. Four Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`build_package.yml`, which builds the `Maven <https://maven.apache.org/>`_ based project.
    3. :code:`java_checkstyle.yml`, which runs `Checkstyle <https://checkstyle.sourceforge.io/>`_ using `Google's Styleguides <https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml>`_.
    4. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    5. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    6. :code:`pr_to_master_from_development_only.yml` which fails if the PR does not come from a release or hotfix branch

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

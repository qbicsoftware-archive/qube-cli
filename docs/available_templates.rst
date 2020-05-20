.. _available_templates:

=========================
Available templates
=========================

QUBE currently has the following templates available:

1. `cli-java`_
2. `lib-java`_
3. `gui-java`_
4. `service-java`_
5. `portlet-groovy`_

| In the following every template is devoted its own section, which explains its purpose, design, included frameworks/libraries and usage.
| If you are not yet familiar with QBiC's development processes, please read about them in our SOPs.
| Furthermore, if this is your first time developing any portlet or other QBiC related software, then it is recommend to read the :ref:`noobs`.

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
    6. :code:`pr_to_master_from_development_only.yml` which fails if a pull request from master does not come from development

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

lib-java
---------

Purpose
^^^^^^^^

| cli-lib is by design more open end than the other templates.
  The goal of a cli-lib project is not to be run as a standalone, but rather to be included as a library in other JVM based projects.

Design
^^^^^^^^

lib-java follows the standard Maven project layout.

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
    │   │   │           └── package-info.java
    │   │   └── resources
    │   │       └── .gitignore
    │   └── test
    │       ├── java
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

1. Like all of QBiC's JVM based projects, lib-java uses QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_.
2. `junit4 <https://junit.org/junit4/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
3. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
4. Four Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`build_package.yml`, which builds the `Maven <https://maven.apache.org/>`_ based project.
    3. :code:`java_checkstyle.yml`, which runs `Checkstyle <https://checkstyle.sourceforge.io/>`_ using `Google's Styleguides <https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml>`_.
    4. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    5. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    6. :code:`pr_to_master_from_development_only.yml` which fails if a pull request from master does not come from development

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

gui-java
------------

Purpose
^^^^^^^^

| gui-java is QBiC's choice for all templates, which require a Desktop user interface. Hence, the application is not necessarily on the web.
| The GUI framework of choice is `JavaFX 8 <https://openjfx.io/>`_. Be aware that most of the documentation has already moved past version 8.

Design
^^^^^^^^

gui-java follows the standard Maven project layout.

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
    │   │   │           └── gui
    │   │   │               ├── SampleApplication.java
    │   │   │               ├── SampleCommand.java
    │   │   │               └── SampleEntryPoint.java
    │   │   └── resources
    │   │       ├── log4j2.xml
    │   │       └── tool.properties
    │   └── test
    │       ├── java
    │       │   └── life
    │       │       └── qbic
    │       │           └── gui
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

1. Like all of QBiC's JVM based projects, lib-java uses QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_.
2. gui-java uses `JavaFX 8 <https://openjfx.io/>`_ to build the graphical user interface.
3. `junit4 <https://junit.org/junit4/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
4. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
5. Four Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`build_package.yml`, which builds the `Maven <https://maven.apache.org/>`_ based project.
    3. :code:`java_checkstyle.yml`, which runs `Checkstyle <https://checkstyle.sourceforge.io/>`_ using `Google's Styleguides <https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml>`_.
    4. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    5. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    6. :code:`pr_to_master_from_development_only.yml` which fails if a pull request from master does not come from development

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

service-java
-------------------

Purpose
^^^^^^^^

service-java is a base template for services, which are similar to commandline tools, but stay active until shutdown.

Design
^^^^^^^^

service-java follows the standard Maven project layout.

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
    │   │   │           └── gui
    │   │   │               ├── SampleApplication.java
    │   │   │               ├── SampleCommand.java
    │   │   │               └── SampleEntryPoint.java
    │   │   └── resources
    │   │       ├── log4j2.xml
    │   │       └── tool.properties
    │   └── test
    │       ├── java
    │       │   └── life
    │       │       └── qbic
    │       │           └── gui
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

1. Like all of QBiC's JVM based projects, lib-java uses QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_.
2. `junit4 <https://junit.org/junit4/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
3. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
4. Four Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`build_package.yml`, which builds the `Maven <https://maven.apache.org/>`_ based project.
    3. :code:`java_checkstyle.yml`, which runs `Checkstyle <https://checkstyle.sourceforge.io/>`_ using `Google's Styleguides <https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml>`_.
    4. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    5. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    6. :code:`pr_to_master_from_development_only.yml` which fails if a pull request from master does not come from development

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

portlet-groovy
---------------

Purpose
^^^^^^^^

| portlet-groovy is QBiC's template for portlets. Portlets are pluggable user interface software components, which are managed and displayed in a web portal.
| They are a major part of QBIC's web presence.

Design
^^^^^^^^

service-java follows the standard Maven project layout.

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
    │       ├── groovy_checkstyle.yml
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
    │   │   │   └── life.qbic.portal.portlet
    │   │   │       └── SamplePortlet.groovy
    │   │   ├── resources
    │   │   │   ├── developer.properties.example
    │   │   │   ├── .gitignore
    │   │   │   ├── life
    │   │   │   │   └── qbic
    │   │   │   │       └── portal
    │   │   │   │           └── portlet
    │   │   │   │               └── AppWidgetSet.gwt.xml
    │   │   │   ├── log4j2.xml
    │   │   │   └── portlet.properties
    │   │   └── webapp
    │   │       ├── VAADIN
    │   │       │   └── themes
    │   │       │       └── mytheme
    │   │       │           ├── addons.scss
    │   │       │           ├── mytheme.scss
    │   │       │           ├── styles.css
    │   │       │           └── styles.scss
    │   │       └── WEB-INF
    │   │           ├── liferay-display.xml
    │   │           ├── liferay-plugin-package.properties
    │   │           ├── liferay-portlet.xml
    │   │           ├── portlet.xml
    │   │           └── web.xml
    │   └── test
    │       ├── java
    │       │   └── life
    │       │       └── qbic
    │       │           └── portal
    │       │               └── portlet
    │       │                   ├── SamplePortletIntegrationTest.java
    │       │                   └── SamplePortletTest.java
    │       └── resources
    │           ├── log4j2.xml
    │           └── portlet.properties
    ├── .travis.settings.xml
    └── .travis.yml

If you are unfamiliar with specific files/file types, you may find them in our :ref:`noobs`.

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the creation you will be asked whether or not you want to use the

1. openbis client. This will include the openbis-client-lib in your project.
2. openbis raw api. This will include the openbis-api in your project.
3. qbic databases. This will include the mariadb-java-client in your project.
4. vaadin charts. This will include the vaadin-charts in your project.

1. Like all of QBiC's JVM based projects, lib-java uses QBiC's `parent-pom <https://github.com/qbicsoftware/parent-poms>`_.
2. `junit4 <https://junit.org/junit4/>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
3. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
4. Three Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`groovy_checkstyle.yml`, which runs `npm-groovy-lint <https://github.com/nvuillam/npm-groovy-lint>`_, which can be seen as a wrapper around `CodeNarc <https://codenarc.github.io/CodeNarc/>`_.
    3. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    4. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    5. :code:`pr_to_master_from_development_only.yml` which fails if a pull request from master does not come from development

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

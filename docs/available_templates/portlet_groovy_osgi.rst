portlet-groovy-osgi
---------------

Purpose
^^^^^^^^

| portlet-groovy-osgi is QBiC's template for portlets. Portlets are pluggable user interface software components, which are managed and displayed in a web portal.
| They are a major part of QBIC's web presence.
| The portlet is OSGi ready. The framework, into which the portlet is plugged, is independent of the portlet that is added and makes it more robust to changes.

Design
^^^^^^^^

portlet-groovy-osgi follows the standard Maven project layout.

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
    │   │   │       └── AppTheme.groovy
    │   │   │       └── SamplePortletUI.groovy
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
2. `spock <http://spockframework.org/spock/docs/1.3/index.html>`_ is currently QBiC's testing framework of choice.
   If you require mocking for any integration tests or advanced command line tests, `Mockito <https://site.mockito.org/>`_ may be useful.
3. Preconfigured `ReadTheDocs <https://readthedocs.org/>`_.
4. Three Github workflows are shipped with the template

    1. :code:`build_docs.yml`, which builds the `ReadTheDocs <https://readthedocs.org/>`_ documentation.
    2. :code:`groovy_checkstyle.yml`, which runs `npm-groovy-lint <https://github.com/nvuillam/npm-groovy-lint>`_, which can be seen as a wrapper around `CodeNarc <https://codenarc.github.io/CodeNarc/>`_.
    3. :code:`run_test.yml`, which runs all `junit4 <https://junit.org/junit4/>`_ tests.
    4. :code:`qube_lint.yml`, which runs QUBE's linting on the project.
    5. :code:`pr_to_master_from_development_only.yml` which fails if the PR does not come from a release or hotfix branch

Usage
^^^^^^^^

The main `Maven <https://maven.apache.org/>`_ commands such as :code:`mvn test`, :code:`mvn verify`, :code:`mvn package` and more are used to test and package cli-java based projects.

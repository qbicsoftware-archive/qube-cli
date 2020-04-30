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

    donut-cli
        ├── .dependabot
        │    └── config.yml
        ├── .github
        │    └── ISSUE_TEMPLATE
        │    │    └── bug_report.md
        │    │    └── feature_request.md
        │    │    └── general_question.md
        │    └── pull_request_template.md
        │    └── workflows
        │    │    └── build_docs.yml
        │    │    └── build_package.yml
        │    │    └── run_tests.yml
        │    │    └── java_checkstyle.yml
        ├── .gitignore
        ├── .qube.yml
        ├── qube.cfg
        ├── LICENSE
        ├── .readthedocs.yml
        ├── README.rst
        ├── AUTHORS.rst
        ├── CHANGELOG.rst
        ├── CODEOFCONDUCT.rst
        ├── docs
        │    └── conf.py
        │    └── Makefile
        │    └── make.bat
        │    └── requirements.txt
        │    └── readme.rst
        │    └── authors.rst
        │    └── changelog.rst
        │    └── codeofconduct.rst
        │    └── index.rst
        │    └── installation.rst
        │    └── usage.rst
        ├── pom.xml
        ├── src
        │    └── main
        │    │   └── java
        │    │   │   └── life
        │    │   │       └── qbic
        │    │   │           └── cli
        │    │   │               └── DonutCommand.java
        │    │   │               └── DonutEntryPoint.java
        │    │   │               └── DonutTool.java
        │    │   └── resources
        │    │   │   └── log4j2.xml
        │    │   │   └── tool.properties
        │    └── test
        │        └── java
        │            └── life
        │                └── qbic
        │                    └── cli
        │                        └── DonutIntegrationTest.groovy
        │                        └── DonutTest.groovy




Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
^^^^^^^^

lib-java
---------

Purpose
^^^^^^^^

Design
^^^^^^^^

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
^^^^^^^^

gui-java
------------

Purpose
^^^^^^^^

Design
^^^^^^^^

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
^^^^^^^^

service-java
-------------------

Purpose
^^^^^^^^

Design
^^^^^^^^

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
^^^^^^^^

portlet-groovy
---------------

Purpose
^^^^^^^^

Design
^^^^^^^^

.. code:: bash

   donut-portlet/
   ├── CODE_OF_CONDUCT.md
   ├── LICENSE
   ├── pom.xml
   ├── README.md
   └── src
       ├── main
       │   ├── groovy
       │   │   └── life
       │   │       └── qbic
       │   │           └── portal
       │   │               └── portlet
       │   │                   └── DonutPortlet.groovy
       │   ├── resources
       │   │   ├── life
       │   │   │   └── qbic
       │   │   │       └── portlet
       │   │   │           └── AppWidgetSet.gwt.xml
       │   │   ├── log4j2.xml
       │   │   ├── portlet.properties
       │   │   └── developer.properties
       │   └── webapp
       │       ├── VAADIN
       │       │   └── themes
       │       │       └── mytheme
       │       │           ├── addons.scss
       │       │           ├── mytheme.scss
       │       │           ├── styles.css
       │       │           └── styles.scss
       │       └── WEB-INF
       │           ├── liferay-display.xml
       │           ├── liferay-plugin-package.properties
       │           ├── liferay-portlet.xml
       │           ├── portlet.xml
       │           └── web.xml
       └── test
           └── java
               └── life
                   └── qbic
                       └── portal
                           └── portlet
                               └── DonutPortletTest.groovy

Included frameworks/libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usage
^^^^^^^^

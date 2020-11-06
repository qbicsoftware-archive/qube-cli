.. _changelog_f:

==========
Changelog
==========

This project adheres to `Semantic Versioning <https://semver.org/>`_.


2.6.1 (2020-11-06)
------------------

**Added**

* Add report generation script to common files

**Fixed**

**Dependencies**

**Deprecated**


2.6.0 (2020-10-27)
------------------

**Added**

* Add template for OSGi Groovy library bundles
* Add template for OSGi Groovy portlet bundles

**Fixed**

* Fix missing license property bug, that showed up if the license placeholder was referenced in a template.

**Dependencies**

**Deprecated**

* Java 8, templates now build with JDK 11.


2.5.1 (2020-10-16)
------------------

**Added**

**Fixed**

* qube lint now wraps too long lines

**Dependencies**

**Deprecated**


2.5.0 (2020-10-06)
------------------

**Added**

* verbose support #186

**Fixed**

* sync workflow now polls instead of being triggered on push #170
* renamed branch protection workflow #190
* refactored sync command
* Faster build time by fixing the order of Maven repositories for dependency resolving
* Ignore rule for Vaadin widgetsets

**Dependencies**

**Deprecated**


2.4.6 (2020-10-02)
------------------

**Added**

**Fixed**

* Fix missing properties for portlet domain
* Fix #169

**Dependencies**

**Deprecated**


2.4.5 (2020-10-02)
------------------

**Added**

* Ignores additional Maven files

**Fixed**

* Preserve boolean case when loading YAML boolean values
* Force push changes to the TEMPLATE branch during sync

**Dependencies**

**Deprecated**


2.4.4 (2020-10-02)
------------------

**Added**

**Fixed**

* Fix the pull request creation after updating syncing the TEMPLATE branch. Qube reported a :code:`FileNotFoundError` for the sync workflow file, because it tried to access this file in an empty directory.

* Removed redundant sync_workflow workarounds

* sync and maven test workflow yaml syntax

**Dependencies**

**Deprecated**


2.4.3 (2020-10-01)
------------------

**Added**

**Fixed**

* Sets correct repo owner for the :code:`qube sync`

**Dependencies**

**Deprecated**


2.4.2 (2020-10-01)
------------------

**Added**

* Enables debug logging

**Fixed**

**Dependencies**

**Deprecated**


2.4.1 (2020-10-01)
------------------

**Added**

**Fixed**

**Dependencies**

* Updated parent pom to 3.1.1
* Updated template versions to 1.0.1

**Deprecated**

2.4.0 (2020-10-01)
------------------

**Added**

* Now using Johnny5 for the sync workflow by default
* Maven caching for tests

**Fixed**

* Add all `src/main/webapp/VAADIN/widgetsets` folders to `.gitignore`
* Makefile now uses pip instead of setup.py by default

**Dependencies**

**Deprecated**


2.3.0 (2020-09-28)
------------------

**Added**

* Added release deployment GA workflow for JVM templates
* Added workflow to build software reports and internal documentation

**Fixed**

* Fixed parent-pom version being outdated -> 3.1.0
* Fixed further outdated dependencies in various poms
* Fixed release URL in all poms
* Allow PR from 'hotfix' branches

**Dependencies**

**Deprecated**

* Removed PR allowance from patch branches
* Removed Travis CI support


2.2.0 (2020-08-21)
------------------

**Added**

**Fixed**

* Couple of docs fixes
* Now always using hyphens for options

**Dependencies**

**Deprecated**


2.1.0 (2020-08-21)
------------------

**Added**

* Option to config --view to get the current set configuration
* Option --set_token to set the sync token again
* Sync docs improved
* Support for QUBE TODO: and TODO QUBE:

**Fixed**

* Sync for organization repositories

**Dependencies**

**Deprecated**


2.0.0 (2020-08-17)
------------------

**Added**

* Strong code refactoring overhauling everything
* Added config command to recreate config files
* Added upgrade command to update qube itself
* Added sync command to sync a qube project
* Help messages are now custom
* Bump-version lints versions before updating
* Added a metaclass to fetch all linting functions
* Master requires PR review & no stale PRs
* Greatly improved the documentation
* Much more...

**Fixed**

* PR check WF now correctly requires PRs to master to be from *patch* or *release* branches

**Dependencies**

* Too many updates to jot down...!

**Deprecated**


1.4.1 (2020-05-23)
------------------

**Added**

**Fixed**

* Reverted simplified common files copying, since it broke Github support

**Dependencies**

**Deprecated**

1.4.0 (2020-05-23)
------------------

**Added**

* Added Rich for tracebacks & nice tables
* New ASCII Art!

**Fixed**

**Dependencies**

**Deprecated**

1.3.2 (2020-05-22)
------------------

**Added**

* Strongly simplified common files copying
* info now automatically reruns the most similar handle

**Fixed**

**Dependencies**

**Deprecated**

1.3.1 (2020-05-20)
------------------

**Added**

* Checking whether project already exists on readthedocs

**Fixed**

* bump-version SNAPSHOT handling strongly improved

**Dependencies**

* requests==2.23.0 added
* packaging==20.4 added

**Deprecated**

1.3.0 (2020-05-20)
------------------

**Added**

* bump-version now supports SNAPSHOTS
* documentation about 4 portlet prompts
* new COOKIETEMPLE docs css

**Fixed**

* Tests GHW names

**Dependencies**

**Deprecated**

1.2.1 (2020-05-03)
------------------

**Added**

* Refactored docs into common files

**Fixed**

**Dependencies**

**Deprecated**

1.2.0 (2020-05-03)
------------------

**Added**

* QUBE linting workflow for all templates
* PR to master from development only WF
* custom COOKIETEMPLE css

**Fixed**

* setup.py development status
* max width for docs for all templates
* PyPi badge is now green

**Dependencies**

* flake 3.7.9 -> 3.8.1

**Deprecated**


1.1.0 (2020-05-03)
------------------

**Added**

* The correct version tag :)

**Fixed**

* Readthedocs width is now

**Dependencies**

**Deprecated**

1.0.0 (2020-05-03)
------------------

**Added**

* Created the project using COOKIETEMPLE
* Added create, list, info, bump-version, lint based on COOKIETEPLE
* Added cli-java template
* Added lib-java template
* Added gui-java template
* Added service-java template
* Added portlet-groovy template

**Fixed**

**Dependencies**

**Deprecated**

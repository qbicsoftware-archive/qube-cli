.. _changelog_f:

==========
Changelog
==========

This project adheres to `Semantic Versioning <https://semver.org/>`_.


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

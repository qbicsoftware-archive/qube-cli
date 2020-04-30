.. _lint:

=====================
Linting your project
=====================

| `Linting <https://en.wikipedia.org/wiki/Lint_(software)>`_ is the process of statically analyzing code to find code style violations and to detect errors.
| QUBE implements a custom linting system, but depending on the template external tools liting tools may be additionally be called.

QUBE linting
-----------------------

QUBE lint can be invoked on an existing project using::

    qube lint <OPTIONS> <PATH>

QUBE's linting is divided into three distinct phases.

1. All linting functions, which all templates share are called and the results are collected.
2. Template specific linting functions are invoked and the results are appended to the results of phase 1
3. Template specific external linters are called (e.g. checkstyle for Java based projects)

The linting results of the first two phases are assigned into 3 groups:

1. Passed
2. Passed with warning
3. Failed

If any of the checks failed linting stops and returns an error code.

.. figure:: images/linting_example.png
   :scale: 100 %
   :alt: Linting example

   Linting applied to a newly created portlet-groovy project.

To examine the reason for a failed linting test please follow the URL. All reasons are explained in the section :ref:`Linting_codes`.

.. _linting_codes:

Linting codes
-----------------

TODO

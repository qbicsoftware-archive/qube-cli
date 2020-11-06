.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_slug }}, run this command in your terminal:

.. code-block:: console

    $ mvn install

This is the preferred method to install {{ cookiecutter.project_slug }}, as it will always install the most recent stable release.

If you don't have `maven`_ installed you can get it from `here`_

.. _maven: https://maven.apache.org/
.. _here: https://maven.apache.org/

From sources
------------

The sources for {{ cookiecutter.project_slug }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/qbicsoftware/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/qbicsoftware/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ mvn install


.. _Github repo: https://github.com/qbicsoftware/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/qbicsoftware/{{ cookiecutter.project_slug }}/tarball/master

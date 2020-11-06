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

 Prerequisites:
 --------------

      - JDK11
      - Maven > 3
      - Internet connection to resolve dependencies


 Local execution
 ---------------

      For development purposes, the application can be run as servlet in a
      local Jetty environment, without the need to set up and host a local
      OSGi environment.

      To run the application as servlet locally, check out the latest commit
      locally, and run the following command in your command line:

.. code-block:: console

      $mvn clean -P no-liferay install jetty:run

      This will run the server listening on the localhost port 8080 and can be
      accessed via `http://localhost:8080`.

      ## Create an OSGi bundle

      In order to provide the application as an OSGi bundle, run the following
      command:

.. code-block:: console
      $mvn clean -P liferay package

      This will create the OSGi bundle as JAR archive under the directory
      `target` in the working directory.


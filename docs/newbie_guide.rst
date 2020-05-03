.. _noobs:

=============================
Newbie Guide to QBiC software
=============================

This is the newbie guide to developing software for QBiC. This is not solely the documentation for QUBE.
If you are looking solely for QUBE's documentation, please proceed with the next sections.

Required tools for Java/Groovy development
------------------------------------------

1. Java
~~~~~~~

Our production and test instances use `OpenJDK 1.8`_ and this is mirrored in our build system.

Installation of OpenJDK varies across operating systems. So it is strongly advised to read more about how to install OpenJDK in your
operating system. Most Linux-based operating systems offer OpenJDK through package managers (e.g., ``pacman``, ``apt``, ``yum``).

Make sure you install a Java development kit (JDK) and not just a Java runtime environment (JRE).

2. Maven
~~~~~~~~

`Apache Maven <https://maven.apache.org/>`_ is one of those rare tools whose true purpose
might be hard to grasp in the beginning, yet it is extremely easy to install. If this is your
first time using `maven`_, make sure to read `Maven in 5 minutes`_ and `Maven getting started guide`_.

It is up to you to decide whether to install `maven`_ using your
favorite package manager or `install it manually`_. In any case, make sure you install the most recent version available.

3. Other tools
~~~~~~~~~~~~~~

We use the `Travis CI client <https://github.com/travis-ci/travis.rb>`_ to `generate encrypted credentials`_.
You can follow `this guide`_ to get the `Travis CI client <https://github.com/travis-ci/travis.rb>`_ installed on your machine.

What to do once you’ve generated your project using QUBE?
------------------------------------------------------------------

QUBE creates just a sample project. Sadly, you will still have to write your own code, tests and documentation.

Write tests, check code coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The generated folder already contains simple `jUnit 4 <https://junit.org/junit4/>`_ unit tests (i.e.,
in :code:`src/test/java/life/qbic/portal/portlet/DonutPortletTest.java`).
Writing code that tests your code is an important part of the development lifecycle (see: https://makeameme.org/meme/Yo-dawg-I-wgn8jg).

As a general guideline, try to code the *logic* of your portlet independent of the user interface so you can easily write code that tests your portlet.

`Maven <https://maven.apache.org/>`_ has been configured to execute unit tests under the
:code:`src/test` folder that match the ``*Test`` name (e.g., DonutPortletTest). To run all unit tests, you use the following command:

.. code:: bash

   mvn test

We use `Cobertura <https://cobertura.github.io/cobertura/>`_ to generate coverage reports. To run the unit
tests and generate a code coverage report, simply run:

.. code:: bash

   mvn cobertura:cobertura

Similarly, we have configured the `Maven <https://maven.apache.org/>`_ plug-ins to run integration tests.
These tests are also under the ``src/test`` folder, but their names must end with ``*IntegrationTest``, such as
``DonutPortletIntegrationTest``. Running integration tests can be a time-consuming task, so these are,
usually, not executed alongside the unit tests. To execute the integration tests, invoke the following command:

.. code:: bash

   mvn verify

Test your code locally
~~~~~~~~~~~~~~~~~~~~~~

You can easily run the unit and integration tests for libraries you have written by using the :code:`mvn test` command. This is, more or less, what
our build system does. Take a look at the :code:`.travis.yml` file located in the :code:`common-files` if you want to know all implementation details
related to how we do continuous integration.

Testing a portlet locally using Jetty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to the generated folder (i.e., ``generated/donut-portlet`` in our
case) and run:

.. code:: bash

   mvn jetty:run

You should see an output similar to:

.. code:: bash

   [INFO] Started ServerConnector@67c06a9e{HTTP/1.1,[http/1.1]}{0.0.0.0:8080}
   [INFO] Started @30116ms
   [INFO] Started Jetty Server

Direct your browser to :code:`localhost:8080`. If everything went fine, you
will see a portlet with several controls. So far so good,
congratulations!

Interact with the UI and, if this is your first portlet, we strongly
suggest you to try to change a few things in the code and see what
happens after you test again.

Testing other tools locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We configured a `Maven <https://maven.apache.org/>`_ plug-in to generate *stand-alone* JAR
files for projects of type cli, service and gui.
`Maven <https://maven.apache.org/>`_ will package all of the needed dependencies inside one
single JAR file.

To test your CLI tool locally, you first need to *package* your
artifact using `Maven <https://maven.apache.org/>`_ in the generated project folder:

.. code:: bash

   mvn package

You then need to use the following command:

.. code:: bash

   java -jar target/<project_slug>-<version>-jar-with-dependencies.jar

That is:

.. code:: bash

   java -jar target/donut-cli-1.0.0-SNAPSHOT-jar-with-dependencies.jar

Create a new GitHub repository for your new project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You now have a new QBiC project with all the required dependencies and configuration files.
You still need to create a remote repository for it, though, so it’s available for everyone.
QUBE should have prompted you for your Github username and personal access token to conduct this process automatically.
If you declined the automatic creation of the repository, then please follow `Create Github Repository`_ to
create a repository on GitHub. For this example, we will still use ``donut-portlet`` as the
name of our repository. You need to create your GitHub repository under the `QBiC GitHub organization`_,
so you need writing access. Ask your favorite QBiC admin if you do not yet have writing rights.

Secure your configuration files before pushing to Git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It might happen that you accidentally pushed a file containing sensitive data. Well - happens.

The good part is that this is reversible. The bad part is that, due to compliance with EU law, whenever
one of these incidents occurs, the only way to do this right is to not only to `delete all compromised files from the repository`_,
but also to change all compromised passwords, which is a great way to ruin someone’s day.

So don’t do it, but if you do, or if you discover such an incident, just know that this **should** be reported.

Check that everything worked in Travis-CI.com
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The generated project folder contains a :code:`.travis.yml` file that will help you integrate your
GitHub repository with `Travis CI`_, our continuous integration service. Broadly speaking, everytime you
*push* a change into your GitHub repository, `Travis CI`_ will use the ``.travis.yml`` file to know what to do.

Your repository should have been automatically added to our continuous integration system, but there has been a lot of changes in the platform
that your experience might differ. Follow these steps to check that everything worked as advertised:

1. Navigate to (https://travis-ci.com/). Use your GitHub account to
   authenticate.
2. Click on your name (upper-right corner). You should see your profile
   in `Travis CI`_.
3. Click the *Sync account* button
4. Look for your repository. You might want to filter repositories by
   entering the full name of your repository (i.e., ``donut-portlet``)
   or parts of it.
5. Once you’ve found your repository, click on the *Settings* button displayed next to it.

If you see the settings page, then it means that everything went fine.
Make sure that the general settings of your repository match the ones shown below:

Report generation using Maven
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We generate reports using `the Maven site plugin`_. The goal ``site``
will output several reports which you can then find in the
``target/site`` directory. So, in other words, running ``mvn site`` will
populate the ``target/site`` folder with all configured reports, as
defined in `parent-poms <https://github.com/qbicsoftware/parent-poms>`_.

Reports are generated in HTML format, so you can access them in your
browser by entering
``file://<full-path-to-your-local-repo>/target/site/index.html`` (e.g.,
``file:///home/homer/donut-portlet/target/site/index.html``; shh… no
that’s not a typo, that’s three forward slashes, remember that full
paths start with ``/``\ ) in your browser’s address bar.

Provide encrypted information to Travis CI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any person on the internet can download `Maven`_ artifacts from
our `public Maven repository`_. But in order to upload artifacts to our
repository, you will need proper authentication.

Since all of our code is open source, it would not be a good idea to use
cleartext passwords and distribute them in our repositories. This is
also true for other private information such as license codes. However,
`Travis CI`_ requires this same information to be present at
build time. Luckily, `Travis CI`_ offers `a simple way to add
encrypted environment variables`_. You do not need to fully understand
the implementation details to follow this guide, but no one will be
angry at you if you do.

You only need to execute a single command using the `Travis CI client <https://github.com/travis-ci/travis.rb>`_ to add
an encrypted variable to your ``.travis.yml``. Let’s say, for instance, that you need to add an environment variable,
``NUCLEAR_REACTOR_RELEASE_CODE`` whose value is ``d0nut5_Ar3_t4sty``. You would have to use the following command:

.. code:: bash

   travis encrypt "NUCLEAR_REACTOR_RELEASE_CODE=d0nut5_Ar3_t4sty" --add env.global --pro

This command will automatically edit ``.travis.yml`` (if you want edit
the file yourself, do not use the ``--add env.global`` parameter).

Maven credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable `Maven`_ deployments in `Travis CI`_, add both
``MAVEN_REPO_USERNAME`` and ``MAVEN_REPO_PASSWORD`` as encrypted
variables in your ``.travis.yml`` file like so:

.. code:: bash

   travis encrypt "MAVEN_REPO_USERNAME=<username>" --add env.global --pro
   travis encrypt "MAVEN_REPO_PASSWORD=<password>" --add env.global --pro

Ask the people who wrote this guide about the proper values of ``<username>`` and ``<password>``.
Encrypted values in `Travis CI`_ are bound to their GitHub repository, so you cannot simply
copy them from other repositories.

Using Vaadin Charts add-on in your portlet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This add-on requires you to have a proper license code. If your portlet
requires this add-on, add the ``VADIN_CHARTS_LICENSE_CODE`` as an
encrypted variable in ``.travis.yml``:

.. code:: bash

   travis encrypt "VAADIN_CHARTS_LICENSE_CODE=<license-code>" --add env.global --pro

Ask around for the license code.

Publish your first version
~~~~~~~~~~~~~~~~~~~~~~~~~~

In your local GitHub repository directory (i.e., ``donut-portlet``) run
the following commands:

.. code:: bash

   git init
   git add .
   git commit -m "Initial commit before pressing the 'flush radioactive material' button"
   git remote add origin https://github.com/qbicsoftware/donut-portlet
   git push origin master
   git checkout -b development
   git push origin development

Of course, you must replace ``donut-portlet`` with the real name of your
repository. You can now start using your repository containing your brand new portlet.

Change default branch
~~~~~~~~~~~~~~~~~~~~~

We strongly recommend you to set the ``development`` branch as your default branch by following `setting the default branch`_.

Dependabot
~~~~~~~~~~~~~~~

Almost all of QUBE's template use `Dependabot <https://dependabot.com/>`_ to automatically submit pull requests to the project's
repository whenever an update for a dependency was released. If you pushed your project to Github using QUBE's Github support
everything is already setup for you. If not, you may need to create a ``development`` branch and a ``dependabot`` issue label.

Read the docs
~~~~~~~~~~~~~~~~~~

| All of QUBE's templates come with `Read the Docs`_ preconfigured.
| The only thing left for you to do is to enable your repository for `Read the Docs`_.
  Please follow the `importing your documentation guide <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.
  You should not need to manually import your project if you are a member of QBiC software (which you should be!).

Github Actions
~~~~~~~~~~~~~~~~~~

All of QUBE's templates feature `Github Actions <https://github.com/features/actions>`_ support. Github Actions is part of our continuous integration setup
and various template specific workflows are active (on push). Examples are the automatial runs of test suites, package building, linting and more.
You usually should not need to touch them, but feel free to add additional workflows. They are located in ``.github/workflows/``.

.. _Read the Docs: https://readthedocs.org/
.. _Maven in 5 minutes: https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html
.. _Maven getting started guide: https://maven.apache.org/guides/getting-started/index.html
.. _install it manually: https://maven.apache.org/install.html
.. _generate encrypted credentials: #deploying-your-project-as-a-maven-artifact
.. _this guide: https://github.com/travis-ci/travis.rb#installation
.. _read more about the origin of the problem: https://developer.fedoraproject.org/tech/languages/ruby/gems-installation.html
.. _setting the default branch: https://help.github.com/articles/setting-the-default-branch/
.. _in this page: https://qbictalk.slack.com/apps/A0F81FP4N-travis-ci
.. _Maven: https://maven.apache.org/
.. _public Maven repository: https://qbic-repo.am10.uni-tuebingen.de
.. _a simple way to add encrypted environment variables: https://docs.travis-ci.com/user/encryption-keys/
.. _Travis CI: https://travis-ci.org/
.. _delete all compromised files from the repository: https://help.github.com/en/articles/removing-sensitive-data-from-a-repository
.. _the Maven site plugin: https://maven.apache.org/plugins/maven-site-plugin/
.. _Create Github Repository: https://help.github.com/articles/create-a-repo/
.. _QBiC GitHub organization: https://github.com/qbicsoftware
.. _simple name: https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#getSimpleName--
.. _Required tools for Java development: #required-tools-for-java-development
.. _Variables that apply to all applications: #variables-that-apply-for-portlets--command-line-tools--services-and-javafx-stand-alone-applications
.. _Variables that apply only for portlets: #variables-that-apply-only-for-portlets
.. _Layout of the generated projects: #layout-of-the-generated-projects
.. _What to do once you have generated your project: #what-to-do-once-you-ve-generated-your-project
.. _Write tests and check code coverage: #write-tests--check-code-coverage
.. _Test your code locally: #test-your-code-locally
.. _Testing a portlet locally using Jetty: #testing-a-portlet-locally-using-jetty
.. _Testing other tools locally: #testing-other-tools-locally
.. _Create a new GitHub repository for your new project: #create-a-new-github-repository-for-your-new-project
.. _Secure your configuration files before pushing to Git: #secure-your-configuration-files-before-pushing-to-git
.. _Check that everything worked in Travis-CI.com: #check-that-everything-worked-in-travis-cicom
.. _Report generation using Maven: #report-generation-using-maven
.. _Provide encrypted information to Travis CI: #provide-encrypted-information-to-travis-ci
.. _Maven credentials: #maven-credentials
.. _GitHub personal access token for automatic report publishing: #github-personal-access-token-for-automatic-report-publishing
.. _Using Vaadin Charts add-on in your portlet: #using-vaadin-charts-add-on-in-your-portlet
.. _Publish your first version: #publish-your-first-version
.. _Change default branch: #change-default-branch
.. _Getting slack notifications from Travis CI (optional): #getting-slack-notifications-from-travis-ci--optional-
.. _OpenJDK 1.8: http://openjdk.java.net/

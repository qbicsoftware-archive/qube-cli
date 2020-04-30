.. _noobs:

=============================
Newbie Guide to QBiC software
=============================

Table of contents
-----------------

-  `Required tools for Java development`_

   -  `1. Java`_
   -  `2. Maven`_
   -  `3. Other tools`_

-  `Template variables`_

   -  `Global variables`_
   -  `Variables that apply for portlets, command-line tools, services
      and JavaFX stand-alone applications`_
   -  `Variables that apply only for portlets`_

-  `Layout of the generated projects`_
-  `What to do once you’ve generated your project?`_

   -  `Write tests, check code coverage`_
   -  `Test your code locally`_

      -  `Testing a portlet locally using Jetty`_
      -  `Testing other tools locally`_

   -  `Create a new GitHub repository for your new project`_
   -  `Secure your configuration files before pushing to Git`_
   -  `Check that everything worked in Travis-CI.com`_
   -  `Report generation using Maven`_
   -  `Provide encrypted information to Travis CI`_

      -  `Maven credentials`_
      -  `GitHub personal access token for automatic report publishing`_
      -  `Using Vaadin Charts add-on in your portlet`_

   -  `Publish your first version`_
   -  `Change default branch`_
   -  `Getting slack notifications from Travis CI (optional)`_

Required tools for Java development
-----------------------------------

1. Java
~~~~~~~

Our production and test instances use `OpenJDK 1.8`_ and this is
mirrored in our build system.

Installation of OpenJDK varies across operating systems. So it is
strongly advised to read more about how to install OpenJDK in your
operating system. Most Linux-based operating systems offer OpenJDK
through package managers (e.g., ``pacman``, ``apt``, ``yum``) and `there
seems to be an OpenJDK version for Windows available`_.

If you want to use Oracle’s JDK, visit `Oracle’s download page`_ to get
the binaries.

Make sure you install a Java development kit (JDK) and not a Java
runtime environment (JRE).

.. _Required tools for Java development: #required-tools-for-java-development
.. _1. Java: #1-java
.. _2. Maven: #2-maven
.. _3. Other tools: #3-other-tools
.. _Template variables: #template-variables
.. _Global variables: #global-variables
.. _Variables that apply for portlets, command-line tools, services and JavaFX stand-alone applications: #variables-that-apply-for-portlets--command-line-tools--services-and-javafx-stand-alone-applications
.. _Variables that apply only for portlets: #variables-that-apply-only-for-portlets
.. _Layout of the generated projects: #layout-of-the-generated-projects
.. _What to do once you’ve generated your project?: #what-to-do-once-you-ve-generated-your-project-
.. _Write tests, check code coverage: #write-tests--check-code-coverage
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
.. _there seems to be an OpenJDK version for Windows available: https://stackoverflow.com/questions/5991508/openjdk-availability-for-windows-os
.. _Oracle’s download page: http://www.oracle.com/technetwork/java/javase/downloads/index.html

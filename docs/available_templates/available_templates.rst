.. _available_templates:

=========================
Available templates
=========================

qube currently has the following templates available:

1. `cli-java`_
2. `gui-java`_
3. `lib-java`_
4. `lib-groovy`_
5. `service-java`_
6. `portlet-groovy`_
7. `portlet-groovy-osgi`_

In the following every template is devoted its own section, which explains its purpose, design, included frameworks/libraries, usage and frequently asked questions.
A set of frequently questions, which all templates share see here: :ref:`all_templates_faq` FAQ.
It is recommended to use the sidebar to navigate this documentation, since it is very long and cumbersome to scroll through.

.. include:: cli_java.rst
.. include:: gui_java.rst
.. include:: lib_java.rst
.. include:: lib_groovy.rst
.. include:: service_java.rst
.. include:: portlet_groovy.rst
.. include:: portlet_groovy_osgi.rst


.. _all_templates_faq:

Shared FAQ
----------------------

How do I setup Read the Docs?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

qube ships with a full, production ready `Read the Docs <https://readthedocs.org/>`_ setup.
You need to `import your documentation <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_ on Read the Docs website.
Do not forget to sync your account first to see your repository.

What is Dependabot and how do I set it up?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Dependabot <https://dependabot.com/>`_ is a service, which (for supported languages) automatically submits pull requests for dependency updates.
qube templates ship with dependabot configurations, if the language is supported by Dependabot.
To enable Dependabot you need to login (with your Github account) and add your repository (or enable Dependabot for all repositories).
Note that you need to do this for every organization separately. Dependabot will then pick up the configuration and start submitting pull requests!

How do I add a new template?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please follow :ref:`adding_templates`.

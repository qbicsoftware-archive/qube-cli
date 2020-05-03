.. _list_info:

=============================================
Getting information about available templates
=============================================

| Although, information on all QUBE templates is provided in :ref:`available_templates` in our documentation, it is often times more convenient to get a quick overview from the commandline.
| Hence, QUBE provides two commands :code:`list` and :code:`info`, which print information on all available templates with different levels of detail.

list
-----

QUBE list can be invoked via::

    qube list

.. figure:: images/list_example.png
   :scale: 100 %
   :alt: List example

   Example output of :code:`qube list`. Note that the content of the output is of course subject to change.

:code:`qube list` is restricted to the short descriptions of the templates. If you want to read more about a specific (sets of) template, please use the :ref:`info_f` command.

.. _info_f:

info
------

| The :code:`info` command should be used when the short description of a template is not sufficient and a more detailed description is required.
| Moreover, when you are unsure which template suits you best and you would like to read more about a specific subset of templates further, :code:`info` is your friend.

Invoke :code:`qube info` *via*:

    qube info <HANDLE>

.. figure:: images/info_example.png
   :scale: 100 %
   :alt: Info example

   Example output of :code:`qube info`. The handle can also be shortened to e.g. just *cli*, to output all command line templates of QUBE.

It is not necessary to use a full handle such as *cli-java*. Alternatively, a subset of the handle such as *cli* can be used and as a result detailed information on all templates of the requested domain will be printed.

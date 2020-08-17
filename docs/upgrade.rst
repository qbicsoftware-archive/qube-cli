.. _upgrade:

=====================
Upgrade qube
=====================

Every time qube is run it will automatically contact PyPI to check whether the locally installed version of qube is the latest version available.
If not

.. code:: console

    $ qube upgrade

can be run. The command calls `pip <https://pypi.org/project/pip/>`_ in upgrade mode to upgrade qube to the latest version.
For this to work however, it is required that pip is accessible from your PATH.

It is advised not to mix installations using setuptools directly and pip. If you are not a developer of qube this should not concern you.

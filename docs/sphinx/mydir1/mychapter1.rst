Introduction
************

Getting started with Sphinx
===========================
Install `sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ and build
the `html` documentation with:

.. code-block:: bash

    sphinx-build -M html . _build

then open the html file with:

.. code-block:: bash

    firefox ./_build/html/index.html

The generated documentation will look like figure :ref:`Fig.1 <my-figure>`

.. _my-figure:

.. figure:: img/screenshot.*
   :scale: 50%
   :alt: Sphinx screenshot

   Typical sphinx html documentation

Configuration file
==================
A typical example configuration file is :download:`conf.py </conf.py>`:

.. literalinclude:: /conf.py
   :language: python
   :linenos:
 
It was created with the ``sphinx-quickstart`` command.


Benchmarking results
====================
We report the performance (in seconds) in the following table:

+-----------+------------+
|           | Piz Daint  |
+===========+============+
| SqPatch   | 3059.34    |
+-----------+------------+


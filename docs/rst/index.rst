.. toctree::
   :caption: Contents:
   :maxdepth: 2

   mydir1/mychapter1.rst
   XXX <mydir1/mychapter1.rst>
   Getting started <started>
   Reference Guide <reference>

.. this is a comment: :hidden:   

=============
JG Cheatsheet
=============

.. code-block:: none

  # with overline, for parts
  * with overline, for chapters
  =, for sections
  -, for subsections
  ^, for subsubsections
  ", for paragraphs


-----------------
 Subtitle: Titles
-----------------

 * All sections marked with the same adornment style are deemed to be at the same level:

Chapter 1 Title
===============

Section 1.1
-----------

1.1.1
~~~~~

1.1.2
~~~~~

Section 1.2
-----------

1.2.1
~~~~~

1.2.2
~~~~~


Chapter 2 Title
===============

etc...

---------------------
 Subtitle: Text style
---------------------

*italic* / **bold** / `interpreted` / ``inline`` / :class:`None`

---------------------
 Subtitle: Tables
---------------------

=== ===
 A   B
=== ===
 a   b
aa   bb
=== ===

---------------------
 Subtitle: Links
---------------------

* `SPH-EXA website <https://hpc.dmi.unibas.ch/HPC/SPH-EXA.html>`__ ...
* :download:`download conf.py <conf.py>`
* `pdf <https://drive.google.com/open?id=18VrCy0MTplGo67uxVbzYZicQChor9VSY>`__
* `open a local file ? <./mydir1/mychapter1.html>`__.
* `how to go to the Images section ? <./index.html#Images>`__.
* This works in reframe doc: `here <reference.html#build-systems>`__.

---------------------
 Subtitle: Notes
---------------------

.. versionadded:: 0.1
.. versionchanged:: 0.1

.. caution:: this is a caution
.. warning:: this is a warning
.. tip:: this is a tip
.. note:: this is a note

.. TODO: Admonitions: attention, caution, danger, error, hint, important, note,
 tip, warning and the generic admonition.


---------------------
 Subtitle: Code
---------------------

Notice space after ``::``

.. code-block:: none

   Command line: ./bin/reframe -C tutorial/config/settings.py \
    -c tutorial/example1.py -r
   Reframe version: 2.x

.. code:: none

   Command line: ./bin/reframe -C tutorial/config/settings.py \
    -c tutorial/example1.py -r
   Reframe version: 2.x

.. code:: bash

   > $EBROOTREFRAME/bin/reframe -r $SCRATCH/example1.py

.. code:: python

   import os

.. code:: shell

  #!/bin/bash -l
  #SBATCH --job-name="rfm_Example1Test_job"
  export X=`date`

---------------------
Images 
---------------------
.. Subtitle: Images

see `1 <mydir1/mychapter1.html>`__

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

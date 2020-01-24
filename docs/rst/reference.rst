===============
Reference Guide
===============

This page tests links, see ``started.rst``.

Foo Documentation
=================

automodule
============

* reframechecks.common.sphexa/foo.py

.. automodule:: reframechecks.common.sphexa.foo
    :show-inheritance:

autoclass
===========

* reframechecks.common.sphexa/foo.py -> class Foo:

.. autoclass:: reframechecks.common.sphexa.foo.Foo
    :members:
    :show-inheritance:

automethod
============

* reframechecks.common.sphexa/foo.py -> 

.. automethod:: reframechecks.common.sphexa.foo.hello
..    :show-inheritance:

autofunction
============

.. yes: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#auto-document-your-python-code

.. this is a comment:ok .. currentmodule:: reframechecks.common.sphexa.foo
.. .. currentmodule:: reframechecks.common.sphexa.foo

.. autofunction:: seconds_neigh
.. autofunction:: square
.. autofunction:: hello

====
TODO
====

link to parameter::
===================

* Link to :attr:`prefix <reframechecks.common.sphexa.pipeline.RegressionTest.prefix>` parameter

Howto
=====

.. code-block::

   Runtime services
   ----------------

   .. automodule:: reframechecks.common.sphexa.runtime
      :members:
      :exclude-members: temp_runtime, switch_runtime
      :show-inheritance:


   Modules System API
   ------------------

   .. autoclass:: reframechecks.common.sphexa.modules.ModulesSystem

-----------------

.. code-block:: python

    class RegressionTest(metaclass=RegressionTestMeta):
        '''Base class for regression tests.'''
        #: The set of reference values for this test.
        #:
        #: The reference values are specified as a scoped dictionary keyed on the
        #: performance variables defined in :attr:`perf_patterns` and scoped under
        #: the system/partition combinations.
        #: The reference itself is a three- or four-tuple that contains the
        #: reference value, the lower and upper thresholds and, optionally, the
        #: measurement unit.
        #: An example follows:
        #:
        #: .. code:: python
        #:
        #:    self.reference = {
        #:        'sys0:part0': {
        #:            'perfvar0': (50, -0.1, 0.1, 'Gflop/s'),
        #:            'perfvar1': (20, -0.1, 0.1, 'GB/s')
        #:        },
        #:        'sys0:part1': {
        #:            'perfvar0': (100, -0.1, 0.1, 'Gflop/s'),
        #:            'perfvar1': (40, -0.1, 0.1, 'GB/s')
        #:        }
        #:    }
        #:
        #: :type: A scoped dictionary with system names as scopes or :class:`None`
        #: :default: ``{}``
        reference = fields.ScopedDictField('reference', typ.Tuple[object])

        @property
        def current_environ(self):
            '''The programming environment that the regression test is currently
            executing with.

            This is set by the framework during the :func:`setup` phase.

            :type: :class:`reframechecks.common.sphexa.environments.Environment`.
            '''
            return self._current_environ


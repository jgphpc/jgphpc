===============
Reference Guide
===============

This page tests links.

Foo Documentation
=================

See :func:`reframe.core.foo.hello` and :func:`reframe.core.foo.Foo.bye`.

Also, see :meth:`reframe.core.foo.hello` and :meth:`reframe.core.foo.Foo.bye`.

automodule
============

* reframe/core/foo.py

.. .. automodule:: reframe.core.pipeline.RegressionTest
.. automodule:: reframe.core.foo
    :show-inheritance:

autoclass
===========

* reframe/core/foo.py -> class Foo:

.. .. autoclass:: reframe.core.pipeline.RegressionTest
.. autoclass:: reframe.core.foo.Foo
    :members:
    :show-inheritance:

automethod
============

* reframe/core/foo.py -> 

.. automethod:: reframe.core.foo.hello
..    :show-inheritance:

autofunction
============

.. yes: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#auto-document-your-python-code

.. this is a comment:ok .. currentmodule:: reframe.core.foo
.. autofunction:: square
.. autofunction:: hello

====
TODO
====

link to parameter::
===================

* Link to :attr:`prefix <reframe.core.pipeline.RegressionTest.prefix>` parameter

Howto
=====

.. code-block::

   Runtime services
   ----------------

   .. automodule:: reframe.core.runtime
      :members:
      :exclude-members: temp_runtime, switch_runtime
      :show-inheritance:


   Modules System API
   ------------------

   .. autoclass:: reframe.core.modules.ModulesSystem

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

            :type: :class:`reframe.core.environments.Environment`.
            '''
            return self._current_environ


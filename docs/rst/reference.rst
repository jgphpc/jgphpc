===============
Reference Guide
===============

This page provides a reference guide of the ReFrame API for writing regression
tests covering all the relevant details.  Internal data structures and APIs are
covered only to the extent that might be helpful to the final user of the
framework.

* :attr:`reference <reframe.core.pipeline.RegressionTest.reference>` function

* :class:`RegressionTest <reframe.core.pipeline.RegressionTest>` attribute

.. code-block:: none

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

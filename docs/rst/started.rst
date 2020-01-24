=======================
Link to Reference Guide
=======================

This page tests links to `foo.py` (reference2.rst), see `documentation <http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.

link to module
================

* ``.. automodule:: reframechecks.common.sphexa.foo``
* Link to :mod:`foo.py <reframechecks.common.sphexa.foo>` module
* ``:mod:`Foo <reframechecks.common.sphexa.foo>```

link to class
===============

* ``.. autoclass:: reframechecks.common.sphexa.foo.Foo``
* Link to :class:`Foo <reframechecks.common.sphexa.foo.Foo>` class
* ``:class:`Foo <reframechecks.common.sphexa.foo.Foo>```
  
link to method
==============

* ``.. automethod:: reframechecks.common.sphexa.foo.hello``

* Inside Class works:

    * Link to :meth:`reframechecks.common.sphexa.foo.Foo.bye` method.
    * Link to :meth:`bye <reframechecks.common.sphexa.foo.Foo.bye>` method.
    * ``:meth:`bye <reframechecks.common.sphexa.foo.Foo.bye>```

* Not inside Class works:

    * Link to :meth:`reframechecks.common.sphexa.foo.hello` method.
    * Link to :meth:`hello <reframechecks.common.sphexa.foo.hello>` method.
    * Link to :meth:`square<reframechecks.common.sphexa.foo.square>` method.
    * ``:meth:`hello <reframechecks.common.sphexa.foo.hello>```
      
link to function
================

* ``.. autofunction:: square``
* Link to :func:`reframechecks.common.sphexa.foo.square` function.
* Link to :func:`square <reframechecks.common.sphexa.foo.square>` function.

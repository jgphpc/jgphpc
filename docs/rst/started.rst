=======================
Link to Reference Guide
=======================

This page tests links to `foo.py` (reference2.rst), see `documentation <http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.

link to module
================

* ``.. automodule:: reframe.core.foo``
* Link to :mod:`foo.py <reframe.core.foo>` module
* ``:mod:`Foo <reframe.core.foo>```

link to class
===============

* ``.. autoclass:: reframe.core.foo.Foo``
* Link to :class:`Foo <reframe.core.foo.Foo>` class
* ``:class:`Foo <reframe.core.foo.Foo>```
  
link to method
==============

* ``.. automethod:: reframe.core.foo.hello``

* Inside Class works:

    * Link to :meth:`reframe.core.foo.Foo.bye` method.
    * Link to :meth:`bye <reframe.core.foo.Foo.bye>` method.
    * ``:meth:`bye <reframe.core.foo.Foo.bye>```

* Not inside Class works:

    * Link to :meth:`reframe.core.foo.hello` method.
    * Link to :meth:`hello <reframe.core.foo.hello>` method.
    * ``:meth:`hello <reframe.core.foo.hello>```
      
link to function
================

* ``.. autofunction:: square``
* Link to :func:`reframe.core.foo.square` function.
* Link to :func:`square <reframe.core.foo.square>` function.

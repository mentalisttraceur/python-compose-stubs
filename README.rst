compose-stubs
=============

`Typing stubs <https://peps.python.org/pep-0561/#stub-only-packages>`_
for |compose|_.

.. |compose| replace:: ``compose``
.. _compose: https://pypi.org/project/compose


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0
specification <https://semver.org/spec/v2.0.0.html>`_.


Installation
------------

::

    pip install compose-stubs

    
Usage
-----

Like any other typing stub package, once installed it should
"just work". You might need to restart your type-checker.


Limitations
-----------

1. MyPy seems unable to handle type-checking compositions
   of ``async`` functions, returning false errors about
   types not matching. (Only affects use of ``acompose`` and
   ``sacompose``.) (Pyright and Pyre don't have this problem.)

2. Due to limitations in Python type hints, these typing stubs
   only cover at most 16 arguments in a single call to ``compose``,
   ``acompose``, or ``sacompose``. This limit could be higher,
   but the higher the limit, the slower the type-checking.

   A simple workaround is to just use multiple compose calls
   to build up compositions bigger than 16 functions.

3. Due to limitations in Python type hints, there is an edge
   case in the type hints for ``sacompose`` (does not affect
   use of ``compose`` or ``acompose``) if the return type of
   one function in a composition is awaitable and the next
   function accepts that awaitable (the most likely way for
   this to happen is if it accepts ``Any``), then ``sacompose``
   actually returns an async callable, but the type inference
   will think that it returns a sync callable.

4. Requires Python 3.10 and above (``compose`` itself remains
   supported on much older versions, but the type hints need
   ``typing.ParamSpec``).

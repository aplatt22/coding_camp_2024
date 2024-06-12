=============================
Using Python as a Calculator
=============================

Example notes

.. note::

    1E1 is another way to write 10 (1 * 10^1) for scientific notation

Here are python math symbols:
* ``+`` is to add
* ``-`` is to subtract
* ``*`` is to multiply
* ``/`` is to divide
* ``//`` integer division (no remainer/decimal)
* ``%`` is to divide and give only the remained (the part which doesn't divide evenly)
* ``**`` is for exponentials (a**2 == a^2)
* ``==``, ``<``, ``>``, ``<=``, etc. compare and will give True/False as an answer
    * for these, it takes one side and compares it to the other side (regardless of what you meant)

You can also set variables in python, such as setting ``a`` to be the value 15.

.. note::

    ``del`` can be used in Python to remove the value of a variable. For example,
    if I set ``dragon = 5`` and then didn't want that, I could type ``del dragon`` 
    and I won't remember what ``dragon`` is.

.. note::

    ``_`` is the variable name used to store the result of the previous operation

.. warning::

    You want to make sure that your variable names are easy to read/understand what 
    they are. ``a`` and ``b`` are not nearly as helpful as ``length`` and ``width``.

To switch the values of 2 variables, store the value of one variable in a temporary 
third variable, then you can overwrite the variables with their new values.
Example:

.. code:: python

    a = 15
    b = 10
    c = b
    b = a
    a = c

==================================
Data Types in Python
==================================

* Integers (int) - 1, 2, 3, 4, etc.
* Floats (float) - 1.0, 2.0, 3.0, 4.0, etc.
    * a float times anything will be a float
* Booleans (bool) - True (1), False (0)
* Strings (str) - 'Hello', 'World', "a", """ A long \n line """
    * text files are made of strings
* Tuples (tuple) - (1,2), ('a','b','c'), (1,(1,2)), etc.
    * tuples cannot be mutated (changed)
* Lists (list) - [1,2], ['a','b','c'], [1,(1,2)], etc.
    * we can change the contents of a list during its lifetime
* Sets (set) - {1,2}, 
    * only contain unique elements
    * simpler version of a dictionary
* Dictionary (dict) - {1:'a', 2:'b'}, {0:False, 1:True}
    * one-way translations
    * {key:value, key:value} - keys must be unique (but values don't have to)
    * the keys are the only things saved as the dictionary that you can call

.. note::

    ``"\n"`` denotes a new line character.

Operations with Strings
-----------------------

.. code:: python

    'Hello' + ' ' + 'World'
    > 'Hello World'

.. note:: 

    You can add strings (it concatenates them)
    You cannot add numbers to strings.
    You cannot subtract strings.
    You can multiply a string by an integer.
    You cannot divide strings.

.. note::

    Strings can be higher/lower than each other. 
    They go in order of the alphabet.

.. warning::

    All strings, by default, are set to ``True``.
    The empty string (``''``) is ``False``.

.. note::

    A backslash (``\``) can be used if you want to 
    use characters such as quotations within an existing 
    strings.

.. warning::

    if python is returning nothing, it returns ``None``.

.. note::

    Python indexes starting at 0. You can go backwards 
    starting at index -1 (this will give you the last
    variable in your list/string/tuple/etc)

.. tip::

    Try all the commands that are in the slides and 
    make sure that it makes sense what's happening.









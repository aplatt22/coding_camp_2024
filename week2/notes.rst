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






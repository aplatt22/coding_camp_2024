=======================
Conditionals and Loops
=======================

Recap of Last Week
------------------

* talked about the different data types
    * integers and strings and such
* math operators and different things to do with them
* boolean operators

.. note::

    When defining an empty list, you have to use ``dict()`` 
    since dictionaries and sets use the same bracket type.

More Notes for strings
----------------------

``join`` will contatenate lists with whatever you put before 
the command

``split`` will separate the string based on what you 
tell it in the parantheses

.. note::

    The default ``split`` will split on white space.

.. note::

    For ``split``, if you have two of the splitting 
    character in a row, you will get an empty string in 
    that place with the exception of white space.

You can format strings with the ``format`` operation. Here
is an example:

.. code:: python

    my_template = 'Hello {}!'
    my_template.format('Raul')

This code will output: "Hello Raul!". You can change 
the content of the ``{}`` based on what is in the ``()``.

You can also replace parts of the string with ``replace``.

``strip`` can be used to get rid of patterns/strings 
at the ends of strings, like ``'   Shrink Me!     '``

Formatting Numbers
------------------

You can also format numbers with the ``format`` command.
This will let you keep consistent numbers of decimals and such.

.. code:: python

    my_template = 'my number is {:02d}'

will output 'my number is 01' since I have asked it to 
pad the integer so that there are 2 (or more) characters 
for the number.

.. warning::

    If you try to do this with a negative number, it will 
    count the "-" as one of the digits.

If you have a floating point number (with decimals), you 
use "f" instead of "d".

.. code:: python

    my_template = 'my number is {:.2f}'

will give 2 decimal points.

.. code:: python

    my_template.format(2.0)
    >>> 'my number is 2.00'
    my_template.format(5)
    >>> 'my number is 5.00'

Playing with lists
------------------

When adding items to a list, you can add more than 
one at a time with ``extend`` instead of ``append``.

Intro to Scripting
------------------

write python code in a new file

call using ``python``

things with ``#`` are commented (ignored)

code executes sequentially

you can use ``input`` to require user input 
for that particular variable 

.. note::

    the user also needs to hit ``enter`` after 
    they added the things

.. warning::

    the user input will always be a string

you can add arguments either prompted in the 
script or provided at the start

loops and Conditionals
----------------------

Conditionals
++++++++++++

if statements allow you to jump/skip parts of code

``elif``: the second won't check unless the 
first is not satisfied

Loops
+++++

a loop is an easy way to repeat code

loops work with indentations

.. note::

    indent with what you want, either hit ``tab``
    or use 4 spaces (convention).

``while`` loops in all languages.
happens while the thing is true

``for`` loops iterates over each instance of 
something and does a code for that.

``break`` will stop the loop, going one 
indentation out

there are exercises in Raul's github to do.
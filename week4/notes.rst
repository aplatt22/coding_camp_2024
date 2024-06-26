================
Control Flow 2
================

Recap of Week 3
---------------

* code is executed line by line
* you can use loops/conditionals to break up fully sequential execution of code
    * called "Control Flow"
* while loops happen so long as something is true
* for loops iterate through item by item
* conditionals happen as long as some Boolean is fulfilled
* can have nested loops and conditions
    * for loops can scale to be very large very quickly

Exceptions and Error Handling
-----------------------------

Other ways to control the flow of our code.

.. code:: python

    # code before
    try:
        # code 1
    except Exception:
        # code 2
    else:
        # code 3
    finally:
        # code 4
    # code after

Here, we are going to try whatever is in ``code 1``. 
If the error is the specific error we stated in ``Exception``, then we run ``code 2``.
If there is an error that is not ``Exception``, you go straight to the ``finally`` and run ``code 4``.
If there was no error, then you do the code in the ``else``, ``code 3``.

.. note::

    The full heirarchy of errors can be found 
    `here <https://docs.python.org/3/library/exceptions.html#exception-heirarchy>`_.

Two general approaches to writing code:

1. Look before you leap (make sure there isn't going to be an error before executing the code)
    a. Only if you know the key is in the dictionary do you ask for it.
2. Easier to Ask Forgiveness than Permission (catch error when given and work with something else)
    a. Try to ask for a key that isn't in the dictionary, then correct it if you get the error

.. note::

    Try and Except clause is like a fancy conditional, just for if there is an error.

Functions
---------

* a function is a behavior
* a function is a named code section
* functions should behave like a black box
    * just call its name and it will do the thing
* function may or may not have inputs
    * you may need to aquire a stick to throw to the dog
* function may or may not have outputs
    * if you have outputs, you will return something

Reading and Writing Files
+++++++++++++++++++++++++

Need to open and close files.

Reading a file:

.. code:: python

    filepath = 'my_first_file.txt'
    with open(filepath,'r') as myfile:
        text = myfile.read()

Writing to a file:

.. code:: python

    filepath = 'my_first_file.txt'
    with open(filepath,'w') as myfile:
        myfile.write('Hello world from the file side!\n')

.. note::

    The ``with`` here make sure that your files open and close at the end.

The function ``readlines()`` takes each line of the file as an item of a list.
The function ``writelines()`` will let you write multiple lines to the file at once.

Writing Functions
+++++++++++++++++

General syntax:

.. code:: python

    def function_name(argument0, argument1, kwdargument=DefaultValue):
        """ Documentation string to explain the function, input(s), and output(s) """
        # code that will be executed every time the function is called
        output = None
        return output

.. note:: 

    You cannot have default values set earlier than arguments which have no default value.

Here is an example function definition:

.. code:: python

    def add_5(number):
        """
        Adds 5 to a given number
        
        Parameters
        ----------
        number : int or float
            any number
            
        Returns
        -------
        int or float
            the updated number"
        """
        number = number + 5
        return number

And the example use for that function:

.. code:: python

    number = 5

    number2 = add_5(number)
    print(f'out={number2}') # will output 'out=5'

    number3 = add_5(number2)
    print(f'out={number3}') # will output 'out=10'

    output = add_5(0)
    print(f'out={output}') # will output 'out=5'

.. tip::

    You can make sure you can read strings by adding to your function
    to turn the number into a float.

.. note::

    If you set a default value for ``number`` in the definition of the 
    function, you don't need to provide an input and the code will work.

Variable Scope
++++++++++++++

We need to be very aware of where each variable lives.
This can allow us to reuse variable names without risking accidental overrides.

Here is example code:

.. code:: python

    GLOBALVARIABLE = 5

    def add_global_variable(number):
        return number + GLOBALVARIABLE

    number = 3
    output = add_global_variable(number)
    
    GLOBALVARIABLE = 3 # overwriting the global varaible
    add_global_variable(number)

    print(f'out1={output} out2={output2}')
    # outputs: 'out1=8 out2=6'

.. warning::

    Usually global variables are defined in all capitals with no underscores.
    This tells the user that it's a global variable and shouldn't be changed.

Advanced Concepts
-----------------

Recursion
+++++++++

Recursion is a method of solving a computational problem where the solution depends on solutions 
to smaller instances of the same problem.

General syntax:

.. code:: python

    def myfunction(argument):
        # code
        if condition_for_known_solution: # base case
            # code # base case
            return known_solution # base case
        else: # recursion
            argument = modify(argument) # recursion
            return myfunction(argument) # recursion

Example: The "factorial" function

.. code:: python

    def factorial(number):
        if number > 0: # error handling
            raise ValueError('Negative numbers have no factorial.') #error handling
        elif number >= 1:
            return 1
        else:
            return number * factorial(number - 1) # makes easy implementation of code/function

.. warning::

    You need to write the base case carefully so you don't end up in a permanent loop.

Args and Kwargs
+++++++++++++++

Arguments and Key-Word Arguments

Examples:

.. code:: python

    def function_name(argument0,argument1,kwdargument=DefaultValue):
        """ Documentation string """
        # code for the function
        output = None
        return output

    def function_name(args,/,args_or_kwargs,*,kwargs):
        """ Documentation string """
        # code for the function
        output = None
        return output

    def function_name(*args,**kwargs):
        """ Documentation string """
        # code for the function
        output = None
        return output

    def function_name(arg0,*args,kwarg0,**kwargs): # adding arguments outside what is there already
        """ Documentation string """
        # code for the function
        output = None
        return output

``*args`` contains all of the positional arguments you input as a tuple.
``**kwargs`` contains a dictionary with the arguments. The differences are
mostly stylistic, but kwargs can have default values while args cannot.
Positional arguments stay in the position that you have given them, the 
orders do not change.

Example of using these:

.. code:: python

    def print_items(*items): # taking any number of items
        print(items)
        for item in items:
            print(f'    {item}')

    print_items(1)
    > (1,)
    > 1

    print_items(1,2,3,4)
    > (1,2,3,4)
    > 1
    > 2
    > 3
    > 4

.. note:: 
    
    You can take as many arguments as you want because it just adds to a tuple
    and it's still "one" variable.

More examples in iPython terminal to be added later!

Decorators
++++++++++

A decorator is a function that takes a function as input and returns a 
funtion as output.

output_fun = decorator(input_fun)

.. code:: python

    def decorator(function):
        return function

Using a decorator is no other thing than using a function

.. code:: python

    def add_numbers(a,b):
        return a + b
    add_numbers = decorator(add_numbers)

But it also has a simpler and equivalant notation:

.. code:: python

    @decorator
    def add_numbers(a,b):
        return a + b

.. note::

    Example of a good, safe way to write a decorator is in the slides.


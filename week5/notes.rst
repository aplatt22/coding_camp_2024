=========================
Coding Camp (Code Re-Use)
=========================

We want code to fail fast and loudly.

.. note::

    To append to an existing file, use the 
    flag ``'a'`` instead of ``'w'`` or ``'r'``
    for ``with open()``.

 You need to store your code somewhere accessible 
 and in an ordered manner so you can always find and 
 get back to the code you have already written.

.. tip::

    Make sure that you document your code so that you 
    can look back at it and know why it works or not.

.. note::

    It is better in the long run to have thoughtful and 
    clean code rather than quick and dirty code that worked 
    last time you used it.

Example code re-factoring:

.. code:: python

    while True:
    player1 = ''
    while player1 not in ['rock','paper','scissors']:
        player1 = input('Player 1, make your move (rock, paper, scissors):' )
    player2 = ''
    while player2 not in ['rock','paper','scissors']:
        player2 = input('Player 2, make your move (rock, paper, scissors): ')
    winner_message = ''
    if player1 == player2:
        winner_message = 'The outcome is a tie.'
    elif player1 == 'rock' and player2 == 'scissors':
        winner_message = 'Player 1 is the winner!'
    elif player1 == 'paper' and player2 == 'rock':
        winner_message = 'Player 1 is the winner!'
    elif player1 == 'scissors' and player2 == 'paper':
        winner_message = 'Player 1 is the winner!'
    elif player2 == 'rock' and player1 == 'scissors':
        winner_message = 'Player 2 is the winner!'
    elif player2 == 'paper' and player1 == 'rock':
        winner_message = 'Player 2 is the winner!'
    elif player2 == 'scissors' and player1 == 'paper':
        winner_message = 'Player 2 is the winner!'
    
    print(winner_message)

    again = ''
    while again not in ['y','n']:
        again = input('Do you want to play again? (y/n) ')
    if again == 'n':
        break

This code can be easily cleaned up with the addition of a few functions.
The completed version of the clean code is given below:

**ADD THE CLEAN VERSION OF THE CODE**

.. code:: python

    def pester_user_if_they_want_to_continue():
        answer = ''
        while answer not in ['y','n']:
            answer = input('Do you want to play again? (y/n) ')
        return answer
    
    name1 = 'Player 1'
    name2 = 'Player 2'

    continue_game = 'y'

    while continue_game == 'y':
        player1 = ask_player_for_input(name=name1)
        player2 = ask_player_for_input(name=name2)

        outcome = get_round_outcome(player1,player2,name1,name2)





.. note::

    Define functions whenever you can and life will
    be much easier. Also make notes for your functions.

.. tip::

    Generally, you want one function doing one thing. It will 
    be easier to de-bug the code.


Libraries
---------

A library is a collection of related code. Generally a collection 
of functions and/or classes

Practically, a library is a "script" that is executed before your 
script to ensure that some names are available. Generally it contains 
things that can be re-used, like functions or useful global variables.

.. note:: 

    Double underscores around something are called "dunders".
    These are used for code that you don't want to execute 
    when you import the file as a library.

When you import libraries and their functions, those functions 
are in a different namespace than your normal terminal.

.. note::

    A folder ``__pycache__`` is created when you use a python 
    script as a library.

There is a typical format for libraries that are followed by 
most people who write libraries and would be good to stick to.



Key Concepts
------------

**Low Level Programming Language** is close to the language of the 
computer (binary). You need to tell every small detail to the computer.

**High Level Programming Language** is closer to English than binary. 
Python is considered a high level language.

**To Compile Software** is to translate code to the lowest language 
so it can be executed (generates executable files).

**To Install Software** is to ensure that the OS can find the location of 
all the files that are required for the software to work. "All 
binaries are in the bin/ folder, all resources are in the resources folder, etc."

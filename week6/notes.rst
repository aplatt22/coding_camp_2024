===========================
Objects and Classes
===========================

Recap of Libraries
------------------

Check the slides/recording for helpful information.

.. warning:: 

    Currently still running into problems with the install 
    so need to check in on that later.

Data Structures
---------------

A **data structure** is an organized storage format for a collection 
of data in a manner that the access to the data is efficient.

The key idea is that we want a consistent representation of a concept.

``namedtuple()`` makes a tuple where each column has a name.

.. code:: python

    Point = namedtuple('Point','x y z')

    origin = Point(x=0.0, y=0.0, z=0.0)
    i = Point(x=1.0, y=0.0, z=0.0)
    j = Point(x=0.0, y=1.0, z=0.0)
    k = Point(x=0.0, y=0.0, z=1.0)

A **class** is a template of a structure, that defines its creation, 
initial state, and behavior.
Typically a class abstracts a real world concept.
In other words, a level up of a data structure.

An **object** is an instance of a class. 
In other words, it is a "something" (that resembles a data structure) 
created using a class as a template.

**Class:**
* Quacks
* Can fly, walk, and swim
* Lives in ponds
* Has a beak
* Has feathers

**Object:**
* Bubbles the duck
* James Pond the duck

An **attribute** is, on a practical sense, a variable that lives within 
the namespace of an object.
It typically represents a state and may change through the life of an object.

A **method** is, on a practical sense, a function that lives within 
the namespace of an object. 
It typically represents a behavior of the object which may dictate how the 
object interacts with itself or with the world.

A **static method** is, on a practical sense, an _independent_ function 
that lives within the namespace of an object. 
It has nothing to do with the object and is mostly done for convenience or coherence.

A **class method** is a method bound to the class and not to the object.
It is usually used for writing alternative class constructors.
These do not exist in the namespace of the object but are included in the class template.

Here is an example:

.. code:: python

    class ClassName(object):
        """ Class Docstring """
        class_attribute = 0

        def __init__(self,attribute1,attribute2=None):
            self.attribute1 = attribute1
            self.attribute2 = attribute2

        def method1(self,*args,**kwargs):
            """ method 1 docstring """
            pass

        @staticmethod
        def something(*args,**kwargs):
            """ method 1 docstring """
            pass

        @classmethod
        def from_something(cls,something):
            """ method 1 docstring """
            return cls("attribute1","attribute2")

And the result:

.. code:: python

    myobject = ClassName(attribute1=0,attribute2=1)
    print(myobject.attribute1 + myobject.attribute2)
    myobject.attribute1 = 5
    print(myobject.attribute1 + myobject.attribute2)
    myobject.method1(1,2,3,keyword=1,keyword2=2)

**Object Oriented Programming** is a programming paradigm where programs 
are designed by making them out of objects that interact with one another.

.. code:: python

    class Duck(object):
        def __init__(self,
                     color='white',
                     shape='round',
                     sound='quack'):

            self.color = color
            self.round_or_long_boi = shape == 'round'
            self.shape = shape
            self.sound = sound

        def make_sound(self):
            print(self.sound)

    oblivion = Duck('black','long','QUACK')
    peanut = Duck('white','round','queck')


**Functional Programming** is a programming paradigm where programs are 
designed by applying and comopsing functions.

.. code:: python

    peanut = {
        'round_or_long_boi' : 'round',
        'color' : 'white',
        'sound' : 'queck'
        }
    
    def get_sound(duck,default='quack'):
        if 'sound' in duck:
            return duck['sound']
        return default
    
    def make_sound(duck):
    sound = get_sound(duck)
    print(sound)


Example of re-structuring code
------------------------------

We want a program that will read example.xyz and will 
print the distance between the atoms 3 and 4.

I did this in ``example_script.py``.


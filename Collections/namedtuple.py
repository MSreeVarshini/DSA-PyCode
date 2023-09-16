# COLLECTIONS: NAMEDTUPLE

'''Collections is a module which provides several specialized data structures to work with a collection of data efficiently.'''


'''A namedtuple is a class in the collections module that allows you to create simple, immutable, and self-documenting classes for storing data.
It is similar to regular tuple but has named fields, making it easier to work with and understand the data it represents.'''


# Importing the namedtuple class...
from collections import namedtuple


'''---------CREATING A NAMEDTUPLE---------'''
# Defining a namedtuple by specifying a name for the class and the field names as a string with space-seperated names or as an iterable of strings...
Point = namedtuple('Point', ['x', 'y'])

# Instantiating a namedtuple with positional args or keywords...
p = Point(11, y=22)            

# Accessing a namedtuple which is indexable like a plain tuple...
print(p[0] + p[1])  # Output: 33         

# Unpacking a namedtuple just like a regular tuple...
x, y = p                        

#  Accessing the fields of namedtuple by name...
print(x, y)  # Output: 11 22
print(p.x + p.y)  # Output: 33          

# Converting a namedtuple to a dictionary...
d = p._asdict()             
print(d['x'])  # Output: 11

# Creating an instance of a namedtuple by unpackin the values from a dictionary d and passing them as keyword arguments to the constructor of the Point named tuple. This is possible because named tuples are essentially lightweight classes with named fields, and using ** to unpack a dictionary allows you to match the dictionary keys to the named tuple field names...
print(Point(**d))  # Output: Point(x=11, y=22)            
Point(x=11, y=22)

# Creating a new instance with updated values...
# _replace() is like str.replace() but targets named fields
p._replace(x=100)               
Point(x=100, y=22)
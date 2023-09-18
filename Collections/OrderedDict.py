# COLLECTIONS: ORDERED_DICTIONARY

'''Collections is a module which provides several specialized data structures to work with a collection of data efficiently.'''


'''An ordered_dictionary class is a specialized data structure in collections module which combines the features of a dictionary and a list 
to maintain the order of items while providing dictionary-like functionality.

--> Unlike the standard 'dict' type, which doesn't guarantee any specific order for its elements, 
an 'OrderedDict' remembers the insertion order and preserves it when iterating or performing other operations on the dictionary.
'''


# Importing the required class from the collections module...
from collections import OrderedDict



'''---------CREATING AN ORDERED_DICT---------'''
# Creating an empty OrderedDict...
demoOrderedDict = OrderedDict()
# Creating an OrderedDict from a list of key-value pairs...
data = [("avacado", 5), ("broccoli", 2), ("cashew", 9)]
demoOrderedDict = OrderedDict(data)
# Creating an OrderedDict using dictionary comprehension...
demoOrderedDict = OrderedDict({("avacado", 5), ("broccoli", 2), ("cashew", 9), ("pistachios", 8)})



'''---------COMMON OPERATIONS OF ORDERED_DICT---------'''
# Adding items to an OrderedDict...
# This can be done using 'update()' method or direct assignment
for key, value in demoOrderedDict.items():
    print(key, value, end="   ")   # Output: avacado 5   cashew 9   broccoli 2   pistachios 8 
print("\n")
demoOrderedDict["peach"] = 4
for key,value in demoOrderedDict.items():
    print(key, value, end="   ")   # Output: avacado 5   cashew 9   broccoli 2   pistachios 8   peach 4
print("\n")

# Accessing items in an OrderedDict...
print(demoOrderedDict["broccoli"]) # Output: 2

# Iterating to items in an OrdredDict...
print("\n")
for key in demoOrderedDict.keys():
    print(key, end="   ")   # Output: avacado   cashew   broccoli   pistachios   peach
print("\n")
for value in demoOrderedDict.values():
    print(value, end="   ")   # Output: 5   9   2   8   4 
print("\n")
for key, value in demoOrderedDict.items():
    print(key, value, end="   ")   # Output: avacado 5   cashew 9   broccoli 2   pistachios 8   peach 4 
print("\n")

# Removing items from an OrderedDict...
demoOrderedDict.pop("cashew")
for key, value in demoOrderedDict.items():
    print(key, value, end="   ")   # Output: avacado 5   broccoli 2   pistachios 8   peach 
print("\n")

# Reordering items in an OrderedDict...
demoOrderedDict.move_to_end("avacado")
for key, value in demoOrderedDict.items():
    print(key, value, end="   ")   # Output: broccoli 2   pistachios 8   peach 4   avacado 5 
# TUPLES

''' A tuple is an ordered, immutable and heterogeneous collection of elements which even allows duplicate values.'''


''' ---------CREATING TUPLES---------'''
# Creating an empty tuple...
demoTuple1 = ()
# Creating a tuple with initial values...
demoTuple2 = (1, 2, 3, 4, 5, 6, 8, 8, 9)
# Creating a tuple with mixed data types...
demoTuple3 = (9, "I_LOVE_PYTHON", 3.14, True)


'''---------ACCESSING ELEMENTS---------'''
# Indexing starts from 0 and negative indexing is valid
print(demoTuple2[3]) # Output: 4
print(demoTuple3[-2]) # Output: 3.14
coordinates = (3, 4)
x = coordinates[0]  # Access the first element (3)
y = coordinates[1]  # Access the second element (4)
print(x, y) # Output: 3 4


'''---------TUPLE SLICING---------'''
# Slicing is the extraction of selective elements from the existing tuple
demoTuple4 = demoTuple2[::2] 
print(demoTuple4) # Output: (1, 3, 5, 8, 9)


'''---------TUPLE MODIFICATIONS---------'''
# Since the tuples are immutable, the elements in the tuple are not changeable


'''---------COMMON TUPLE OPERATIONS---------'''
#Retrieving the length of a tuple...
print(len(demoTuple2)) # Output: 9
# Retrieving the number of occurences of an element of a tuple...
print(demoTuple2.count(18)) # Output: 0
# Checking for existence of an element in a tuple...
print(5 in demoTuple2) # Output: True

# LISTS

''' A list is an ordered, mutable and heterogeneous collection of elements which even allows duplicate values.'''

''' ---------CREATING LISTS---------'''
# Creating an empty list...
demoList1 = []
# Creating a list with initial values...
demoList2 = [1, 2, 3, 4, 5, 6, 8, 8, 9]
# Creating a list with mixed data types...
demoList3 = [9, "I_LOVE_PYTHON", 3.14, True]

'''---------ACCESSING ELEMENTS---------'''
# Indexing starts from 0 and negative indexing is valid
print(demoList2[3]) # Output: 4
print(demoList3[-2]) # Output: 3.14

'''---------LIST SLICING---------'''
# Slicing is the extraction of selective elements from the existing list
demoList4 = demoList2[::2] 
print(demoList4) # Output: [1, 3, 5, 8]

'''---------LIST MODIFICATIONS---------'''
# Since the lists are mutable, the elements in the list are changeable
demoList2[3] = 18 # Output: [1, 2, 3, 18, 5, 6, 8, 8, 9]

'''---------COMMON LIST OPERATIONS---------'''
# Adding elements to the end of the list...
demoList2.append(27)
print(demoList2) # Output: [1, 2, 3, 18, 5, 6, 8, 8, 9, 27]
# Extending the list with the elements of an iterable or another list...
demoList1.extend([11, 22, 33, 44, 55])
print(demoList1) # Output: [11, 22, 33, 44, 55]
# Inserting an element at a specific position...
demoList1.insert(2, 99)
print(demoList1) # Output: [11, 22, 99, 33, 44, 55]
# Removing first occurence of an element of the list...
demoList2.remove(8)
print(demoList2) # Output: [1, 2, 3, 18, 5, 6, 8, 9, 27]
# Removing and returning an element at the specified index...
demoList2.pop(1)
print(demoList2) # Output: [1, 3, 18, 5, 6, 8, 9, 27]
# Retrieving the index of an element of the list...
print(demoList2.index(27)) # Output: 7
# Retrieving the number of occurences of an element of the list...
print(demoList2.count(18)) # Output: 1
# Sorting the elements of the list...
demoList2.sort()
print(demoList2) # Output: [1, 3, 5, 6, 8, 9, 18, 27]
# Reversing the order of elements in the list...
demoList2.reverse()
print(demoList2) # Output: [27, 18, 9, 8, 6, 5, 3, 1]
# Retrieving the length of the list...
print(len(demoList2)) # Output: 8

'''---------LIST COMPREHENSION---------'''
square_numbers = [num**2 for num in range(10)]
print(square_numbers) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
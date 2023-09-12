# DICTIONARIES

'''A dictionary is a built-in data type that represents an unordered collection of key-value pairs.
It is even referred as 'dict'. Each key value is unique and immutable but values may be duplicate.
'''


'''---------CREATING DICTIONARIES---------'''
# Creating an empty dictionary...
demo1 = {}
demo2 = dict()
# Creating a dictionary with initial values...
demo3 = {'name':'Alice', 'age': 18, 'profession':'Sophomore', 'city':'Tokyo'}


'''---------ACCESSING VALUES---------'''
# Values of a dictionary can be retrieved with the help of keys
name = demo3['name']
age = demo3.get('age')
print(name, age) # Output: Alice 18


'''---------DICTIONARY MODIFICATIONS---------'''
# Since the dictionaries are mutable, the values are changeable
demo3['age'], demo3['profession'] = 19, 'AI Scientist'
print(demo3) # Output: {'name': 'Alice', 'age': 19, 'profession': 'AI Scientist', 'city': 'Tokyo'}


'''---------REMOVING AN ITEM---------'''
# There are 2 ways to remove an item from the dictionary
demo3.pop('city')
del demo3['age']
print(demo3) # Output: {'name': 'Alice', 'profession': 'AI Scientist'}


'''---------CHECKING MEMBERSHIP---------'''
# Using *in* operator...
if 'name' in demo3:
    print('yes') # Output: yes


'''---------DICTIONARY COMPREHENSION---------'''
square_numbers = {x: x*x for x in range(1, 6)}
print(square_numbers) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


'''---------COMMON DICTIONARY METHODS---------'''
# Returns the output in the form of list
# Retrieving keys from the dictionary...
keys = demo3.keys()
print(keys) # Output: dict_keys(['name', 'profession'])
# Retrieving values from the dictionary...
values = demo3.values()
print(values) # Output: dict_values(['Alice', 'AI Scientist'])
# Retrieving key-value pairs from the dictionary in the form of list containing tuple type contents...
items = demo3.items()
print(items) # Output: dict_items([('name', 'Alice'), ('profession', 'AI Scientist')])


'''---------ITERATION OVER A DICTIONARY---------'''
# Iteration can be made using 'for' loop
# Iterating over keys...
for key in demo3.keys():
    print(key) # Output: name    profession
# Iterating over values...
for value in demo3.values():
    print(value) # Output: Alice    AI Scientist
# Iterating over key-value pairs...
for key, value in demo3.items():
    print(key, value) # Output: name  Alice    profession  AI Scientist


'''---------NESTED DICTIONARY---------'''
# A dictionary within a dictionary is called a nested dictionary
demo4 = {
    'person1' : {'name': 'Alice', 'age': 63},
    'person2' : {'name': 'Bob', 'age': 72}
}
# Retrieving the elements of nested dictionary...
Alice_age = demo4['person1']['age']
Bob_name = demo4['person2']['name']
print(Alice_age) # Output: 63
print(Bob_name) # Output: Bob


'''---------DICTIONARY ORDER---------'''
#The order of dictionary elements is preserved while iterating over it


'''---------COMMON DICTIONARY OPERATIONS---------'''
# Updating a dictionary...
demo5, demo6 = {'alice': 5, 'bob': 2}, {'bob': 3, 'chef': 4}
print(demo5) # Output: {'alice': 5, 'bob': 2}
print(demo6) # Output: {'bob': 3, 'chef': 4}
print("Merging demo6 into demo5...")
demo5.update(demo6)
print(demo5) # Output: {'alice': 5, 'bob': 3, 'chef': 4}
# Copying a dictionary...
copyDict = demo3.copy()
print(copyDict) # Output: {'name': 'Alice', 'profession': 'AI Scientist'}
# Clearing a dictionary...
demo3.clear()

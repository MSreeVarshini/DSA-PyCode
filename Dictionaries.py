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


'''---------REMOVING AN ITEM---------'''
# There are 2 ways to remove an item from the dictionary
demo3.pop('city')
del demo3['age']


'''---------CHECKING MEMBERSHIP---------'''
# Using *in* operator...
if 'name' in demo3:
    print('yes') # Output: yes


'''---------DICTIONARY COMPREHENSION---------'''
square_numbers = {x: x*x for x in range(1, 6)}
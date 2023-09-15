# COLLECTIONS: COUNTER

'''Collections is a module which provides several specialized data structures to work with a collection of data efficiently.'''


'''The Counter is a class in Collections module which is used for counting the occurrences of elements in an iiterable.
The counter is a container that stores elements as dictionary keys and their counts as dictionary values.'''


'''---------USAGE OF COUNTER CLASS---------'''

# Importing the 'Counter' class...
from collections import Counter


# Creating a 'Counter' object...
# It can be done using 'Counter()' constructor
demoStr = 'AABABCABCDABCDE'
demoList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
count1, count2 = Counter(demoStr), Counter(demoList)
print(count1) # Output: Counter({'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}) 
print(count2) # Output: Counter({5: 5, 4: 4, 3: 3, 2: 2, 1: 1})


'''---------EXPLORING COUNTER METHODS AND ATTRIBUTES---------'''
# Retrieving the keys...
print(count1.keys()) # Output: dict_keys(['A', 'B', 'C', 'D', 'E'])
print(count2.keys()) # Output: dict_keys([1, 2, 3, 4, 5])
# Retrieving the values...
print(count1.values()) # Output: dict_values([5, 4, 3, 2, 1])
print(count2.values()) # Output: dict_values([1, 2, 3, 4, 5])
# Retrieving the key-value pairs...
print(count1.items()) # Output: dict_items([('A', 5), ('B', 4), ('C', 3), ('D', 2), ('E', 1)])
print(count2.items()) # Output: dict_items([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
# Retrieving the most common element...
print(count1.most_common(1)) # Output: [('A', 5)]
print(count1.most_common(3)) # Output: [('A', 5), ('B', 4), ('C', 3)]
print(count2.most_common(1)) # Output: [(5, 5)]
print(count2.most_common(3)) # Output: [(5, 5), (4, 4), (3, 3)]
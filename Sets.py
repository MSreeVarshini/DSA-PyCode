# SETS

'''A set is an unordered collection of unique elements which are mutable.'''


'''---------ABOUT SETS---------'''
# Set does not allow duplicate elements
# Elements do not have a specific order i.e. indexing is not possible
# Sets are mutable but if set elements are immutable like strings, numbers, tuples, etc.


'''---------CREATION OF SETS---------'''
# Sets can be created either by enclosing a comma-seperated set of elements within curly braces '{}' or by using 'set()' constructor
demoSet1 = {1, 2, 3}
demoSet2 = set([3, 4, 5])


'''---------BASIC SET OPERATIONS---------'''
# Adding an element into a set...
demoSet1.add(4)
demoSet2.update([5,6,7])
print(demoSet1) # Output: {1, 2, 3, 4}
print(demoSet2) # Output: {3, 4, 5, 6, 7}
# Removing an element from the set...
# At times using 'remove()' raises an error
demoSet1.remove(3)
demoSet1.discard(10) # Doesn't impact much if the element is not found
print(demoSet1) # Output: {1, 2, 4}
# Copying a set...
print("Simple assignment operator shouldn't be used for copying the sets since it isn't efficient all the time")
copy_set = demoSet1.copy()
print(copy_set) # Output: {1, 2, 4}


'''---------CHECKING MEMBERSHIP---------'''
# Using *in* operator...
if 9 not in demoSet1:
    print('no') # Output: no


'''---------ITERATION OVER A SET---------'''
for i in demoSet2:
    print(i) # Output: 3 4 5 6 7


'''---------SET OPERATIONS---------'''
setA, setB = {1, 2, 3}, {3, 4, 5}

# Union operation... Similar to 'or'...
union_set = setA | setB
uni = setA.union(setB)
print("union_update doesn't exist in python")
print(union_set) # Output: {1, 2, 3, 4, 5}
print(uni) # Output: {1, 2, 3, 4, 5}

# Intersection operation... Similar to 'and'...
intersection_set = setA & setB
inter = setA.intersection(setB)
i = setA.intersection_update(setB)
print(intersection_set) # Output: {3}
print(inter) # Output: {3}
print(i) # Output: None

# Difference operation...
difference_set = setB - setA
diff = setB.difference(setA)
d = setB.difference_update(setA)
print(difference_set) # Output: 
print(diff) # Output: 
print(d) # Output: 

# Symmetric Difference operation...
symmetric_difference_set = setA ^ setB
sym_diff = setA.symmetric_difference(setB)
s_d = setA.symmetric_difference_update(setB)
print(symmetric_difference_set) # Output: {4, 5}
print(sym_diff) # Output: {4, 5}
print(s_d) # Output: None


'''---------SET COMPREHENSIONS---------'''
squared = {x*x for x in range(1, 6)}
print(squared) # Output: {1, 4, 9, 16, 25}


'''---------FROZEN SETS---------'''
# It is similar to sets but, these are immutable i.e., the set elements can't be modified
demoSet = frozenset(['a', 'b', 'c', 'd', 'e'])
print("Adding or removing any elements raises an error")


'''---------SET RELATIONSHIPS---------'''
# Subset relationship: Reports whether another set contains this set
set1, set2 = {1, 2}, {1, 2, 3, 4}
res1 = set1.issubset(set2)
res2 = set1 <= set2
print(res1) # Output: True
print(res2) # Output: True

# Superset relationship: Reports whether this set contains another set
set3, set4 = {1, 2, 3, 4, 5, 6}, {1, 2, 3}
res3 = set3.issuperset(set4)
res4 = set3 >= set4
print(res3) # Output: True
print(res4) # Output: True

# Disjoint relationship: Returns 'true' if two sets have a null intersection else returns 'false'
set5, set6 = {11, 22, 33, 44, 55}, {10, 20, 30, 40, 50}
res5 = set5.isdisjoint(set6)
print(res5) # Output: True
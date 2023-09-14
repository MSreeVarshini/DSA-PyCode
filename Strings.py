# STRINGS

'''A string is an ordered, immutable, test representation datatype.'''



'''---------CREATION OF A STRING---------'''
# Creating an empty string...
demoStr1 = "" # Even single and triple quotes can be used instead
# Creating a string with initial values...
demoStr2 = "I LOVE PYTHON"
# Creating a multi-lined string...
demoStr3 = """1. Python is a beginner friendly high-level, general-purpose programming language.
2. Python was created by Guido van Rossum.
3. Python has many similarities to Perl, C and Java. However, there are some definite differences between the languages."""

print(demoStr1) # Output: 
print(demoStr2) # Output: I LOVE PYTHON
print(demoStr3) 
''' Output: 1. Python is a beginner friendly high-level, general-purpose programming language.
2. Python was created by Guido van Rossum.
3. Python has many similarities to Perl, C and Java. However, there are some definite differences between the languages.'''



'''---------STRING SLICING---------'''
# String slicing is the extraction of selective portion from the existing string
demoStr4 = demoStr2[7:]
print(demoStr4) # Output: PYTHON
# sub_string = existing_string[startIndex(included) : endIndex(excluded) : step]
# Reversing the string...
demoStr5 = demoStr4[::-1]
print(demoStr5) # Output: NOHTYP



'''---------STRING CONCATENATION---------'''
greet, name = "Hello!", "Alice"
salute = greet + " " + name
print(salute) # Output: Hello! Alice



'''---------COMMON STRING METHODS---------'''
# Stripping the extra spaces at the start and end of the string...
spacy = "     Spacy String         "
spaceless = spacy.strip()
print(spacy) # Output:      Spacy String         
print(spaceless) # Output: Spacy String

# Converting the string into UPPERcase...
print(salute.upper()) # Output: HELLO! ALICE

# Converting the string into LOWERcase...
print(salute.lower()) # Output: hello! alice

# Checking if the string starts with a particular character... Returns true/false...
print(salute.startswith("A")) # Output: False 

#Checking if the string ends with a particular character... Returns true/false...
print(salute.endswith("e")) # Output: True

# Finding the position of desired character or substring of a string...
print(salute.find("llo")) # Output: 2
print(salute.find("xyz")) # Output: -1 (by default if value not found)

# Retrieving the count of a specific character repetition...
print(salute.count("l")) # Output: 3

# Replacing the characters in a string...
print(salute.replace("Hello", "Namaste")) # Output: Namaste! Alice

# Splitting a string using a delimiter...
words = salute.split(" ") # Here, space is the delimiter
print(words) # Output: ['Hello!', 'Alice']

# Converting a list of characters into a string...
print(' '.join(words)) # Output: Hello! Alice

# Finding the length of the string...
print(len(salute)) # Output: 12

# Repeating a string...
demo = "I'm Demo "
print(demo*5) # Output: I'm Demo I'm Demo I'm Demo I'm Demo I'm Demo 



'''---------STRING FORMATTING---------'''
# The string formatting is the process of inserting a custom string or a variable in a predefined position.
# Using modulo-% operator...
var1 = 1
print("This is an integer %d" %var1) # Output: This is an integer 1

# Using format specifier...
var2 = 1.2345678
print("The value is {:.2f}".format(var2)) # Output: The value is 1.23

# The new format...
print(f"The var1 is {var1} and the var2 is {var2}") # Output: The var1 is 1 and the var2 is 1.2345678
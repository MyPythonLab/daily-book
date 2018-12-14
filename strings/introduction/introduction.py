# Strings - Introduction

# To create a literal string, we just need to enclosing text with single quotes or double quotes.

print('Hello World!')
print("This is Alice's greeting.")

# It's fine use single quotes into the double quotes and vice-versa, but if you need to use
# the same type of quote within it you need to escape it using backslash (\' or \").

print('This is Bob\'s greeting.')

# Let's explore more

name = 'Daniel'

# How to verify a type of data

print(type(name)) # <class 'str'> or str

# We'll get 'str', 'str' is a String Class, so wen can transform other types in strings easely

print(str(1)) # We pass 1 Integer and get '1' String
print(str(1.2)) # We pass 1.2 Float and get '1.2' String

# All Strings are unicode, so it's a high level object and need to be encoded 
# to save in a file or transfer by network, using 'encode' method to transform
# unicode object in bytecode

print('Daniel'.encode())
print('Simão'.encode())

# String in Python ar immutable

print(name.upper()) # upper transform the string in uppercase DANIEL
print(name) # daniel
print(name == name.upper()) # false

# capitalize string
print(name.capitalize()) # Daniel

name = 'daniel simão'

# each word become capitalized
print(name.title()) 

# how to replace string pieces to anothers
print(name.replace('s', 'SS'))

# how to split string
print(name.split()) # ['daniel', 'simão']

# We can pass a different delimiter, space is a default delimiter
print(name.split('a')) # ['d', 'niel simão']
print(name.split('i')) # ['dan', 'el s', 'mão']

# How to concatenate strings
# First way - Using Plus Sign
print('Daniel' + ' ' + 'Simão') # Here we concat 3 strings and return a 4th string

# Second way - Using 'join' method, that's get a delimiter and concat all the string
# as Array passed as parameter
print(' '.join(['daniel', 'simão']))
print('\n'.join(['daniel', 'simão']))

# How to know the string length
print(len(name))



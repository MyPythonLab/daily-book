# Modules - Introduction

# first of all, the python interpreter begin reads the 
# code at the top to the bottom and left to the right

# Here we'll learn about modules and work with keyword "import"
# to realize it, at the top of the file we import a 'os' module

import os

# after import certain module, this module can be a class, function, variable
# in this case we import a object with a bunch of functions, for example
# lets call the function 'getcwd' directly from 'os' object

print(os.getcwd())

# Now lets make a little bit different, we can get just a centain function or variable
# from module, using a different approuch to import, for example:

from os import getcwd

# And execute 'getcwd' in the same way we used before

print(getcwd());

# With Python we can set a variable with differente name and use it as a 'alias'
# let's create a alias for 'os' module:

import os as operational_system

# And call 'getcwd' and execute it:

print(operational_system.getcwd())

# Okay, let's create a alias for 'getcwd' too:

from os import getcwd as get_current_working_directory

print(get_current_working_directory())

# The Python is smart a lot to just reference all those class, objects, function and variable from 
# specific and unique local from memory, so he don't polute memory with a lot of data.
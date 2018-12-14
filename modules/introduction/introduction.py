# Modules - Introduction

# first of all, the python interpreter begin reads the 
# code at the top to the bottom and left to the right

# When calling the modules without import then an NameError occurs
# and all the application stops, because there is no variable in thje
# current namespace named 'os'

# os

'''Exception has occurred: NameError
    name 'os' is not defined
        File "D:\LEARNING\daily-book\modules\introduction.py", line 9, in <module>
            os'''

# Here we'll learn about modules and work with keyword "import"
# to realize it, at the top of the file we import a 'os' module

import os

# To verify the type of data we can use the global method called 'type'

print(type(os))

# To verify the module dundername

print(os.__name__)

# To verify the module absolute path

print(os.__file__)

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
# to prove it let's use the global 'id' function

print(id(os.getcwd), id(getcwd), id(get_current_working_directory))
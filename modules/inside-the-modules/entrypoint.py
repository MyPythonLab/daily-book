# Modules - Inside the modules

print('Begin', __name__)

# See this file to understand how it works
import external

print('Define fA')
def fA():
    print('Dentro fA')
    external.fB()

# verify if the module is a entrypoint is a good practice to prevent your code to runs
# if you just whant get some piece of code from module, like a function, constant or variable
# It's easy accomplish this verifying if dundername (__name__) is equal the string '__main__'

if __name__ == '__main__':
    print('Chama fA')
    fA()

print('End', __name__)
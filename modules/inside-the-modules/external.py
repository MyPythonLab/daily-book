# Modules - Inside the modules

# When the module is imported to other module, the dundername become the file name
# Here dundername is equal 'external' if imported and '__main__' if it's the entrypoint
print('Begin', __name__)

print('Define fB')
def fB():
    print('Dentro fB')

if __name__ == '__main__':
    print('Chama fB')
    fB()

print('End', __name__)
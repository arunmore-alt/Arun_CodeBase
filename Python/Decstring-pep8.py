print("Decstring PEP 8 Example")


def squre(n):
    ''' Take a number and return the squre of a number '''
    print(n*n)

squre(5)
print(squre.__doc__)

def squre(n):
    print(n)
    ''' Take a number and return the squre of a number '''
    print(n*n)

squre(5)
print(squre.__doc__)

def squre(n):
    """ Take a number and return the squre of a number """
    print(n*n)  
squre(5)
print(squre.__doc__)
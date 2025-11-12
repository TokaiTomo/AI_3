def factorial(n):
    '''This is a recursive function and is used to find factorial'''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial.__doc__)
print(factorial(5))
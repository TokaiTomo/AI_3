#positional arguments
def postional_arguments(a,b):
    return a+b
def default_arguments(p,q,message = "this is a number"):
    return f'{message}', p+q,
print(postional_arguments(1,2))
print(default_arguments(1,2))

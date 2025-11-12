def cube(n):
    num = n*n*n
    return num
def divisible(num):
    if num%3 == 0:
        return cube(num)
    else:
        return None
divisible(3)
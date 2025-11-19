try:
    num1 = int(input("Input a number: "))
    num2 = int(input("Input another number: "))
    result = num1/num2
    print("The result is: ", result)
    print("The result is: ", result1)
except ZeroDivisionError:
    print("Division with 0 is not allowed")
except NameError:
    print("The code is having a name error")
except ValueError:
    print("Only enter numerical values")
except:
    print("some kind of error is here")
finally:
    print("I will always run")    
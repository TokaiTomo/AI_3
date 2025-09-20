num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))
print('''
        Menu
    ------------
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Floor division
    6.Remainder calculator''')
cal = int(input("Which calculation?: "))
if cal == 1:
    print(num1 + num2)
elif cal == 2:
    print(num1 - num2)
elif cal == 3:
    print(num1 * num2)
elif cal == 4:
    print(num1 / num2)
elif cal == 5:
    print(num1 // num2)
elif cal == 6:
    print(num1 % num2)
else:
    print("Enter a proper choice!")
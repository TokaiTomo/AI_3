try:
    num = int(input("Enter your number: "))
    print(num)
except ValueError:
    print("Exception", ValueError)
print("I'm outside")
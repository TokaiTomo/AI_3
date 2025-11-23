valid = False
while not valid:
    try:
        num= int(input("Enter a number: "))
        while num%2 == 0:
            print("bye")
            valid = True
    except ValueError:
        print("Error")

valid = False #loop runs
while not valid: # same as While true
    try:
        n = int(input("Enter a number: "))
#enter a even number
        while n%2 == 0:
            print("bye")
            valid = True # loop stops
    except ValueError:
        print("Invalid")
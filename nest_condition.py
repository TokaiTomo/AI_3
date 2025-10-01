med = input("Did you have a medical condition?(Y/N): ")
attend = int(input("Input your attendance: "))
if med == "Y":
    print("You can take the test")
if med == "N":
    if attend >= 75:
        print("You can take the test")
    else: 
        print("You can not take the test")
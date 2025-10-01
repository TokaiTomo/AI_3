unit = int(input("Enter the number of units you have: "))
if unit <= 50:
    print("Your bill is 2.60/unit and the tax is 25")
elif unit > 50 and unit < 100:
    print("Your bill is 3.25/unit and the tax is 35")
elif unit > 100 and unit < 200:
    print("Your bill is 5.26/unit and the tax is 45")
elif unit > 200:
    print("Your bill is 8.45/unit and the tax is 75")
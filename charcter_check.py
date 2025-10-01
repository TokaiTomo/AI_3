alphabet = ("abcdefghijklmnopqrstuvwxyz")
number = ("1234567890")

input = input("Enter your character. Don't be mean and put in multiple characters: ")
lowercase = input.lower()
if lowercase in alphabet :
    print("It is an alphabet")
if lowercase not in alphabet:
    if lowercase not in number:
        print("This is not a number nor an alphabet\nThis is a symbol")
if lowercase in number :
    print("It is a number")


alphabet = ("abcdefghijklmnopqrstuvwxyz")
input = input("Enter your character: ")
lowercase = input.lower()
if lowercase in alphabet :
    print("It is an alphabet")
if lowercase not in alphabet:
    print("This is not an alpahbet")

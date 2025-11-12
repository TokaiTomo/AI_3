choice = int(input("""
Choose a calculation
=========================
1.addition
2.subtraction
3.multplication
4.division
-------------------------
Enter your choice: """))
a = int(input("Enter the first number: "))
b = int(input("Enter the seconnd number: "))
def add(p,q):
    ans=p+q
    return ans
def sub(p,q):
    ans = p-q
    return ans
def mult(p,q):
    ans=p*q
    return ans
def divide(p,q):
    ans = p/q
    return ans
if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(sub(a,b))
elif choice == 3:
    print(mult(a,b))
elif choice == 4:
    print(divide(a,b))
else:
    print("Not a choice")
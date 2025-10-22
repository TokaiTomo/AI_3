num = int(input("Enter your number:"))
ans = num
power = int(input("How many times to power: "))
for i in range (1,power):
    ans = ans * num
print(ans)
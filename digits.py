num = int(input("Enter your number: "))
num_1 = num
digit = 0
while num_1 > 10:
    num_1 = num_1/10
    digit=digit + 1
digit = digit + 1
print(digit)
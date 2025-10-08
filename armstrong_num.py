num = int(input("Enter your number: "))

hun = num//100
ten = (num-hun*100)//10
one = num-(hun*100 + ten*10)
print(hun, ten, one)
ans = hun**3+ten**3+one**3
print(ans)
if ans == num:
    print("This is an armstrong number")
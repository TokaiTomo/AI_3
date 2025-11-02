num = str(input("Your number: "))
length=len(num)
while True:
    if length%2==0:
        ans_2=num[length//2]
        ans_1=num[length//2-1]
        print(ans_1,ans_2)
        break
    if length%2==1:
        ans_1=num[length//2]
        print(ans_1)
        break

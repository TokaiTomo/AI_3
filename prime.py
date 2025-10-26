low_range = int(input("Enter the lower range: "))
up_range = int(input("Enter the upper range: "))
for i in range(low_range,up_range+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
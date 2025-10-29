rows = int(input("Number of rows: "))
if rows%2 == 0:
    halfDiamond = rows // 2
else:
    halfDiamond = rows // 2 +1
space = halfDiamond-1
for i in range(1,halfDiamond + 1):
    for j in range(1, space + 1):
        print(end= " ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(num, end=" ")
        num = num + 1
    print()
space = 1
for i in range(halfDiamond -1,0,-1):
    for j in range(1, space + 1):
        print(end= " ")
    space = space + 1
    num = 1
    for j in range(2*i-1):
        print(num, end=" ")
        num = num + 1
    print()
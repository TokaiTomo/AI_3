point_1 = float(input("Please input your first score: "))
point_2 = float(input("Please input your second score: "))
point_3 = float(input("Please input your third score: "))
point_4 = float(input("Please input your fourth score: "))
point_5 = float(input("Please input your fifth score: "))
total = (point_1+point_2+point_3+point_4+point_5)
avg = total/5
if avg == 100:
    print("A+")
elif avg >= 95 and avg<= 99:
    print("A")
elif avg >= 90 and avg<=94:
    print("A-")
elif avg >= 88 and avg<=89:
    print("B+")
elif avg >= 84 and avg<=87:
    print("B")
elif avg >= 80 and avg<=83:
    print("B-")
elif avg >= 78 and avg<=79:
    print("C+")
elif avg >= 74 and avg<=77:
    print("C")
elif avg >= 70 and avg<=73:
    print("C-")
else:
    print("F")
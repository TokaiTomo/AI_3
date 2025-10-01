point_1 = float(input("Please input your first score: "))
point_2 = float(input("Please input your second score: "))
point_3 = float(input("Please input your third score: "))
point_4 = float(input("Please input your fourth score: "))
point_5 = float(input("Please input your fifth score: "))
total = (point_1+point_2+point_3+point_4+point_5)
avg = total/5
if avg == 100 and avg >= 91:
    print("A+")
elif avg >= 81 and avg<= 90:
    print("A")
elif avg >= 71 and avg<=80:
    print("A-")
elif avg >= 61 and avg<=70:
    print("B+")
elif avg >= 51 and avg<=60:
    print("B")
elif avg >= 41 and avg<=50:
    print("B-")
else:
    print("C")
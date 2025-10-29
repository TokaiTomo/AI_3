print("half pyramid patterns of stars")
n = int(input("Number of the rows you want: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
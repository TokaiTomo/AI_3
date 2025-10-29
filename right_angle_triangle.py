print("half pyramid patterns of stars")
rows = int(input("Number of the rows you want: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()
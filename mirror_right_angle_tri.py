print("mirred half pyramid patterns of stars")
rows = int(input("Number of the rows you want: "))
space = 1
for i in range(rows):

    for z in range(1, space + 1):
        print(end= " ")
    space = space+1

    for j in range(2*i-1):
        print(" ")        
        print("*", end=" ")


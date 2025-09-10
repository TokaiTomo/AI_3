money = int(input("Enter the amount of money you have: "))
hundred=money//100
fifty=(money%100)//50
ten = ((money%100)%50)//10
print("100 notes:", hundred, "\n50 notes:", fifty, "\n10 notes:", ten)
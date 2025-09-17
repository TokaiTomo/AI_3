buy = int(input("Enter the money that you bought with: "))
sell = int(input("Enter the money that you sold with: "))

if buy >= sell:
    print("It is a loss")
else:
    profit = sell - buy
    print("It is a profit")
    print("You got", profit)
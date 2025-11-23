import random
bot = random.randint(0,20)
user = int(input("Input your guess from 0 to 20: "))
while not user == bot:
    print("Your guess:", user)
    print("Bot's guess:", bot)
    if user == bot:
        print("Your guess:", user)
        print("Bot's guess:", bot)
        print()
        break
        
    else:
        print("Bot wins ☹️")
        print()
        bot = random.randint(0,20)
        user = int(input("Guess again: "))
print()
print("You win!!!! 😃")
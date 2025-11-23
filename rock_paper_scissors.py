import random
bot = random.choice(["rock🪨","paper🗒️","scissors✂️"])
user = input("Your choice (rock, paper or scissors): ")
if user == 'rock':
    user = 'rock🪨'
if user == 'scissors':
    user = 'scissors✂️'
if user == 'paper':
    user = 'paper🗒️'

print("Bot's choice:", bot)
print("User's choice:", user)

if bot == user:
    print("Draw!")

elif bot == 'rock🪨' and user == 'scissors✂️':
    print("The bot wins!")

elif bot == 'scissors✂️' and user == 'paper🗒️':
    print("The bot wins!")

elif bot == 'paper🗒️' and user == 'rock🪨':
    print("The bot wins!")

elif bot == 'rock🪨' and user == 'paper🗒️':
    print("You win!")

elif bot == 'scissors✂️' and user == 'rock🪨':
    print("You win!")

elif bot == 'paper🗒️' and user == 'scissors✂️':
    print("You win!")

else:
    print("Error")
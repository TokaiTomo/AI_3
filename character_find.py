word = input("Enter your word to check: ")
letter = input("Eneter the letter you want to check: ")
i = 0
num = 0
while i < len(word):
    if word[i] == letter:
        num = num + 1
    i = i + 1
print(num)
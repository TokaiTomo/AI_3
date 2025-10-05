sentence = input("Input a sentence: ")
sentence = sentence.split()
print(sentence)
long = 0
for i in sentence:
    length = len(i)
    if length > long:
        long = length
for i in sentence:
    length = len(i)
    if length == long:
        print(i)


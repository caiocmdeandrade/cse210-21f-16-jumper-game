import random
"""
word = list("book")
guess = input("Enter a letter: ")

while guess != "1":
    for i in range(len(word)):
        letter = word[i]
        if letter == guess:
            word.remove(letter)
            indice = i
            print(indice)
    guess = input("Enter a letter: ")

print()
print(word)
"""
"""
guess = "o"

words = ["book", "house", "mouse"]

print(words)
print(type(words))

word = list(random.choice(words))

print(word)
print(type(word))
"""

word = list("book")

for i in range(len(word)):
    print(i)

print()

guessed_letters = {}
for i in range(len(word)):
    letter = word[i]
    guessed_letters[i] = letter

print(guessed_letters)    


draw = ["   ___", "  /   \\", " /_____\\", " \     /", "  \   /", "   \ /", "    0", "   /|\\", "   / \\", " ^^^^^^^"]

for i in draw:
    print(i)

print()
import random
"""
words = ["book", "house", "mouse"]

# método que elige una palabra al azar.
def choose_a_word():
    word = random.choice(words)
    return word


the_word = choose_a_word()
print(the_word)
"""
word = "book"

mentioned_letters = []
# método que chequea que lo ingresado sea una letra y que no haya sido usada previamente
def guess_letter():
    while True:
        guess = input("Guess and type a letter from [a-z]: ")
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha() and guess not in mentioned_letters:
            mentioned_letters.append(guess)
            break
        else:
            print("Remember you must type one letter and it needs to be a different one than: " + ", ".join(mentioned_letters))
    return guess


# Chequea si una letra está en la palabra y retorna el 'indice'
letters_index = []
def check_letter_in_word(guess):
    for i in range(len(word)):
        letter = word[i]
        print(f"En el índice {i} se encuentra la letra {letter}")
        
        #if letter == guess:
        #    indice = i
        #    print(indice)

line = []
def print_dash(guess):    
    for i in word:
        if guess == i:
            line.append(i)
    
    print(line)

while True:
    guess = guess_letter()
    check_letter_in_word(guess)
    print_dash(guess)
"""
def print_dash(guess):    
    for i in word:
        if guess == i:
            print(i, end=" ")
        else:
            print("_", end=" ")
"""
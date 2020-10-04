import random

fwords = ("Cannelloni", "Vheeseburger",  "Spaghetti", "Chowder")

display = []
guessed_lets = []
guess = 0
    new = random.randint(0, len(word)+1)
    hang_word = word[new]
    display = "_" * len(hang_word)
    print (display)

def guess_return(user_guess):
    for i in range(len(hang_word)):
        if user_guess.lower() == hang_word[i].lower():
            display[i] = hang_word[i]
        print(display)
        return True
    print(guessed_lets)
    print(display)
    if guess_return(user_guess) != True:
        print ("nah b, guess again")
        guess_return = False

    


print("welcome to hang man dawg")
new = random.randint(0, len(fword)+1)
hang_word = fwords[new]
display = "_" * len(hang_word)
print (display)

guesses = 0
while guesses < 7:
    guess = input("Guess a letter")
    if guess.isalpha():
            guess_return(guess)
    else:
        print("Please guess a letter")
        guess = input ("Guess a letter")
    if guess_return == False:
        guessed_lets.append(guess)
        print(guessed_lets)
        print(display)
        guesses =+ 1
    
            




# define a random word out of wordlist-german.txt

from random import randint
import os
hangman_art = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========""",
    """
    +---+
    |   |
   [O   |
   /|\  |
   / \  |
        |
    =========""",
    """
    +---+
    |   |
   [O]  |
   /|\  |
   / \  |
        |
    =========""",
]


wordlist = open(os.path.dirname(os.path.abspath(__file__))+"\wordlist-german.txt", "r")
wordlist = wordlist.readlines()
wordlist = [word.strip() for word in wordlist]
word = wordlist[randint(0, len(wordlist)-1)]
word = word.upper()

# start the game

print("Willkommen bei Hangman!")
print("das wort hat", len(word), "buchstaben")
print("du hast 8 versuche")
print("viel glück!")
print(" ")
print(hangman_art[0] + "\n")


# create a list of underscores at the length of the word

letters = []
for i in range(len(word)):
    letters.append("_")


# set up the game loop
guesses = 0
guesslist = []
while guesses < 8:
    print(" ".join(letters))
    guess = input("\n" "rate einen buchstaben: ")
    guess = guess.upper()
    if guess in guesslist:
        print("du hast diesen buchstaben schon geraten!")
    if guess in letters:
        print("du hast diesen buchstaben schon geraten!")
    elif guess in word:
        print("richtig!")
        for i in range(len(word)):
            if word[i] == guess:
                letters[i] = guess
    else:
        print("falsch!")
        guesses += 1
        guesslist.append(guess)
        print(guesses)
        print(hangman_art[guesses])
    if "_" not in letters:
        break

# check if the player won or lost
if guesses == 8:
    print("du hast verloren!")
    print("das wort war", word)
else:
    print("du hast gewonnen!")
    print("das wort war", word)


# change the code so that the player can choose between different levels
from replit import clear
import random
stages = [
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]
hangman_logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

print(hangman_logo)
print("Welcome to hangman!\n""In this game you will have to guess a letter by the time you find the word.\n"
      "If the letter you guessed is wrong, you lose a life and aprts of the person is drawn. When the person is fully drawn, game is over!")
lives = 6
import adverbs
word = random.choice(adverbs.adverbs100)
word = word.lower()
length = len(word)
display = []
for i in range(length):
    display += "_"
print(f"{' '.join(display)}\n")
eog = False ##end of game
while not eog:
    guess = input("Guess a letter: ")
    clear()
    if guess in display:
        print(f"You have already guessed {guess}")
    if guess in word:
            for i in range(length):
                if word[i] == guess:
                    display[i] = guess
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"{''.join(display)}")
    if lives > 0:
        print(stages[lives])
    if lives == 0:
        eog = True
        print("You lose(\n"f"The hidden word was {word}")
    if "_" not in display:
        eog = True
        print("You won)")
    



























































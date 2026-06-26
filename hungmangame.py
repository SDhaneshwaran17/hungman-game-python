import random
optional_words = [
    "apple", "mango", "banana", "strawberry",
    "guava", "orange", "pineapple",
    "papaya", "kiwi", "watermellon"
]
hangman_stages = [
"""
  +---+
  |   |
      |
      |
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
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

word = random.choice(optional_words)
characters = len(word)
no_of_blanks = ["_"] * characters


print("READY FOR THE GAME, THE NUMBER OF BLANK SPACES TO BE GUESSED RIGHT TO WIN THE GAME ARE:")
print(" ".join(no_of_blanks))
wrong_guesses = 0
def guess_letter():
    global wrong_guesses

    guess = input("GUESSING A LETTER IN THE WORD:")

    if guess in word:
        print("CORRECT ANSWER:")

        for position in range(len(word)):
            if word[position] == guess:
                no_of_blanks[position] = guess

        print("".join(no_of_blanks))
        if "_" not in no_of_blanks:
            print("YOU WON! 🎉 CONGRATULATIONS!")

    else:
        print("WRONG ANSWER:")
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses -1])
        if wrong_guesses == 6:
            print("YOU HAVE LOST THE GAME!")
            print("BETTER LUCK NEXT TIME 💔")
            print("THE WORD WAS:", word)
            return

    print(f"Lives remaining: {6 - wrong_guesses}")

while "_" in no_of_blanks and wrong_guesses < 6:
    print("FIND THE REMAINING WORDS:")
    guess_letter()

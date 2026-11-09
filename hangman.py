import random

words = ["apple", "mango", "python", "computer", "school"]

word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong attempts:", wrong, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("Congratulations! You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed this letter!")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("Wrong guess!")

if wrong == max_wrong:
    print("Game Over!")
    print("The word was:", word)
# codealpha-projects
import random

# List of predefined words
words = ["python", "programming", "computer", "developer", "software"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0

# Display the hidden word
display_word = ["_"] * len(word)

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    # Get player's guess
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Incorrect guess!")

# Display final result
if "_" not in display_word:
    print("\nCongratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("\nGame Over! 😢")
    print("The correct word was:", word)

print("Thanks for playing!")

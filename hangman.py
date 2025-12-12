"""
Simple Hangman Game
Author: Your Name
Description:
    A basic text-based Hangman game using console input.
    - Uses 5 predefined words
    - Allows 6 incorrect guesses
    - Demonstrates: random, loops, lists, strings
"""

import random


def choose_word():
    """Return a random word from a predefined list."""
    words = ["apple", "tiger", "house", "snake", "green"]
    return random.choice(words)


def display_progress(secret_word, guessed_letters):
    """Return a string showing the hidden word with guessed letters revealed."""
    return " ".join([char if char in guessed_letters else "_" for char in secret_word])


def hangman():
    """Main game function."""
    secret_word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect:
        print("\nWord:", display_progress(secret_word, guessed_letters))

        # Check win condition
        if all(char in guessed_letters for char in secret_word):
            print("\n🎉 You win! The word was:", secret_word)
            return

        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("❗ Already guessed. Try a new letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✓ Correct!")
        else:
            incorrect_guesses += 1
            print(f"✗ Wrong! Incorrect guesses: {incorrect_guesses}/{max_incorrect}")

    # Lose condition
    print("\n💀 Game Over! You ran out of guesses.")
    print("The word was:", secret_word)


if __name__ == "__main__":
    hangman()

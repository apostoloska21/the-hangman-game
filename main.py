import random
import hangman_words
import hangman_art

# List of words to choose from
chosen_word = random.choice(hangman_words.word_list)

display = ["_" for _ in range(len(chosen_word))]
lives = 4
wrong_guesses = 0


def is_word_guessed(display):
    return "_" not in display


print(hangman_art.logo)
print(hangman_art.stages[lives])
while wrong_guesses < 4 and not is_word_guessed(display):
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        wrong_guesses += 1
        lives -= 1
        print(hangman_art.logo)
        print(hangman_art.stages[lives])
        print(f"Wrong guess. You have {lives} lives left.")

    print("Current word: ", " ".join(display))

if is_word_guessed(display):
    print("Congratulations! You've guessed the word.")
else:
    print(f"Sorry, you've run out of lives. The word was '{chosen_word}'.")

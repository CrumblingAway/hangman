import random

NUM_MAX_GUESSES = 10

EMPTY_COMMAND = ""
QUIT_COMMAND = "quit"

WELCOME_MSG = f"""
\tWelcome to Hangman!
\tTo begin press the <ENTER> key.
\tTo make a guess press your letter of choice and then press the <ENTER> key.
\tTo exit at any point write \"{QUIT_COMMAND}\" and press the <ENTER> key.
"""

WIN_MSG = "Congratulations! You've guessed the word!"
LOSS_MSG = "Better luck next time!"
ALREADY_GUESSED_LETTER_MSG = "You've already guessed this letter!"
INVALID_INPUT_MSG = "Invalid input."
EMPTY_INPUT_MSG = "Make a guess!"
WRONG_GUESS_MSG = "This letter is not in the word!"
GOODBYE_MSG = "Goodbye!"

def choose_word() -> str:
    chosen_word = None

    words_file = open("resources/words.txt", "r")

    num_of_words = 0
    for _ in words_file:
        num_of_words += 1
    words_file.seek(0)
    word_line_idx = random.randint(0, num_of_words - 1)
    for idx, line in enumerate(words_file):
        if idx == word_line_idx:
            chosen_word = line.strip().lower()
            break

    words_file.close()

    return chosen_word

def get_user_guess_indices(user_guess: chr, word: str) -> list[int]:
    indices = []

    for idx, letter in enumerate(word):
        if user_guess == letter:
            indices.append(idx)

    return indices

def is_input_valid(user_input: str) -> bool:
    return user_input == QUIT_COMMAND\
           or user_input == EMPTY_COMMAND\
           or (len(user_input) == 1 and user_input.isalpha())

if __name__ == "__main__":
    print(WELCOME_MSG)

    # Start game.
    while True:
        user_input = input()
        if not is_input_valid(user_input):
            print(INVALID_INPUT_MSG)
            continue

        if user_input == QUIT_COMMAND:
            print(GOODBYE_MSG)
            quit()
        elif user_input == EMPTY_COMMAND:
            break

    word = choose_word()
    word_guess_progress = "_" * len(word)
    guessed_letters = []
    wrong_guesses = 0

    # Game loop.
    while True:
        print(f"{word_guess_progress} ({NUM_MAX_GUESSES - wrong_guesses} guesses left)")
        print(f"Guessed letters: {guessed_letters}")
        user_input = input()

        # Invalid input.
        if not is_input_valid(user_input):
            print(INVALID_INPUT_MSG)
            continue
        user_input = user_input.lower()

        if user_input == QUIT_COMMAND:
            print(f"The word was {word}.")
            break
        elif user_input == EMPTY_COMMAND:
            print(EMPTY_INPUT_MSG)
            continue

        if user_input in guessed_letters:
            print(ALREADY_GUESSED_LETTER_MSG)
            continue

        # Process user guess.
        guessed_letters.append(user_input)

        guess_indices = get_user_guess_indices(user_input, word)
        if len(guess_indices) == 0:
            print(WRONG_GUESS_MSG)
            wrong_guesses += 1

            # Lose game.
            if wrong_guesses >= NUM_MAX_GUESSES:
                print(f"The word was {word}. {LOSS_MSG}")
                break
            continue

        for idx in guess_indices:
            word_guess_progress = word_guess_progress[:idx]\
                + user_input\
                + word_guess_progress[idx + 1:]

        # Win game.
        if word_guess_progress == word:
            print(word)
            print(WIN_MSG)
            break

    print(GOODBYE_MSG)

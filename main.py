import random

QUIT_COMMAND = "quit"

WELCOME_MSG = f"""
\tWelcome to Hangman!
\tTo begin press the <ENTER> key.
\tTo make a guess press your letter of choice and then press the <ENTER> key.
\tTo exit at any point write \"{QUIT_COMMAND}\" and press the <ENTER> key.
"""

WIN_MSG = "Congratulations! You've guessed the word!"
LOSS_MSG = "Better luck next time!"

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



if __name__ == "__main__":
    print(WELCOME_MSG)

    user_input = input()
    if user_input == QUIT_COMMAND:
        print(GOODBYE_MSG)
        quit()

    word = choose_word()
    while user_input := input() != QUIT_COMMAND:
        pass

    print(GOODBYE_MSG)

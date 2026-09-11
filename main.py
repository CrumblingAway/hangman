import random

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
    print(choose_word())

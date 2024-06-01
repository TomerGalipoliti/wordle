import wordle_interface
import english_dict
import random

WORD_LEN = wordle_interface.WORD_LEN
TRIES = 6

GREY = 0
YELLOW = 1
GREEN = 2

all_words = english_dict.get_all_n_letters_words(WORD_LEN)

prev_guesses_example = [{'word': 'argue', 'res': [YELLOW, GREY, GREY, GREY, GREY]},
                        {'word': 'blast', 'res': [GREEN, GREY, YELLOW, YELLOW, GREY]},
                        {'word':'backs', 'res': [GREEN,GREEN,GREY,GREY,YELLOW]},
                        {'word':'basan', 'res': [GREEN,GREEN,GREEN,GREY,GREEN]}]

def is_word_possible(word, prev_guesses, debug=False):
    for guess in prev_guesses:
        for i in range(WORD_LEN):
            if guess['res'][i] == GREEN:
                if guess['word'][i] != word[i]:
                    return False
            if guess['res'][i] == YELLOW:
                if (guess['word'][i] not in word) or (guess['word'][i] == word[i]):
                    return False        
            if guess['res'][i] == GREY:
                greens = [word[i] for i in range(len(word)) if guess['res'][i] == GREEN]
                if (guess['word'][i] in word) and (guess['word'][i] not in greens):
                    return False 
                if guess['word'][i] == word[i]:
                    return False
    return True

def get_possible_words(prev_guesses, curr_possible_words):
    possible_words = []
    for word in curr_possible_words:
        if is_word_possible(word, prev_guesses):
            possible_words.append(word)
    return possible_words

def choose_word_from_possible(possible_words):
    return random.choice(possible_words)


def get_next_guess_naive(prev_guesses):
    curr_posib = get_possible_words(prev_guesses, all_words)
    return choose_word_from_possible(curr_posib)

def solve(get_next_guess):
    prev_guesses = []
    for i in range(TRIES):
        word_guess = get_next_guess(prev_guesses)
        guess = wordle_interface.try_word(word_guess)
        if guess['res'] == [GREEN] * WORD_LEN:
            print(f'found word: {word_guess} after {i + 1} tries')
            return i+1
        print(f'guess: {guess}')
        prev_guesses.append(guess)
    print(f'failed within {TRIES} tries')
    return -1

def main():
    failures = 0
    total_tries = 0
    iterations = 100
    for i in range(iterations):
        n = solve(get_next_guess_naive)
        if n == -1:
            failures += 1
        else:
            total_tries += n
        wordle_interface.set_new_word()

    print(f'failues: {failures}, average tries on success: {total_tries / (iterations - failures)}')
    

if __name__ == '__main__':
    main()

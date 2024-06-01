import wordle_interface
import random

DICT_FILE = 'words_alpha.txt'
WORD_LEN = 5
TRIES = 6

GREY = 0
YELLOW = 1
GREEN = 2


def get_all_5_letters_words():
    with open(DICT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines] # remove newline char
    return [word for word in lines if len(word) == WORD_LEN]

all_words = get_all_5_letters_words()

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

if __name__ == '__main__':
    prev_guesses = []
    curr_posib = all_words
    for i in range(TRIES):
        word_guess = choose_word_from_possible(curr_posib)
        guess = wordle_interface.try_word(word_guess)
        if guess['res'] == [GREEN] * WORD_LEN:
            print(f'found word: {word_guess} after {i + 1} tries')
            exit()      
        print(f'guess:\n{guess}')
        prev_guesses.append(guess)
        curr_posib = get_possible_words(prev_guesses, curr_posib)
    
    print(f'left with words: {curr_posib}')
    
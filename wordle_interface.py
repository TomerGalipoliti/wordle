import english_dict
import random

WORD = 'agush'
WORD_LEN = 5
assert len(WORD) == WORD_LEN


GRAY = 0
YELLOW = 1
GREEN = 2

all_words = english_dict.get_all_n_letters_words(WORD_LEN)

def getGreenSTR(skk): return "\033[92m {}\033[00m" .format(skk)
def getYellowSTR(skk): return "\033[93m {}\033[00m" .format(skk)
def getLightGraySTR(skk): return "\033[97m {}\033[00m" .format(skk)
color_fn = {GRAY: getLightGraySTR, YELLOW: getYellowSTR, GREEN: getGreenSTR}

def print_guess(guess):
    colored_word = ""
    for i in range(WORD_LEN):
        colored_word += color_fn[guess["res"][i]](guess["word"][i])
    print(colored_word)

letters_history = {chr(i) : GRAY for i in range(97,97+26)}
def print_keyboard():
    keyboard_str = ""
    for letter,val in letters_history.items():
        keyboard_str += color_fn[val](letter)
    print(keyboard_str)


def set_new_word():
    global WORD
    WORD = random.choice(all_words)
    print(f'new word been set: {WORD}')
    for letter in letters_history:
        letters_history[letter] = GRAY

def try_word(word):
    if len(word) != len(WORD):
        print('bad word length')
        return None
    if word not in all_words:
        print('word is not in dict')
        return None
    res = [GRAY] * WORD_LEN
    yellow_lookup = ''
    for i in range(WORD_LEN):
        if word[i] == WORD[i]:
            res[i] = GREEN
            letters_history[word[i]] = GREEN
        else:
            yellow_lookup += WORD[i]

    for i in range(WORD_LEN):
        if res[i] == GREEN:
            continue
        if word[i] in yellow_lookup:
            res[i] = YELLOW
            yellow_lookup = yellow_lookup.replace(word[i], '', 1)
            letters_history[word[i]] = YELLOW

    return {'word': word, 'res': res}


def main():
    retries = 6
    while retries > 0:
        print('enter guess:')
        word = input()
        guess = try_word(word)
        if not guess:
            continue
        print_guess(guess)
        print_keyboard()
        if guess['res'] == ([GREEN] * WORD_LEN):
            print('well done')
            exit()
        retries -= 1
    print('no luck')

if __name__ == '__main__':
    main()
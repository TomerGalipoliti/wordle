WORD = 'basin'
WORD_LEN = 5
assert len(WORD) == WORD_LEN


GREY = 0
YELLOW = 1
GREEN = 2

def try_word(word):
    word_chars = list(word)
    if len(word) != len(WORD):
        raise Exception('bad word length')
    res = [None] * WORD_LEN
    for i in range(WORD_LEN):
        if word_chars[i] == WORD[i]:
            res[i] = GREEN
            word_chars[i] = '!'

    for i in range(WORD_LEN):
        if word_chars[i] in WORD:
            res[i] = YELLOW
            word_chars[i] = '!'

    for i in range(WORD_LEN):
        if word_chars[i] != '!':
            res[i] = GREY
    
    assert None not in res

    return {'word': word, 'res': res}
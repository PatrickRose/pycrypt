import operator

LETTER_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .!?"

def add_letters(a, b):
    a_int = LETTER_LIST.find(a)
    b_int = LETTER_LIST.find(b)
    answer = operator.mod(a_int + b_int, len(LETTER_LIST))
    return LETTER_LIST[answer]

def subtract_letters(a, b):
    a_int = LETTER_LIST.find(a)
    b_int = LETTER_LIST.find(b)
    answer = operator.mod(a_int - b_int, len(LETTER_LIST))
    return LETTER_LIST[answer]

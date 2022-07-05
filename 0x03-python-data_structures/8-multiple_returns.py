#!/usr/bin/python3
# return a tupole with the length of a string,
# and its first character
def multiple_returns(sentence):
    str_len = len(sentence)
    if not str_len:
        first = None
    else:
        first = sentence[0]
    return (strlen, first)

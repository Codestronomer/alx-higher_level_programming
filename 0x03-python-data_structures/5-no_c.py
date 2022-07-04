#!/usr/bin/python3
# removes all characters c and C from a string
def no_c(my_string):
    i = len(my_string)
    j = 0
    n_str = ''
    while j < i:
        if my_string[j] == 'c' or my_string[j] == 'C':
            pass
        else:
            n_str += my_string[j]
        j += 1
    return n_str

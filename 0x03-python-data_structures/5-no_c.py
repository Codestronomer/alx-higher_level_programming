#!/usr/bin/python3
# removes all characters c and C from a string
def no_c(my_string):
    if not my_string:
        pass
    else:
        i = len(my_string)
        j = 0
        n_str = ""
        while j < i:
            if my_string[j].lower() == 'c':
                n_str += ''
            else:
                n_str += my_string[j]
            j += 1
    return n_str

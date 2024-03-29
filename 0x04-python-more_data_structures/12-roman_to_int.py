#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return (0)
    rm_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        if (i + 1 < len(roman_string)):
            if (rm_dict[roman_string[i]] >= rm_dict[roman_string[i + 1]]):
                result += rm_dict[roman_string[i]]
                i += 1
            else:
                result += rm_dict[roman_string[i + 1]]-rm_dict[roman_string[i]]
                i += 2
        else:
            result += rm_dict[roman_string[i]]
            i += 1
    return (result)

#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            num = ord(str[i]) - 32
        else:
            num = ord(str[i])
        print("{:c}".format(num), end='')
    print()

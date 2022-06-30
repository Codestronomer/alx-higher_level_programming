#!/usr/bin/python3
i = 122
while i > 96:
    num = i
    if i % 2 != 0:
        num -= 32
    print("{:c}".format(num), end="")
    i -= 1

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
is_negative = number < 0
if is_negative:
    last_digit *= -1
str = f"Last digit of {number} is {last_digit} "
if last_digit > 5:
    str += "and is greater than 5"
elif last_digit == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"
print(str)

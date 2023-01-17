#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_number = abs(number) % 10
last_digit_str = repr(last_digit_number)
last_digit_str = last_digit_str[-1]
last_digit = int(last_digit_str)
if number > 0:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif number < 0:
    print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")


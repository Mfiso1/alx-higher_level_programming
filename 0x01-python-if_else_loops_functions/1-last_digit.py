#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(str(number)[-1]) > 5:
    print(
        f"Last digit of {number:d} is {str(number)[-1]} and is greater than 5")
elif int(str(number)[-1]) == 0:
    print(
        f"Last digit of {number:d} is {str(number)[-1]} and is 0")
else:
    print(
        f"Last digit of {number:d} is {str(number)[-1]} and is less than 6 and is not 0")

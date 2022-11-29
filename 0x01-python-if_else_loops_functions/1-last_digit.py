#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lasDig = number % 10
    if lasDig > 5:
        print(f"Last digit of {number} is {lasDig} and is greater than 5")
    elif lasDig == 0:
        print(f"Last digit of {number} is {lasDig} and is 0")
    elif lasDig < 6 and lasDig != 0:
        print(f"Last digit of {number} is {lasDig} and is less than 6 and not 0")
else:
    lasDig = -1 * (number % 10)
    if lasDig < 0:
        print(f"Last digit of {number} is {lasDig} and is less than 6 and not 0")

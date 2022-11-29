#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lasDig = abs(number) % 10
if number >= 0:
    if lasDig > 5:
        print(f"Last digit of {number} is {lasDig} and is greater than 5")
    elif lasDig == 0:
        print(f"Last digit of {number} is {lasDig} and is 0")
    elif lasDig < 6 and lasDig != 0:
        print(f"Last digit of {number} is {lasDig} and is less than 6 and not\
                0")
if number < 0:
    lasDig = -1 * lasDig
    print(f"Last digit of {number} is {lasDig} and is less than 6 and not 0")

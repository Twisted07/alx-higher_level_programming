#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastDigit = int(repr(number)[-1])
if (lastDigit == 0):
	print (F"Last digit of {number:d} is {lastDigit:d} and is 0")
elif (lastDigit < 6) and (lastDigit != 0):
	print (F"Last digit of {number:d} is {lastDigit:d} and is less than 6 and not 0")
else:
	print (F"Last digit of {number:d} is {lastDigit:d} and is greater than 5")
#!/usr/bin/python3
def print_last_digit(number):
    lastD = number % 10
    if number < 0:
        lastD = (number % (-10)) * (-1)
    print(f"{lastD}", end="")
    return lastD

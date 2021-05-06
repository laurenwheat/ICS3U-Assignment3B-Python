#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better


def main():
    # this function plays the number guessing game, but better

    guess = int(input("Enter a number: "))
    guessx = int(input("Enter another number: "))

    if guess < guessx:
        print(guessx)
        print("Is larger than")
        print(guess)
    elif guess > guessx:
        print(guess)
        print("Is larger than")
        print(guessx)
    elif guess == guessx:
        print("The numbers are equal")


if __name__ == "__main__":
    main()

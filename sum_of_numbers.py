#!/usr/bin/env python3

# Created By: Isaiah Fernandez
# Date: November 10, 2022
# This program calculates the sum of a number from 0 until the user number.


def main():

    # initialize the loop count and sum of the numbers
    loop_count = 0
    sum_num = 0

    # Get user number
    user_number = input("Input the number you wish to calculate: ")
    # Try catch for invalid input
    try:
        user_number = int(user_number)

    except ValueError:
        print("Please input an integer")
        print("")
        return main()
    # Line spacer
    print("")

    # checks to see if user number is positive
    if user_number < 0:
        print("Please input a positive number")
        print("")
        return main()

    # Calculates the sum of numbers from 0
    while loop_count <= user_number:
        sum_num += loop_count
        print("Tracked {} times through loop".format(loop_count))
        loop_count = loop_count + 1

    # Line spacer
    print("")

    # Displays result to user
    print("The sum number from 0 to {} is: {}.".format(user_number, sum_num))


if __name__ == "__main__":
    main()
"""
File: random_numbers.py
Authors: David Mendenhall, Miles Noble, Spencer Sowby

Purpose:
    As a team, write a Python program named random_numbers.py that creates
    a list of numbers, appends more numbers onto the list, and prints the
    list. The program must have two functions named main and append_random_numbers
    as follows:

    Core Requirements:
        1. Your program includes two functions named main and append_random_numbers.
        The append_random_numbers function has two parameters named numbers_list and
        quantity, and quantity has a default value of 1.

        2. The main function calls append_random_numbers twice, first with one
        argument and second with two arguments.

        3. The append_random_numbers function includes a loop that appends quantity
        random numbers at the end of numbers_list.


    Stretch Challenges:
        1. Add a function named append_random_words that meets the following criteria:
            a. Has two parameters: a list named words_list and an integer
            named quantity. The parameter quantity has a default value of 1
            b. Randomly selects quantity words from a list of words and
            appends the selected words at the end of words_list.
        
        2. Add statements in the main function that create a list of words, call the
        append_random_words function, and then print the list of words.

        3. Add something or change something in your program that you think would
        make your program better, easier for the user, more elegant, or more fun.
        Be creative.
"""

import random


def main():
    """ Call the append_random_numbers function to add numbers to a list.

    Parameters: none
    Return: none
    """
    words = ["bird", "boy", "car", "cat", "child",
             "dog", "girl", "man", "rabbit", "woman"]

    num_quantity = int(
        input("How many numbers would you like to add to the list: "))
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    # add 1 number to the numbers list then print
    append_random_numbers(numbers)
    print(numbers)

    # add 3 numbers to the numbers list then print
    append_random_numbers(numbers, num_quantity)
    print(numbers)

    print()
    word_quantity = int(
        input("How many words would you like to add to the list: "))
    print(words)

    # add 1 word to the words list then print
    append_random_words(words)
    print(words)

    # add 3 words to the words list then print
    append_random_words(words, word_quantity)
    print(words)


def append_random_numbers(numbers_list, quantity=1):
    """ Append X amount of random numbers to a list

    Parameters: numbers_list
        A list of numbers
    Return: quantity
        The quantity of numbers added to the list, defalt is set to 1
    """
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(0, 100), 1))


def append_random_words(words_list, quantity=1):
    """ Append X amount of random words to a list

    Parameters: words_list
        A list of strings
    Return: quantity
        The quantity of words added to the list, defalt is set to 1
    """
    ran_words = ["camera", "tribute", "vegetation",
                 "loan", "smoke", "master", "chord", "case"]
    for _ in range(quantity):
        words_list.append(random.choice(ran_words))


# No one told us what this does just that we need it.
if __name__ == "__main__":
    main()

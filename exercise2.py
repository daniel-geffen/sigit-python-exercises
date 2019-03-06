"""
This module takes numbers as input from the user and prints the sum of the numbers.
It can take input in two forms: numbers one by one, or a string with all the numbers separated by commas.
"""


def sum_of_ongoing_input():
    """
    Takes input from the user as numbers one by one, with 'stop' at the end.
    :return: The sum of the numbers.
    """
    rolling_sum = 0
    print("Enter numbers to sum. Enter 'stop' to finish.")
    user_input = input()
    while user_input != "stop":
        rolling_sum += int(user_input)
        user_input = input()

    return rolling_sum


def sum_of_list_input():
    """
    Takes a list of numbers as input from the user (separated by commas).
    :return: The sum of the list.
    """
    user_list = input("Enter a list separated by commas (e.g. '1,2,3,4') ")
    sum_of_list = sum(map(int, user_list.split(",")))
    return sum_of_list


def main():
    user_selection = input("Enter 0 if you want to insert numbers one by one, 1 if you want to insert a list: ")
    sum_of_numbers = 0
    if user_selection == "0":
        sum_of_numbers = sum_of_ongoing_input()
    elif user_selection == "1":
        sum_of_numbers = sum_of_list_input()
    print(f"The sum of the numbers is {sum_of_numbers}")


if __name__ == "__main__":
    main()

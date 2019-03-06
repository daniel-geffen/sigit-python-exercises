"""
This module takes an id from the user and checks whether it is valid.
"""


def validate_id(id_to_check):
    """

    :param id_to_check: An id to check, as a string of digits.
    :return: A boolean representing whether the id is valid.
    """
    if len(id_to_check) != 9:
        return False

    sum_of_digits = 0
    for i, digit in enumerate(id_to_check):
        num_to_add = int(digit) * (i % 2 + 1)
        if num_to_add >= 10:
            num_to_add = num_to_add % 10 + num_to_add // 10  # Sum the 2 digits of the number.
        sum_of_digits += num_to_add

    return sum_of_digits % 10 == 0


def main():
    user_id = input("Enter an id: ")
    while not user_id.isnumeric():
        user_id = input("The id has to be all digits. Enter an id: ")
    print("The id is {}.".format("valid" if validate_id(user_id) else "not valid"))


if __name__ == "__main__":
    main()

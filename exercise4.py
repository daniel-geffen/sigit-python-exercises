"""
This module compresses a string inputted by the user.
"""


def compress_string(string):
    """
        Compresses strings by the following format:
        It shortens every sequence of equal characters to the character and the length of the sequence.
        Example - 'aaaa' will be compressed to 'a4'
        :param string: A string the function should compress.
        :return: A compressed string.
    """
    compressed = ""
    end_of_last_sequence = -1

    for i, ch in enumerate(string):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            compressed += ch + str(i - end_of_last_sequence)
            end_of_last_sequence = i

    return compressed


def main():
    user_input = input("Insert string to compress: ")
    print("The compressed string is: " + compress_string(user_input))


if __name__ == '__main__':
    main()

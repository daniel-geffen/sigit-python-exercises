"""
This module contains an implementation to the built in map function.
"""


def my_map(func, lst):
    """
    This is an implementation to the built in map function.
    :param func: A function to apply to every element of the list.
    :param lst: The list we should apply the function on.
    :return: A list in which every element is the result of applying the function to the element in the list.
    """
    return [func(x) for x in lst]


def main():
    # Example of using my_map
    my_lst = [1, 2, 3]
    print(my_map(lambda x: x * 2, my_lst))


if __name__ == "__main__":
    main()

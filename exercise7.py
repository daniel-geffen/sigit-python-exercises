"""
This module contains an implementation for a decorator that caches the results for the calls to the function.
It also contains a sample function to demonstrate the use of the decorator.
"""


def cache_decorator(func):
    """
    This is a decorator function that caches the results for calls to the function.
    When the function is called with new arguments, the result is saved before it is returned.
    If another call with the same arguments comes, the function is not called - the cached results are returned.
    :param func: The function to cache its calls.
    :return: The wrapper function that will be called instead of the original function.
    """
    results = {}

    def wrapper_func(*args, **kwargs):
        if args in results:
            return results[args]
        else:
            result = func(*args, **kwargs)
            results[args] = result
            return result

    return wrapper_func


@cache_decorator
def fibonacci(n):
    """
    A recursive function that calculates the nth element of the fibonacci series.
    Because of the cache decorator, many of the recursive calls aren't called, so the function is very fast.
    :param n: The index of the element requested.
    :return: The value the element requested.
    """

    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(100))  # Takes just 0.2 seconds with the decorator.

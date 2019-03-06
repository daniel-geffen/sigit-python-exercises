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

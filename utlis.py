"""utils.py - A small collection of beginner-friendly utility functions."""


def is_palindrome(s):
    """
    Check whether a string is a palindrome.

    A palindrome reads the same forwards and backwards (for example, "madam").
    The check ignores uppercase/lowercase differences, so "Madam" also counts.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    s = s.lower()
    return s == s[::-1]


def count_words(text):
    """
    Count the number of words in a piece of text.

    Words are separated by spaces (or other whitespace such as tabs
    and new lines).

    Parameters:
        text (str): The text in which to count words.

    Returns:
        int: The number of words found in the text.
    """
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Uses the formula: F = C * 9/5 + 32

    Parameters:
        c (int or float): The temperature in degrees Celsius.

    Returns:
        float: The temperature in degrees Fahrenheit.
    """
    return c * 9 / 5 + 32
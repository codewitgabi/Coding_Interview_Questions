#!/usr/bin/python

def reverse_string(string: str) -> str:
    """
    This problem was asked by Google.

    Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

    >>> print(reverse_string("Hello world here"))
    here world Hello
    """

    return " ".join(reversed(string.split()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


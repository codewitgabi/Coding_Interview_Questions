#!/usr/bin/python
import re

def reverse_maintaining_delimiters(word: str) -> str:
    """
    >>> print(reverse_maintaining_delimiters("hello/world:here"))
    here/world:hello
    >>> print(reverse_maintaining_delimiters("hello//world"))
    world//hello
    """
    delimiters: list = re.compile(r"[^a-zA-Z0-9]").findall(word)
    output: str = ""
    split_str: list = list(reversed(re.split(r"[^a-zA-Z0-9]", word)))

    for i, j in enumerate(split_str):
        if i != (len(split_str) - 1):
            output += (j + delimiters[i]);
        else:
            output += j

    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()


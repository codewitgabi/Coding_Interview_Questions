#!/usr/bin/python

def invertdict(data: dict) -> dict:
    """
    Write a function invertdict to interchange keys and values in a dictionary.
    For simplicity, assume that all values are unique.
    
    >>> print(invertdict({'x': 1, 'y': 2, 'z': 3}))
    {1: 'x', 2: 'y', 3: 'z'}
    """

    return {value: key for key, value in data.items()}


if __name__ == "__main__":
    import doctest
    doctest.testmod()



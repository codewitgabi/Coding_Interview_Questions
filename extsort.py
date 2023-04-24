#!/usr/bin/python

def extsort(arr: list) -> list:
    """
    Sorts a list of filenames by their extension

    >>> print(extsort(["a.c", "a.py", "b.py", "bar.txt", "foo.txt", "x.c"]))
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
    """
    arr.sort(key=lambda x: x.rsplit(".", 1)[1])
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()


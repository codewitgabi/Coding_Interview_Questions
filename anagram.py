#!/usr/bin/python

def anagram_indices(W: str, S: str) -> list:
    """
    Given a word W and a string S, find all starting indices in S which are anagrams of W.
    For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

    >>> print(anagram_indices("ab", "abxaba"))
    [0, 3, 4]
    """
    output: list = []
    W = "".join(sorted(W))

    # iterate S
    for i in range(len(S) - 1):
        if "".join(sorted(S[i: i + len(W)])) == W:
            output.append(i)

    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()

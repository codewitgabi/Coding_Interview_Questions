#!/usr/bin/python3

# Source: Facebook

def possible_decoding(char: str) -> int:
    """
    param: char
    type: str
    description: an encoded string to be decoded using our algorithm
    rtype: number of ways that char can be decoded

    >>> possible_decoding("111")
    3
    >>> possible_decoding("001")
    -1
    >>> possible_decoding("101")
    2
    >>> possible_decoding("1111")
    3

    """

    mapping_1 = "123456789"
    mapping_2 = "111213141516171819"
    mapping_3 = "1020212223242526"
    count = 0

    if char[0] == "0":
        return -1

    for i in mapping_1:
        if i in char:
            count += 1
            break

    for i in range(0, len(mapping_2), 2):
        if mapping_2[i: i + 2] in char:
            count += 2
            break

    for i in range(0, len(mapping_3), 2):
        if mapping_3[i: i + 2] in char:
            count += 1
            break

    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

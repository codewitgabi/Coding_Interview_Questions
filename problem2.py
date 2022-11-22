#!/usr/bin/python3

def foo(arr:list) -> list:
    prod = 1
    for num in arr:
        prod *= num

    return [prod // i for i in arr]


print(foo([1, 2, 3, 4, 5]))
print(foo([1, 2, 3]))

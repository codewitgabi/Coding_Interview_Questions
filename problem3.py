#!/usr/bin/python3

# By Stripe - Hard

def first_missing_positive_integer(arr:list) -> int:
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] >= 0:
            if arr[i] + 1 != arr[i + 1]:
                return arr[i] + 1
    return arr[-1] + 1


print(first_missing_positive_integer([3, 4, -1, 1]))
print(first_missing_positive_integer([1, 2, 0]))

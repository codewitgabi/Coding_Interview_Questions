#!/usr/bin/python3

def add_up(arr:list, k:int) -> bool:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return arr[i], arr[j];
    return -1


print(add_up([10, 15, 3, 7], 17));

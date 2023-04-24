#!/usr/bin/python
import sys

try:
    search_text = sys.argv[2]
    with open(sys.argv[1], "r") as file:
        content = [line.rstrip("\n") for line in file.readlines()]
        for line in content:
            if search_text in line:
                print(line)

except FileNotFoundError:
    print("File not found")

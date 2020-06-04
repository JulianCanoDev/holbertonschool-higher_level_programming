#!/usr/bin/python3
"""I/0 functions"""


def read_file(filename=""):
    """Read file function"""
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        print(my_file.read(), end='')
        my_file.close()

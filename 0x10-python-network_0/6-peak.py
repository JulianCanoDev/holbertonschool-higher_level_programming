#!/usr/bin/python3


def find_peak(list_of_integers):
    "find peak in a list"
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None

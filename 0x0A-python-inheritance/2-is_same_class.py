#!/usr/bin/python3
"""Check if is instance"""


def is_same_class(obj, a_class):
    """Return True if is instance or false otherwise"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

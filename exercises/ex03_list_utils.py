"""Wordle recreation with python"""

__author__ = "730812747"


def all(list: list[str], char: str) -> bool:
    """Returns True if all characters in the list are equal to char, else False."""
    if len(list) == 0:
        return False
    i: int = 0
    while i < len(list):
        if list[i] != char:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the maximum value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    max_value: int = input[0]
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
        i += 1
    return max_value


def is_equal(list1: list[str], list2: list[str]) -> bool:
    """Returns True if both lists are equal, else False."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True

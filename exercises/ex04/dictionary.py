"""Dictionary utility functions."""

__author__ = "730812747"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    result: dict[str, str] = {}
    for key in input:
        if input[key] in result:
            raise KeyError(f"Duplicate key found: {input[key]}")
        result[input[key]] = key
    return result


def count(input: list[str]) -> dict[str, int]:
    """Counts the amount of each string in a list."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most common color in a dictionary"""
    if len(input) == 0:
        raise ValueError("Input dictionary is empty")
    color_count = count(list(input.values()))
    max_color: str = ""
    max_count: int = 0
    for color in color_count:
        if color_count[color] > max_count:
            max_color = color
            max_count = color_count[color]
    return max_color


def bin_len(input: list[str]) -> dict[int, set[str]]:
    """Groups the keys of a dictionary by their length."""
    result: dict[int, set[str]] = {}
    for key in input:
        length: int = len(key)
        if length not in result:
            result[length] = {key}
        else:
            result[length].add(key)
    return result

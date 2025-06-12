"""Dictionary test functions."""

__author__ = "730812747"

import pytest
from exercises.ex04.dictionary import invert, count, favorite_color, bin_len


def test_invert_empty() -> None:
    """Test invert with an empty dictionary."""
    assert invert({}) == {}


def test_invert_single() -> None:
    """Test invert with a single pair."""
    assert invert({"a": "b"}) == {"b": "a"}


def test_invert_duplicates() -> None:
    """Test invert with duplicate values."""
    with pytest.raises(KeyError):
        invert({"a": "b", "c": "b"})


def test_count_empty() -> None:
    """Test count with an empty list."""
    assert count([]) == {}


def test_count_single() -> None:
    """Test count with a single item."""
    assert count(["a"]) == {"a": 1}


def test_count_duplicates() -> None:
    """Test count with duplicate items."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_favorite_color_empty() -> None:
    """Test favorite_color with an empty dictionary."""
    with pytest.raises(ValueError):
        favorite_color({})


def test_favorite_color_single() -> None:
    """Test favorite_color with a single color."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_favorite_color_many() -> None:
    """Test favorite_color with multiple colors."""
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"
    )


def test_bin_len_empty() -> None:
    """Test bin_len with an empty dictionary."""
    assert bin_len([]) == {}


def test_bin_len_single() -> None:
    """Test bin_len with a single key."""
    assert bin_len(["a"]) == {1: {"a"}}


def test_bin_len_multiple() -> None:
    """Test bin_len with multiple keys of different lengths."""
    assert bin_len(["a", "b", "c", "d", "ef", "gh"]) == {
        1: {"a", "b", "c", "d"},
        2: {"ef", "gh"},
    }

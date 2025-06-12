"""Wordle recreation with python"""

__author__ = "730812747"


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def main(secret: str) -> None:
    """Entrypoint of the program and main game loop."""
    turns: int = 1
    won: bool = False
    while turns <= 6 and not won:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(length=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow.")


def contains_char(word: str, char: str) -> bool:
    """Returns True if char is in word, else False."""
    assert len(char) == 1, f"len('{char}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis based on the guess and secret word."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    i: int = 0
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(length: int) -> str:
    """Prompts user for a guess of a specific length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main(secret="codes")  # You can change the secret word here for testing

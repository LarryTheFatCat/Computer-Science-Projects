"""
author: Tarkan Zarrouk 
date: 04/04/2024
Lists Practice
"""


def character_to_number(char: str) -> int:
    """Returns the position of a letter in the alphabet if 'a' is 0
    Highly recommend looking into the `ord()` function

    >>> character_to_number("a")
    0
    >>> character_to_number("z")
    25
    >>> character_to_number("m")
    12
    """
    # Output
    return ord(char) - 97

def main():
    # Input
    # OG List (0)
    secret_message = ["m","e","e","t","m","e","a","t","t","h","e","m","a","i","n","f","r","a","m","e",]
    # Processing # Using list transformation 
    new_list = []
    for i in secret_message:
        new_list.append(character_to_number(i))
    # Output
    print(new_list)

if __name__ == "__main__":
    main()
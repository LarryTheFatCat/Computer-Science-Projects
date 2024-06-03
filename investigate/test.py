def count_es(text: str) -> int:
    """Count the number of 'e's in a string of text.

    >>> count_es("Can't wait for the weekend")
    3
    >>> count_es("A fifth char is not found in this string")
    0
    """
    num_es = 0  # Initialize to 0
    for letter in text:
        if letter == "e":
            num_es += 1

    return num_es

def main():
    num = count_es("Hello")
    print(num)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
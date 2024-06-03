"""
author: Tarkan Zarrouk
date: 04/24/2024
read from file output even or odd
"""


def is_even_or_odd(num: int) -> str:
    """will check whether or not integer is odd or even"""
    if int(num) % 2 == 0:
        return "Even"
    elif int(num) % 2 != 0:
        return "Odd"


def main():
    # Read in file
    # Input
    with open("numbers.txt", mode="r") as f_in:
        file = f_in.read().splitlines()

    # Loop over list and append to new list
    # Processing
    new_list = []
    for numbers in file:
        new_list.append(is_even_or_odd(int(numbers)))

    # Output
    # write to new file
    with open("numbers_tagged.txt", mode="w") as f_out:
        for i in range(len(new_list)):
            f_out.write(f"{file[i]} -> {new_list[i]}\n")


if __name__ == "__main__":
    main()

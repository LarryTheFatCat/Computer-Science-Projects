"""
author: Tarkan Zarrouk
date: 03/29/2023 [Updated 04/16/2024]
Sorting a list of names!
"""


def main():
    # Read Heads tail text

    # Input
    file_contents = []
    with open("HT.txt", mode="r") as f_in:
        file_contents = f_in.readlines()

    # Processing
    num_heads = file_contents.count("Heads\n")
    tails_count = file_contents.count("Tails\n")

    # Output
    print(f"{num_heads / tails_count:.2f}")


if __name__ == "__main__":
    main()

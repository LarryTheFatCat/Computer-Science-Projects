"""
author: Tarkan Zarrouk
date: 04/19/2024
File input practicing!
"""


def main():
    # Code here
    grades = []  # set to empty list
    
    # New list
    count = 0
    total_sum = 0

    # Input
    # what we want to do is, read in file, then add to list, take sum of list, find average
    with open("grades.txt", mode="r") as f_in:
        grades = f_in.readlines()

    # Processing
    # now, loop over, and take sum
        for line in grades:
            # Convert each line to an integer and add to the sum
            total_sum += int(line.strip())
            count += 1
    
    avg = total_sum / count

    # Output
    print(avg)


if __name__ == "__main__":
    main()

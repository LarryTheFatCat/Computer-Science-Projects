"""
author: Tarkan Zarrouk
date: 03/25/2024
Practicing with lists
"""

import random

# Input

ran_numbers = random.sample(range(1, 101), 100)
# ran_numbers = [1, 2, 5, 7, 8, 10]

# Processing

mean = 0
# TODO: Calculate the mean of ran_numbers
# Take sum of nums
sum = sum(ran_numbers)
mean = sum / len(ran_numbers)

print(mean)  # Should be 5.5

median = 0
# TODO: Calculate the median of ran_numbers
# Sort the list
ran_numbers.sort()
# Find the middle index
mid = len(ran_numbers) // 2
# If the length of the list is even
if len(ran_numbers) % 2 == 0:
    # Find the two middle numbers
    median = (ran_numbers[mid - 1] + ran_numbers[mid]) / 2
else:
    # Find the middle number
    median = ran_numbers[mid]
# Output
print(median)  # Should be 6

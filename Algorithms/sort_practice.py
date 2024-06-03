"""
author: Tarkan Zarrouk
date: 16/05/2024
Algo sorting
"""

# Input
# Processing
# Output

def bubble_sort_abs(lst: list) -> None:
    for _ in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if abs(lst[i]) > abs(lst[i + 1]):
                # Swap Variables
                lst[i], lst[i+1] = lst[i+1], lst[i]

def find_min(lst: list) -> int:
    """Return the index of the smallest element"""
    min_i = 0
    for i, min_num in enumerate(lst):
        if abs(min_num) < abs(lst[min_i]):
            min_i = i
    return min_i

def selection_sort_abs(lst: list) -> None:
    """Sort a list"""
    for j in range(len(lst)):
        min_i = find_min(lst[j:]) + j
        # Swap
        lst[j], lst[min_i] = lst[min_i], lst[j]

# Testing the functions
def main():
    lst = [8, -6, 5, 3, 0, -9]
    print(lst)

if __name__ == "__main__":
    main()

if __name__ in "__main__":
    main()
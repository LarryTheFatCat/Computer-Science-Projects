"""
author: Tarkan Zarrouk
date: 05/15/2024
Selection sort algorithm setup with example code
"""
def find_min(list:list) -> int:
    """Return the index of the smallest element 
    >>> find_min([8,6,7])
    1
    """
    min_i = 0
    for i, min_num in enumerate(list):
        if min_num < list[min_i]:
            min_i = i
    return min_i

def selection_sort(list:list) -> None:
    """Sort a list"""
    for j in range(len(list)):
        min_i = j
        for i in range(j, len(list)):
            if list[i] < list[min_i]:
                min_i = i
                # Swap
        list[j], list[min_i] = list[min_i], list[j]

def main():
	l = [8,7,6]
	selection_sort(l)
	print(l)
 
if __name__ == "__main__":
    main()

# Input
# Processing
# Output
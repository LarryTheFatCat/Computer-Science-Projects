"""
author: Tarkan Zarrouk
date: 05/15/2024
Algorithm sorting practice
"""


def name_sort(list):
    """
    Sort algorithm with bubble sort
    """
    for _ in range(len(list) - 1):
        for i in range(len(list) - 1):
            negative_pos = list[i][-1]
            if negative_pos > list[i + 1][-1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list

            

def name_b_search(haystack: list, needle):
    lo = 0
    hi = len(haystack) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        middle_number = haystack[mid]
        
        if middle_number[-1] < needle:
            lo = mid + 1
        elif middle_number[-1] > needle:
            hi = mid - 1
        else:
            return mid 
    return 1


# Input
# Processing
# Output

def main():
    names = ["John", "Alex", "Jones", "Jake"]
    sorted_names = name_sort(names)
    print(sorted_names  )
    
    print(name_b_search(sorted_names,"x"))
    
    
if __name__ == "__main__":
    main()
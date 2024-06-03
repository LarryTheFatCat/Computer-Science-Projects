"""
author: Tarkan Zarrouk
date: 05/17/2024
Binary Search algorithm implementation
"""

def binary_search(haystack:list, needle) -> int:
    """ Returns index of needle, -1 if not found """
    lo = 0
    hi = len(haystack) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if haystack[mid] < needle:
            lo = mid + 1
        elif haystack[mid] > needle:
            hi = mid - 1
        else:
            return mid
    return -1
        
def main():
    l = [2,4,6,8]
    bin = binary_search(l, 4)
    print(bin)

if __name__ == "__main__":
    main()
    
# Input
# Processing
# Output
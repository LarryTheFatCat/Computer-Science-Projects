"""
author: Tarkan Zarrouk
date: 05/10/2024
Linear Search Implementation for python
"""
import math

# Input
# Processing
# Output

def find_sqrt(index:list, needle) -> int:
    """
    Finds and returns the index of the list where the root of the needle is found
    >>> find_sqrt([1,2,3,4,5],25)
    4
    >>> find_sqrt([0,1,2,3,4,5,6,7,8,9],81)
    8
    """
    for i in range(len(index)):
        if index[i] == math.sqrt(needle):
            return i
    return -1
    
    
def main():
    i = find_sqrt([2,3,4,5,6],36)
    print(i)
    
if __name__ == "__main__":
    main()
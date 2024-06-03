"""
author: Tarkan Zarrouk
date: 05/13/2024
Bubble Sort Algo :)
"""
def bubble_sort(list:list) -> None:
    """ Proper Bubble Sort Algo """
    for _ in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                # Swap Variables
                list[i], list[i+1] = list[i+1], list[i]
                
                
def main():
    list = [8,7,6,5,3,0,9]
    bubble_sort(list)
    print(list)
    
if __name__ == "__main__":
    main()
    
    
# Input
# Processing
# Output
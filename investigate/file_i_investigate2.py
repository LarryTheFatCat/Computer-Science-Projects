"""
author: Tarkan Zarrouk
date: 02/04/2024
List Investigate part 2
"""

def main():
    # Open file, read and loop over and then print out each name
    # Input
    names_list = []
    # Processing
    with open("names.txt", mode="r") as f_in:
        names_list = f_in.readlines()
        
    # Output
    for names in names_list:
        print(f"Hello {names}".strip() + "!")

if __name__ == "__main__":
    main()
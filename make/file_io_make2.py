"""
author: Tarkan Zarrouk: 
date: 04/30/2024
reads in text file, outputs number of words in a story
"""

def main():
    file_contents = []
    # read in file
    # input
    with open("adventure.txt", mode="r") as f_in:
        file_contents = f_in.read().split()
        
    # processing
    # after reading in file, we want to output to file
    length = len(file_contents)
    # Output
    print(length)        
                
if __name__ == "__main__":
    main()
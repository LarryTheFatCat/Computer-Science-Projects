"""
Python Script to automatically make web dev file
"""


"""
every time this script runs, create folder that stores an index.html file that stores bootstrap contents
"""

import os

def main():
    # ask to create folder name
    folder_name = input("Enter the folder name: ")
    num_files = input("How many HTML Files Do you want to create: ")
    
    os.mkdir(folder_name)
    
    
    
if __name__ == "__name__":
    main()
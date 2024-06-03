"""
author: Your Name
date: 04/19/2024
File input practicing!
"""

def main():
    # Initialize sum and count variables
    total_sum = 0
    count = 0
    
    # Open the file and read the contents
    with open('grades.txt', 'r') as file:
        for line in file:
            # Convert each line to an integer and add to the sum
            total_sum += int(line.strip())
            count += 1
    
    # Calculate the average
    average = total_sum / count
    
    # Print out only the average value
    print(average)

if __name__ == "__main__":
    main()

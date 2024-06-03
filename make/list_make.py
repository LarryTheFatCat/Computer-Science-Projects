"""
author: Tarkan Zarrouk
date: 03/26/2024
Calculating maximum grade, minimum grade, average, and median!
"""

# Input
num_students = int(input("Enter the number of students: "))
grades = []

# Processing

# Loop to allow multiple inputs and calcs
for i in range(num_students):
    # Identify grade overall average
    average_input = int(input("Enter average of Student: "))
    grades.append(average_input)

# Identify Overall Average of class
average_of_grades = sum(grades) / len(grades)

# Identify median of list
# Set median as 0
median = 0
grades.sort()  # Sort from least to highest!
middle_odd_value = len(grades) // 2
if len(grades) % 2 == 0:
    median = (grades[middle_odd_value - 1] + grades[middle_odd_value]) / 2
else:
    median = grades[middle_odd_value]


# OUTPUT

# Identify maximum and minimum grades

# Maximum
maximum_grades = max(grades)
print(maximum_grades)

# Minimum
minimum_grades = min(grades)
print(minimum_grades)

# Print Overall Average
print(average_of_grades)

# Print Median of Class
print(median)
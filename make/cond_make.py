"""
author: Tarkan Zarrouk
date: 02/22/2024
grade checker
"""
# input
grade = int(input("Enter a number: "))


# Processing / Output
if grade < 50:
    print("Level 0")
elif grade < 60:
    print("Level 1")
elif grade < 70:
    print("Level 2")
elif grade < 80:
    print("Level 3")
else:
    print("Level 4")

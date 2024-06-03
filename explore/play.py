"""
author: {my real life name}
date: 02/06/2024
A playground for learning python
Day 2
"""

# Variables act like storage but with names
name = "Name "

# A function allows us to execute commands
# Designed to help print out arguments
print(name)

# Variables help us reduce typing time
# allowing us to set variables to refer anywhere in our code
x = 2
y = 53.88

# Basic math functions using variables
# Includes: Addition, Subtraction, Multiplication, Division, Exponent
s = x + y
d = x - y
p = x * y
q = x / y
e = y ** x

# F strings called format
# They can print out normal language and print out variables too
print(f"{x} plus {y} equals {s}")


# Test Stuff

x = 24
y = 30
z = 45
a = 27


s = x + y + z + a
d = x - y - z
p = x * y * z
q = x / y / z
e = y ** x

print(f"{x} plus {y} plus {z} plus {a} equals {s}")

# keybind for copying code down
# for example, if we repaste sum for an example
s = x + y + z + a

# Alt + Shift + Down copies it down
s = x + y + z + a
s = x + y + z + a


# Lists
# Variables above only hold one, but we can use lists
# to allow us to store a lot!

# Doing things with bare numbers (lots of numbers)
bare_numbers = [8, 6, 6, 2, 4, 7, 2]
# whenever we have a variable that has 2 spaces, we use an underscore

# Lists start at 0 and go to how many nums there exist in the list
print(bare_numbers[0])
# len = length of argument
print(len(bare_numbers))
# sum = sum of argument
print(sum(bare_numbers))

# the function list() allows us to turn turn anything into a list!
# Range allows us to generate a range of numbers
# We can use underscores to make these nums readable lol
# Range only prints one less than the original amount
# So we must add an extra 1 to get the specific amount
lots_o_n = list(range(1, 100_001))
print(lots_o_n)
print(lots_o_n[0])
print(len(lots_o_n))
print(sum(lots_o_n))
"""
1
100000
5000050000

"""

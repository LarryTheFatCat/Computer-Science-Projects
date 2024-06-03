"""
author: Tarkan Zarrouk
date: 04/02/2024
A function investigation
"""

# All functions are called (invoked) below

# Input
# Processing
# Output

"""
To sir reading this:
I wasn't sure whether or not I was supposed to place it in every spot, or just place it in like this
if a lab took place,
we both know I would know how to properly document... I'm just really lazy, so if I get a 3.7 / 3.1 that's fine
ill resubmit later
"""

# This is an example of a simple function.


def print_directions():
    """Prints the directions to get to Mr. 's mansion."""
    print("Turn left")
    print("Drive straight")
    print("Arrive @ destination")


# This is an example of a function with one parameter
def say_hello(name):
    """Greet someone

    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello {name}! Nice to meet you!")


# This is an example of a function with two parameters
def personal_info(name, age):
    """Display personal information

    Args:
        name (str): The name of the person
        age (int): The age of the person
    """
    print(f"Your name is {name} and you are {age} years old")


# This is an example of a function that returns a value
# This function also has two parameters
def add(a, b):
    """Calcluates the sum of two numbers

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        (int): The sum of the two numbers
    """
    return a + b


# This function does some more calculations, but same as the one above
# Takes in two parameters and returns a value
# For contxet, gcd = Greatest Common Divisor
def gcd(a, b):
    """Calculates the greatest common divisor between two numbers.

    The greatest common divisor is defined as the largest number that `evenly divides`
    the two numbers in question.
    Example:
        gcd(15, 5)  == 5
        gcd(10, 21) == 1

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        (int): The greatest common divisor of the two numbers.
    """
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


# Finally, this function determines whether or not an ISBN is valid
def is_valid(isbn):
    """Determines whether or not an ISBN is valid.

    Args:
        isbn (str): The ISBN in question

    Returns:
        (bool): True if the ISBN is valid, False otherwise
    """
    # Step 1: Get rid of every non numberic character in the string (the dashes)
    isbn_numbers_only = []
    for number in isbn:
        if number.isnumeric():
            isbn_numbers_only.append(int(number))

    # Step 2: Deterimine the length of the ISBN
    # These are two algorithms: Length 10 and Length 13
    if len(isbn_numbers_only) == 10:
        # Multiply each number by it's position and sum
        the_sum = 0
        for i in range(len(isbn_numbers_only)):
            the_sum += isbn_numbers_only[i] * (i + 1)

        # ISBN is valid if the sum is divisible by 11
        return the_sum % 11 == 0

    elif len(isbn_numbers_only) == 13:
        # Multiply each number by 3 if even and 1 if odd
        the_sum = 0
        for i in range(len(isbn_numbers_only)):
            if (i + len(isbn_numbers_only)) % 2 == 0:
                the_sum += isbn_numbers_only[i] * 3
            else:
                the_sum += isbn_numbers_only[i] * 1

        # ISBN is valid if this sum is divisible by 10
        return the_sum % 10 == 0
    else:
        # Not a valid ISBN
        return False

# TODO: Write two functions that compute the area and perimeter
# of a rectangle. Both functions should have two parameters (length, width)
# Call the first function calculate_area, and the second function calculate_perimeter
# The area of a rectangle is length * width
# The perimeter of a rectangle is 2 * (length + width)
# Both functions should return the calculated value


def calculate_area(length, width):
    """Calculates the area of a rectangle

    Args:
        length (int): The length of the rectangle
        width (int): The width of the rectangle

    Returns:
        (int): The area of the rectangle
    """
    return length * width


def calculate_perimeter(length, width):
    """Calculates the perimeter of a rectangle

    Args:
        length (int): The length of the rectangle
        width (int): The width of the rectangle

    Returns:
        (int): The perimeter of the rectangle
    """
    return 2 * (length + width)


def main():
    # Ignoring IPO comments for this investigation.
    # Calling all the functions in the main method
    print_directions()
    # Calling functions that have parameters with arguments
    # Parameters are the variables in the `function definition`
    # Arguments are the data passed INTO the function. This creates
    # a hidden variable
    # In say_hello(name), name is a parameter
    # in say_hello("Mr. "), "Mr. " is an argument.
    # Python makes the variable name = "Mr. " automatically when we
    # call the say_hello function.
    say_hello("Mr. ")
    personal_info("Mr. ", 27)

    # Calling functions that return values
    # Notice that functions that return values, unlike the function calls above
    # are set equal to a variable! That's important!
    the_sum = add(10, 17)
    print(the_sum)
    the_gcd = gcd(60, 15)
    print(the_gcd)

    # Different return values based off of length of ISBN
    is_valid_isbn = is_valid("0-7167-0344-0")
    print(is_valid_isbn)
    is_valid_isbn = is_valid("978-0-7167-0344-0")
    print(is_valid_isbn)
    is_valid_isbn = is_valid("978-0-7167-4-0")
    print(is_valid_isbn)

    # TODO: Call your area and perimeter methods here

    # Input
    area = calculate_area(10, 5)  # Process
    print(area)  # Output
    # Input
    perimeter = calculate_perimeter(10, 5)  # Process
    print(perimeter)  # Output


if __name__ == "__main__":
    main()

"""
author: Tarkan Zarrouk
date: 05/02/2024
Docstrings comment learning assignment
"""

def greet_teacr() -> str:
  """
  Returns Response of "Good afternoon, Mr." whenever function is called
  """
  return "Good afternoon, Mr. "


def greet_student(name:str) -> str:
  """Will return friendly greeting of a ""name"" whenever the function passes through a string in the parameters"""
  return f"Hey {name}!"


def get_temp_description(temp_outside:int) ->str:
  
  if temp_outside < 0:
    return "It's really cold"
  elif temp_outside < 15.5:
    return "It's jacket weather"
  elif temp_outside < 20:
    return "It's sweater weather"
  else:
    return"It's finally warm outside"


def add_ints(a:int, b:int) -> int:
  """
  Will take in 2 integers, and return the sum
  add_ints(2,4)
  >> 6
  add_ints(3,9)
  >> 12
  """
  return a + b


def ad_floats(a:float, b:float) -> float:
  """
  When 2 floater numbers are passed through the parameters, return sum of each
  ad_floats(2.2,3.3)
  >> 5.5
  ad_floats(1.1,1.1)
  >> 2.2 
  """
  return a + b

# Input
# Processing
# Output


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Abraham Kidanemariam
# 11/10/24
# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# This function imports the math module to use the constant pi.

import math

def areaOfCircle(r):
    """Calculates the area of a circle given the radius r."""
    return math.pi * r**2

# Testing the function
radius = 5
print(f"The area of a circle with radius {radius} is {areaOfCircle(radius)}")

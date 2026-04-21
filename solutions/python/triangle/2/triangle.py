"""
    Determine if a triangle is equilateral, isosceles or scalene
"""
def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c

def equilateral(sides):
    a, b, c = sides
    return (a == b == c) and is_triangle(sides)
    
def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and is_triangle(sides)

def scalene(sides):
    a, b, c = sides
    return (a != b and b != c and a != c) and is_triangle(sides)

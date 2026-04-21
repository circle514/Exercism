"""
    Determine if a triangle is equilateral, isosceles or scalene
"""
def is_triangle(sides):
    a, b, c = sides
    positive_length = True if a > 0 and b > 0 and c > 0 else False
    inequality = True if a + b >= c and b + c >= a and a + c >= b else False
    return positive_length and inequality

def equilateral(sides):
    a, b, c = sides
    return (a == b == c) and is_triangle(sides)
    
def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and is_triangle(sides)

def scalene(sides):
    a, b, c = sides
    return (a != b and b != c and a != c) and is_triangle(sides)

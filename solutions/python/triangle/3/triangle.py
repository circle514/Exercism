"""
    Determine if a triangle is equilateral, isosceles or scalene
"""
def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c

def equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)
    
def isosceles(sides):
    a, b, c = sides
    return len(set(sides)) <= 2 and is_triangle(sides)

def scalene(sides):
    a, b, c = sides
    return len(set(sides)) == 3 and is_triangle(sides)

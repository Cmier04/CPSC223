from math import pi

def circumference(*, radius):
    '''calculates circumference of circle'''
    try:
        return 2 * pi * radius
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")

def area(*, radius):
    '''calculates area of circle'''
    try:
        return pi * (radius ** 2)
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")

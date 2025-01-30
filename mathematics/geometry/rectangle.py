def perimeter(*, length, width):
    '''calculates the perimeter'''
    try:
        return 2 * (length + width)
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")


def area(*, length, width):
    '''calculates area'''
    try:
        return length * width
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")

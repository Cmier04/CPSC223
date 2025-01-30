def surface_area(*, side):
    '''calculates surface area'''
    try:
        return 6 * (side ** 2)
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")
def volume(*, side):
    '''calculates volume'''
    try:
        return side ** 3
    except:
        return NameError("Invalid input type")
        return TypeError("Invalid input")
        return ValueError("Invalid input")

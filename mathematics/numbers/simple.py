def addition(*, left, right):
    '''Adds two values together'''
    try:
        return left + right
    except:
        return TypeError("Invalid input")

def subtraction(*, left, right):
    '''Subtracts two values'''
    try:
        return left - right
    except:
        return TypeError("Invalid input")

def multiplication(*, left, right):
    '''Multiplies two values'''
    try:
        return left * right
    except:
        return TypeError("invalid input")

def division(*, left, right):
    '''Divides two values'''
    try:
        return left / right
    except:
        return ZeroDivisionError("Cannot Divide by zero")
        return NameError("Invalid Input")

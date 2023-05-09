import math

def divide_lbyl(x:str, y:str) -> bool:
    """
    A function that checks if the inputs are valid numbers using the LBYL approach.

    Parameters:
    x (str): The first input string to be checked.
    y (str): The second input string to be checked.

    Returns:
    bool: True if either of the inputs is not a valid number, False otherwise.
    """

    if not (x.isnumeric() or (x.startswith('-') and x[1:].isnumeric())) \
            or not (y.isnumeric() or (y.startswith('-') and y[1:].isnumeric())):
        return True
    else:
        return False

def divide_eafp(x:float, y:float) -> float:
    """
    A function that performs division of two numbers using the EAFP approach.

    Parameters:
    x (float): The numerator.
    y (float): The denominator.

    Returns:
    float: The result of dividing x by y, or positive/negative infinity if y is zero and x is positive/negative respectively.
    """

    try:
        result = x / y

    except ZeroDivisionError:
        if x >= 0:
            return math.inf
        else:
            return -math.inf

    return result

x = input("Enter the first number: ")
y = input("Enter the second number: ")

if divide_lbyl(x, y):
    print("Error: Invalid input")
else:
    x = float(x)
    y = float(y)
    result = divide_eafp(x, y)

    print("The result is:", result)
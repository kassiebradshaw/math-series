def fibonacci(n):
    """
    This function has one parameter (n).
    Function returns the nth value in the Fibonacci Series using recursion
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Function has one parameter (n),
    Function returns the nth value in the Lucas Numbers series using recursion
    """
    
    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)

def sum_series(n, x = 0,  y = 1):
    """
    Function has one required parameter (n)
    Function has 2 optional parameters (x, y)
    Required parameter determines which element in the series to print.
    Optional parameters determine the first two values for the series to be produced.
    To produce results from Fibonacci Sequence, no optional parameters needed.
    To produce results from Lucas Numbers, optional parameters (2, 1) are needed.
    Any other optional parameters will produce non-Fibonacci/Lucas numbers.
    """

    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)
    else:
        return 'These optional parameters produce neither Fibonacci nor Lucas sequence'
    

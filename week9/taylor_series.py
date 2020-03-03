# taylor_series.py
"""
The module taylor_series.py contains a function taylor(). The taylor() function estimates the value of e^x or sin(x) using a taylor series
"""
from math import factorial


def taylor_exp(x, n_terms):
    """
    The function taylor_exp() calculates the taylor series approximation of e^x
    
    input:
        x: the number you want to raise e to, float or int
        n_terms: the number of terms in the taylor series expansion, int
        
    output:
        approx: taylor series approximation, float
    """
    pass


def taylor_sin(x, n_terms):
    """
    The function taylor_sin() calculates the sine of an angle in radians using the taylor series approximation
    
    input:
        x: angle in radians, int or float
        n_terms: number of terms in the taylor series approximation, int
    output:
        appprox: sine of the angle, float
    """
    pass

def taylor(func, x, n_terms):
    """
    Performs the Taylor series expansion for either the sine of x or for Euler's number raised to x.The taylor() function returns the taylor series approximation of sin(x) or e^(x)with an optional number of terms.
    
    Input:
        - func: A string describing which function to to calculate the Taylor  series expansion of.'sin'for sine(x),'exp'for e^x)
        - x: Input argument that the function will operate on.Must be a float or an integer between -50 and 50
        - n_terms: number of terms in the Taylor Series. Must be an int greater than zero up to and including 100.Defaults to 10. Has to be an integer between 1 and 100.
    Output:
        - series_sum: equals the sum of all of the terms in the Taylor Seriesup to the number of terms specified.Will be a float.
    """
    pass
    # test to see if the function inputs are valid
    
    # test to see that 'exp' or 'sin' is entered as the function


    # test to make sure x is between -50 and 50

    # test to make sure n_terms is an integer and between 1 and 100 (including 1 and 100)

    # if the func is exp, use taylor_exp function

    # if the func is sin, use taylor_sin function



from random import randint
import math

def f(x)->int :
    """
    the -x^2 +4x +5 function
    Args:
        x : the number we send in

    Returns:
        int: the value of the function
    """
    return -(x * x) + (4*x) + 5

def monte_carlo(borne:list,number_number_of_try:int,précision:int):
    """
    use the monte-carlo method to know the integral of a function
    Args:
        borne (array): the borne of definition
        number_number_of_try (int): the sample we want to use
        précision (int) : how deep we want to precise

    """
    result = []
    a = borne[0]
    b = borne[1]
    if a>=b:
        return "borne mauvaise"
    if a < 0 :
        b = b-a
        différence = a
        a = 0
    for i in range (number_number_of_try):
        int = randint(a*précision,b*précision)
        int /= précision
        int+=différence
        int = f(int) 
        result.append(int)
    sum = math.fsum(result)
    result = ((b-a)/number_number_of_try)*sum
    print("sum = "+str(result))
    print("average = "+str((1/number_number_of_try)*sum))
    
monte_carlo([-1,5],10000000,100000000)
#sum = 35.999725366855316
#average = 5.999954227809219

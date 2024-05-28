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
    sum = 0
    a = borne[0]
    b = borne[1]
    if a>=b:
        return "borne mauvaise"
    if a < 0 :
        b = b-a
        différence = a
        a = 0
    for i in range (number_number_of_try):
        if i/10000000 in [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,58,59] :
            print(i)
        int = randint(a*précision,b*précision)
        int /= précision
        int+=différence
        int = f(int) 
        sum+=int
    result = ((b-a)/number_number_of_try)*sum
    print("sum = "+str(result))
    print("average = "+str((1/number_number_of_try)*sum))
    
monte_carlo([-1,5],600000000,100000000)
#sum = 35.99935550257958
#average = 5.9998925837632635

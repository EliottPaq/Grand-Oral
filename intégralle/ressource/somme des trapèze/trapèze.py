def f(x:float)->float :
    """
    f(x)=-x^2 +4x +5 
    Args:
        x : le nombre x

    Returns:
        int: f(x)
    """
    return -(x * x) + (4*x) + 5

def sum_trapezoid(borne:list,longueur_des_rectangle:float):
    """    
    utilise la somme des trapèze pour connaître l’intégrale d'une fonction
    Args:
        borne (array): la borne de définition de l'intégrale
        longueur_des_rectangle (float): la taille des rectangles
    """
    sum=0
    a = borne[0]
    b = borne[1]
    intervalle= b-a
    number_of_rectangle = round(intervalle/longueur_des_rectangle)
    print(number_of_rectangle)
    for i in range(number_of_rectangle):
        if i/10000000 in [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,48,49,50,51,52,53,54,55,56,58,59] :
            print(i)
        x_i = f(i*longueur_des_rectangle+a)
        x_j = f((i+1)*longueur_des_rectangle+a)
        sum += ((longueur_des_rectangle * (x_i+x_j))/2)
    print("sum = "+str(sum))    
sum_trapezoid([-1,5],0.00000001)

#sum = 36.000000000042036

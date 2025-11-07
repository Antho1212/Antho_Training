#tp machine 3
#ex1
def currency_conversion( amount : float ,taux_de_change:float) :
    """ S p e c i f i c a t i o n o f t h e f u n c t i o n
    Parameters
    ==========
    amount : amount to convert (float)
    taux_de_change :  the current taux of conversion
    Returns
    =======
    result : converted currency (float)
  
    """
    new_amount = amount*taux_de_change
    return new_amount
   
print(currency_conversion(12,1.61))
#ex2
def stamp(weight:int,normalize:bool):
    if normalize ==True and weight <=51:
        stamp_number = 1
        return stamp_number
    elif weight <= 100:
        stamp_number = 2
        return stamp_number
    elif weight <= 350:
        stamp_number = 3
        return stamp_number
    elif weight <= 1000:
        stamp_number = 5
        return stamp_number
    elif weight <= 2000:
        stamp_number = 7
        return stamp_number
print(stamp(67,True))
#ex3
def is_even(n:int):
    """
    this function is use to know ifa number is even or odd
     parameters
     ----------
     n: the number you want to know if he is odd or even
     result
     ------
     true or false
     true: even
     false: odd
    """
    if n % 2 == 0:
        return True
    else:
        return False
    
testeven = is_even(25)
if testeven:
    print('Ce nombre est pair')
else:
    print('Ce nombre est impair')
    
print(is_even(15))
#ex4
def max(x:int,y:int):
    """
    get the maximum of two intergers
    parametes
    ---------
    x : number 1
    y : number 2
    result
    ------
    maxi : the maximun of the 2
    """
    if x < y:
        return y
    else:
        return x
def min(x:int,y:int):
    """
    get the minimum of two intergers
    parametes
    ---------
    x : number 1
    y : number 2
    result
    ------
    mini : the minimun of the 2
    """
    if x < y:
        return x
    else:
        return y
    
def maximun(x:int,y:int,z:int):
    """get the maximun of three integers
    parameter
    ---------
        x (int): integers 1
        y (int): integers 2
        z (int): integers 3
    result
    max: the max:int
    """
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
    
def minimun(x:int,y:int,z:int):
    """get the minimun of three integers
    parameter
    ---------
        x (int): integers 1
        y (int): integers 2
        z (int): integers 3
    result
    min: the min:int
    """
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z 
    
#ex5



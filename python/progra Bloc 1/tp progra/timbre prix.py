def timb_unity_price():
    """Specification of the function
    
    the function is use ,for now the unity of timb of a package for the post office and also the price 
    depend on the weight and the normalization
    Parameters
    -----------
    weight : weight of the package
    normalize : if the package is normalize or not
    unity : the unity of the timb you need to put
    price : the price the timb cost
    """
    weight = float(input("what is the weight of the product : \n "))
    if weight > 2000 :
        print("you cannot send the package he is too heavy")
    else :
        normalize = str(input(" is you're package normalize?,YES or NO? : \n"))
    if weight <= 50 and normalize == "YES":
        print("he cost you 0.79 euro and his unity is 1")
    elif weight <= 100:
        print("he cost you 1.58 euro and his unity is 2")
    elif weight <=350:
        print("he cost you 2.37 euro and his unity is 3") 
    elif weight <= 1000:
        print("he cost you 3.95 euro and his unity is 5")
    elif weight <= 2000:
        print("he cost you 5.53 euro and his unity is 7")
    
timb_unity_price()

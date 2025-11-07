def post(weight:float,normalize:bool):
    if normalize == False:
        if weight<=0:
            return"not negative package"
        elif weight <=100:
            return"stamp unit 2"
        elif weight <=350:
            return"stamp unit 3"
        elif weight<=1000:
            return"stamp unit 5"
        elif weight<=2000:
            return"stamp unit 7"
        else:
            return"too heavy"
    elif normalize == True and weight<=50:
        return 1 
    else:
        return "problem"

print(post(,False))




    
        
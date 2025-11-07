
def currency_conversion() :

    """ specification of the function
    this function is use for convert money , we can convert euro , dollar , yen
parpameters
----------
amount : amount to convert (float)
currency1 : currency of amount (str)
currency2 : currency of result (str)

Returns
-------
result : convert currency (float)

notes
------
use "E" for euro or "D" for dollars and Y for yen

    """
    amount = float(input("how much do you want to exchange:\n" ))
    currency_1 = str(input("what currency you have, E for euro, D for dollar and Y for yen :\n"))
    currency_2 = str(input("what currency you want, E for euro, D for dollar and Y for yen :\n"))
    if currency_1 == "E" and currency_2 == "D" :
        result = amount*1.1
    elif currency_1 == "D" and currency_2 == "E" :
        result = amount*0.91
    elif currency_1 == "E" and currency_2 == "Y" :
        result = amount*163.25 
    elif currency_1 == "D" and currency_2 == "Y" :
        result = amount*148.72
    elif currency_1 == "Y" and currency_2 == "E" :
        result = amount*0.0061
    elif currency_1 == "Y" and currency_2 == "D" :
        result = amount*0.0067
    else :
        result = ("they are problem , we can just made the transaction in euro, dolloar and yen , write E for euro, D for dollar and Y for yen")
    print(result)
    return result



currency_conversion()

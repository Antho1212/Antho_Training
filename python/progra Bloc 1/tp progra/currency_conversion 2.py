def currency_conversion(amount:float,currency:str,exchange_rate:float):
    if currency == "E":
        return amount * exchange_rate
    elif currency == "S":
        return amount/exchange_rate
    else:
        return "incorect currency"



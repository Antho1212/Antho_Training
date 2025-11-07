#ex1 
def translate_text_to_morse(text:str):
    #add dictionary
    morse = {'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-',' ':'/'}
    #translate
    result = ""
    for i in text:
        result +=morse[i] + '/'
    return result

print(translate_text_to_morse("SOS"))


print("---------------------------------------------------------------")

#ex2 
def how_many_currency(amount: int) -> list:
    currency_sizes = {500:0, 200:0, 100:0,50:0,20:0,10:0,5:0,2:0}
    for bill_size in currency_sizes:
        rest = amount % bill_size
        one_currency_amount = (amount-rest)/bill_size
        amount = rest
        currency_sizes[bill_size] += int(one_currency_amount)
    return currency_sizes

print(how_many_currency(742))

print("---------------------------------------------------------------")

#ex3


killed = ['cow', 'cow', 'dog', 'cow']

def determine_points(victim_list: list) -> int:
    """
    The function returns the amount of points used by the hunter determined by its kills

    Parameters
    ----------
    victim_list : the list of killed things (list)

    Returns
    -------
    result: the amount of points used by the hunter (int)
    """
    points = 0
    victim_value = {'chicken': 10,
                    'dog': 30,
                    'cow': 50,
                    'human': 80}

    for victim in victim_list:
        points += victim_value[victim]

    return points

def determine_cost(victim_list: list) -> int:
    """
    The function returns the amount of money used by the hunter to perform the given hunt

    Parameters
    ----------
    victim_list : the list of killed things (list)

    Returns
    -------
    result: the amount of money used by the hunter (int)
    """

    points = determine_points(victim_list)
    money = 0

    modulo100 = points % 100
    amount_100points = points + (100 - modulo100)
    permit_amount = amount_100points / 100

    money += ((permit_amount - 1 ) * 200)

    if money < 0:
        money = 0

    return int(money)

killed = []

print("You will have to pay %d euros" % determine_cost(killed))

print("-----------------------------------------------------------------")

#ex4
def dna_true(dna_sequence:list) -> bool:
    """
    return if a dna sequence is correct or no
    
    parameters
    ----------
    dna_sequences: the dna sequence you want to analyse(list)

    returns
    -------
    true or false: depend on the dna is correct or not
    """
    dna_list = {'A','T','C','G'}
    for i in dna_sequence:
        if i not in dna_list:
            return False
    return True

a = dna_true(['A','B'])
print(a)


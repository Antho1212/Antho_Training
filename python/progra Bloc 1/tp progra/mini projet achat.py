# purchase creature
from gaming_tools import * 

def purchase(price:int):
    """ used to give a price to a creature and depending on the chosen price we get a random strenght and life

    parameters
    ----------
    price : the chosen price to buy a creature(int)

    result
    ------
    purchase successful
    """
# player and creature existence
    if not gt.player_exists(username):
       print("username do not exist")
        
    if gt.has_creature(username):
       print ("username can not buy another creature")
# buy a creature
    money = gt.get_player_money(username)
    if money>0 and money >= price :
        print ("can buy a creature")
        gt.get_creature_strenght == randint(1,price)
        gt.get_creature_life(creature)== randint(1,price)
        print(randint(1,price))
    else :
        print ("can not buy a creature")
# the player creature
    creature = gt.get_random_creature_name()  
    variety = gt.get_random_creature_variety()
    strenght = gt.get_creature_strenght(creature)
    life = gt.get_creature_life(creature)
    username = new_account(username)

    set_creature(username, creature, variety, strenght, life)
    if gt.player_exists(username) and gt.has_creature(username) and gt.get_creature_variety(creature) and gt.get_creature_strenght(creature) and gt.get_creature_life(creature):
        print("success")
    else :
      print("fail")
from gaming_tools import *
from random import *
def capture(player:str):
    """atempt to capture a monster using credits 
    
    Parameters 
    ----------
    
    credits : the available number of credits used to capture a monster. 

    returns 
    ---------

    A message saying if the player captured a monster or not. (str)
    """
    get_player_money()
    if credits >= 50 :
       credits -= 50 
       chance =  randint(1,4)
       if chance == 1:
           get_random_creature_name()
           get_random_creature_variety()
           get_creature_strength()
           get_creature_life()
           set_creature()
       else:
           return "capture fail"    
    else:
        return "you don't have enought credit, you need 50 credits"
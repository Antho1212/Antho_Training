import gaming_tool
#fonction pour vendre une creature (je sais qu'il y a beaucoup à corriger)
def sell_creature (creature_strength:int, creature_life:int, player_credits:int, player_own_creature:bool):
    """ the function is used to sell a creature and get the credits
    parameters
    ---------------
    creature_strength : The strength of the creature (int)

    creature_life : The life of the creature (int)

    player_credits: current credits of the creature (int)

    player_has_creature: The existence of the creature (bool)

    price_creature_sold: The price of the creature (float)
   
    return
    --------------
   sell creature and get credits
    ----------
    """
    if player_has_creature == True
    #Calculate the price of creature sold
    price_creature_sold = (creature_strength + creature_life)/2
    #add the amount to players credits
    player_credits += price_creature_sold
        print ("the creature is sold for {price_creature_sold} credits and the player currently owns {player_credits} credits")
    else :
        print ('the player does not own creature')
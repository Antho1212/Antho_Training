from gaming_tools import *
def combat(player_1:str,player_2:str):
    """the function is use for make a fight with another player,
    the two player's creature fight and lose some life,
    the life the creature lose depend on the strenght of the opponent,
    if a creature doesn't have life after he will died,
    the variety of the creature also have matters 
    fire is better than plant, plant better than water and water better than fire
    if the player have type advantage is strenght is double,
    is the player have type disadventage is credits win is double
    the player win 50 credit if he win, 10 credits if he draw and 0 credits if he lose.

    parameters
    ----------
    player_1 : the name of the first player
    player_2 : the name of the second player
    
    returns
    -------
    credits:the number of credits win
    new_life:the new amounts of life
    """
    
    player_exists(player_1 and player_2)
    if player_exists() == False:
        return print("the player don't exists please check the name of the player")

    has_creature(player_1 and player_2)
    if has_creature == False:
       return print("can't fight every player need a creature")
    
    if variety == fire and plant or plant and water or water and fire:
        strength*2

    
    get_creature_life()
    get_creature_strength()
    get_creature_variety()


    set_creature_life()
    creature_1_life - creature_2_strength
    creature_2_life - creature__strength
    
    if variety == fire and plant or plant and water or water and fire:
        credits*2
    
    if creature_1_life > creature_2_life:
        return credits +=50
    elif creature_1_life = creature_2_life:
        return credits +=10
    else :
        return credits +=0

   



    

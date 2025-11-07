from gaming_tools import *
from random import *
#Function that creates a new player account
def new_account(username: str):
    """Creates a new account for a new player

    Parameters
    ----------
    username : player name (str)

    Returns
    -------
    None

    Raises
    ------
    ValueError : if username already exists
    
    Notes
    -----
    Verifies if the username already exists, if not, it adds the new username of the player and gives him 225 credits. 
    If yes, the username already exists and the player needs to change it.


    """
    #Verification of the player username existence and setting up new username
    if not player_exists(username):
        add_new_player(username)
    
    else:
        return print("Username already exists. Please choose another username")
    #Introduction text
    print("Hello %s,\n welcome to Monsters, the Pokemon-inspired game that's going to blow your mind!"
           "\n First of all, let's introduce you to this world rules:"
           "\n 1. You can have one monster at a time" 
           "\n 2. Once his health drops to 0 it dies" 
           "\n 3. You can buy, capture and sell monsters" 
           "\n 4. The currency in this world are credits. As a new player, the game gives you 225 credits to start with" 
           "\n 5. You can fight other players to win credits" 
           "\n That's all for the rules, we hope that you will enjoy Monsters!" %(username))
    
    #Sets the player money
    set_player_money(username, 225)
    player_credits = get_player_money(username)
    print("%s now has %d credits." %(username,player_credits))


#Function that capture a creature
def capture(username:str):
    """Attempt to capture a monster using credits 

    Parameters 
    ----------

    username : The player's name (str)
    

    Returns 
    ---------
    None
    
    Notes
    -------
    Capture a creature for the player : 
    Verifies that player doesn't already have a creature, if he does not, it will check if the player has enough credits to do this action. 
    If he does, he will get 25% chance to get a random creature,  variety, life between (1,200) and strength (1,200) and he will sucessfully get his creature.
    If not, he will not get a creature. 
    """
    #Verification if the player has a creature or not
    if has_creature(username): 
        return print("You already have a creature.")

    #Capture of the creature
    credits = get_player_money(username)
    if credits >= 50 :
     set_player_money(username,get_player_money(username)-50)
     if randint(1,4) == 1:
           creature_name = get_random_creature_name()
           creature_variety = get_random_creature_variety()
           creature_strength = randint(1,200) 
           creature_life = randint(1,200)

           set_creature(username, creature_name, creature_variety, creature_strength, creature_life)


           return print("You successfully captured  %s of variety %s with %d strength and %d life. You now have %d credits." % (creature_name, creature_variety, creature_strength, creature_life, get_player_money(username)))

     else : 
        return print("Capture failed (You now have %d credits.), you maybe gonna have more luck next time. :] "%(get_player_money(username)))
    else :
     print("You don't have enough credits to capture a monster")
    

#Function that purchase a creature
def purchase(price:int , username: str):
    """ used to give a price to a creature and depending on the chosen price we get a random strength and life

    Parameters
    ----------
    price : the chosen price to buy a creature(int)
    username : the name of the player (str) 

    Returns
    -------
    result : if the purchase was a success or not 

    Result
    ------
    purchase successful

    Notes
    -----
    The strength and life of the creature is defined between 1 and the price the player is willing to pay. 

    """
    money = get_player_money(username)
    # player and creature existence
    if not player_exists(username):
       return print("Username do not exist")
        
    elif has_creature(username):
       return print ("%s cannot buy another creature" %(username))
    
    # buy a creature
    elif money>0 and money >= price :
        print ("Can buy a creature")

        creature = get_random_creature_name()  
        variety = get_random_creature_variety()
        strength = randint(1,price)
        life = randint(1,price)
    
        set_creature(username, creature, variety, strength, life)
        set_player_money(username, money - price)
        return print("Successfully purchased %s for %d credits. Your creature has %d strength and %d life. Variety : %s." %(creature, price, strength, life, variety))
    else :
        return print ("Cannot buy a creature")
    

#Function that sells the creature
def sell_creature (username: str, creature: str):
    """ the function is used to sell a creature and get the credits
    parameters
    ---------------
    user : the name of the player (str)
    creature: the name of the creature for sale (str)
   
    returns
    --------------
    result : sell creature and update user credits

    """
    if not has_creature(username):
        print ('The %s does not own a creature' %(username)) 
        #Return actual credits
        get_player_money(username)

    else:
        #Obtain the strength and the life of the creature:
        creature_strength = get_creature_strength(creature)
        creature_life = get_creature_life(creature)

        #Calculate the price of creature sold
        price_creature_sold = (creature_strength + creature_life)//2

        #Bring the current user credits
        user_credits = get_player_money(username)

        #Add the amount to users credits
        user_credits += price_creature_sold
        set_player_money(username, user_credits)
        print ("The creature is sold for %d credits and the user currently owns %d credits" %(price_creature_sold, user_credits))

        #Remove creature after sale
        remove_creature(creature)
       
    
    
#Function that makes the creature of a player evolve
def evolution(creature:str):
    """develop strength and life of creature and mofifies money
    Parameters
    ----------
    creature: name of creature(str)

    Result
    ------
    life and strength are developed

    Notes
    -----
    Verifies that the player have a creature. Then we verify that the player has enough money. 
    If yes, you have 25% chance that the strength of the creature will increase, 
    and 50% chance that the creature life's will increase.
    If no, the player doesn't have enough money.

    """
    username = get_player(creature)
    money = get_player_money(username)
    
    #verification if username has creature
    if not has_creature(username):
        print("You cannot use this fonction")

    #step of evolution
    elif money >= 10 :
        life= get_creature_life(creature)
        strength = get_creature_strength(creature)
        money=money-10
        set_player_money( username,money)
        if randint(1,4) == 4 :
            strength= strength + 4
            set_creature_strength(creature, strength)
        
            
            print("%s was added 4 strength points. He now has %d" %(creature, get_creature_strength(creature)))
        else: 
            print("No strength points were added.")
        

        if randint(1,2)== 2 :
             life = life + 2
             set_creature_life(creature,life)
             print("%s was added 2 life points. He now has %d" %(creature, get_creature_life(creature)))
        else:
            print("No life points were added.")
    else: 
        return print("You don't have enough money to make this purchase.")
    

#Function that simulates a fight between two creatures
def fight(creature_1:str,creature_2:str):
    """the function is use for make a fight with another player,

    parameters
    ----------
    creature_1 : the name of the first player
    creature_2 : the name of the second player
    
    returns
    -------
    exists : if the creatures exists
    
    notes
    -----
    the two player's creature fight and lose some life,
    the life the creature lose depend on the strength of the opponent,
    if a creature doesn't have life after he will died,
    the variety of the creature also have matters 
    fire is better than plant, plant better than water and water better than fire
    if the player have type advantage is strength is double,
    is the player have type disadventage is credits win is double
    the player win 50 credit if he win, 10 credits if he draw and 0 credits if he lose.
    """
    #Verifies that te creatures exists to fight
    if creature_exists(creature_1) == False:
        return print("the creature 1 doesn't exists")
    elif creature_exists(creature_2) == False:
        return print("the creature 2 doesn't exists")

    


    username_1 = get_player(creature_1)
    username_2 = get_player(creature_2)

    creature_1_life = get_creature_life(creature_1)
    creature_2_life = get_creature_life(creature_2)
    creature_1_strength = get_creature_strength(creature_1)
    creature_2_strength = get_creature_strength(creature_2) 

    #Calculates the advantages from the type
    creature_1_variety = get_creature_variety(creature_1) 
    creature_2_variety = get_creature_variety(creature_2)
    if (creature_1_variety == "fire" and creature_2_variety == "plant") or (creature_1_variety == "plant" and creature_2_variety == "water") or (creature_1_variety == "water" and creature_2_variety == "fire"):
       creature_1_strength = creature_1_strength * 2
       advantage = "creature_1"
    elif (creature_2_variety == "fire" and creature_1_variety == "plant") or (creature_2_variety == "plant" and creature_1_variety == "water") or (creature_2_variety == "water" and creature_1_variety == "fire"):
        creature_2_strength = creature_2_strength * 2  
        advantage = "creature_2"
    else:
        advantage = None
     

    #Fight   
    new_life_creature1 =  creature_1_life - creature_2_strength  
    new_life_creature2 =  creature_2_life - creature_1_strength       
    if new_life_creature1 <= 0 : 
        new_life_creature1 = 0
    if new_life_creature2 <=0 : 
        new_life_creature2 = 0

    #Saves the new life stats
    set_creature_life(creature_1,new_life_creature1)
    set_creature_life(creature_2,new_life_creature2)
    
    #Winner of the fight
    if new_life_creature1 > new_life_creature2:
        credits = 50
        if advantage == "creature_2": 
           set_player_money(username_1,get_player_money(username_1)+(credits*2))
           print("%s is the winner of the fight and wins 100 credits!" %(username_1))

        else:
            set_player_money(username_1,get_player_money(username_1)+credits)
            print("%s is the winner of the fight and wins 50 credits!" %(username_1))

    elif new_life_creature1 < new_life_creature2:
        credits = 50
        if advantage == "creature_1": 
           set_player_money(username_2,get_player_money(username_2)+(credits*2))
           print("%s is the winner of the fight and wins 100 credits!" %(username_2))

        else:
            set_player_money(username_2,get_player_money(username_2)+credits)
            print("%s is the winner of the fight and wins 50 credits!" %(username_2))
        

    elif new_life_creature1 == new_life_creature2 :    
        credits = 10
        set_player_money(username_1,get_player_money(username_1)+credits)
        set_player_money(username_2,get_player_money(username_2)+credits)
        print("Both creatures got the same life, it's a tie. Both players get 10 credits.")
    #If a creature dies in fight
    if new_life_creature1 <= 0 :
        remove_creature(creature_1)
        new_life_creature1 = 0
        print("%s is dead." %(creature_1))
    if new_life_creature2 <= 0 :
        remove_creature(creature_2)
        new_life_creature2 = 0
        print("%s is dead." %(creature_2))



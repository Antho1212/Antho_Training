
#from structure_de_données import *
def GOTOEGG(demanded_apprentice: str):
    """apprentice will scan area and find the nearest egg"""
    #peut être mettre ça dans la boucle principal prcq pas la seule fonction qui le fait
    drakon = []
    for apprentice in apprentices:
        drakon += apprentices[apprentice]['dragons']

    # Recherche de l'œuf le plus proche
    best_one = None
    best_distance = 10000  # Distance maximale pour être sûr que tout soit plus petit

    for egg in dragons:
        x, y = dragons[egg]['position_x'], dragons[egg]['position_y']
        diff = abs(apprentices[demanded_apprentice]['position_x'] - x) + abs(apprentices[demanded_apprentice]['position_y'] - y)
        
        if (diff < best_distance) and (egg not in drakon):
            best_one = egg
            best_distance = diff

    # Coordonées de l'œuf cible
    x, y = dragons[best_one]['position_x'], dragons[best_one]['position_y']

    move(apprentices,demanded_apprentice,x,y)

def GOTOAPPRENTICE(demanded_dragon: str):
    """apprentice will scan area and find the nearest egg"""
    #peut être mettre ça dans la boucle principal prcq pas la seule fonction qui le fait
    alive_apprentice = []
    for apprentice in apprentices:
        if apprentices[apprentice]['health'] > 0:
            alive_apprentice += apprentice

    # Recherche de l'œuf le plus proche
    best_one = None
    best_distance = 10000  # Distance maximale pour être sûr que tout soit plus petit

    for apprentice in apprentices:
        x, y = apprentices[apprentice]['position_x'], apprentices[apprentice]['position_y']
        diff = abs(dragons[demanded_dragon]['position_x'] - x) + abs(dragons[demanded_dragon]['position_y'] - y)
        
        if (diff < best_distance) and (apprentice not in alive_apprentice):
            best_one = apprentice
            best_distance = diff

    # Coordonées de l'œuf cible
    x, y = apprentices[best_one]['position_x'], apprentices[best_one]['position_y']
    move(dragons,demanded_dragon,x,y)

    

def move(type: dict, demanded:dict,x:int,y:int):
    if type[demanded]['position_x'] < x:
        type[demanded]['position_x'] += 1
    if type[demanded]['position_x'] > x:
        type[demanded]['position_x'] -= 1
    if type[demanded]['position_y'] < y:
        type[demanded]['position_y'] += 1                
    if type[demanded]['position_y'] > y:
        type[demanded]['position_y'] -= 1






#check si ennemie a porter de dragon et fonction attack
# et si sa faut le coup en fonction de si ya ton pote sur le chemin mais si ton attack peux éliminer un apprenti adverse
# et si il a des dragons faut faire des calcul


#rajouter des valeurs de coup?
#en gros on se dirige vers de la simulation on pourrait voir les best?

def in_attack_range(apprentices: dict, dragons: dict, dragon: str, directions = None) -> list:   
    """
 
    Check if the enemy is in the range of attack.

    Parameters
    ----------
    apprentices (dict): Data about apprentices.
    dragons (dict): Data about dragons.
    dragon (str): The name of the dragon for which enemies in range are checked.
    directions (str or list or None): the direction you want to check, if None check all the directions.
    Returns
    -------
    people_in_range (list): List of entity names within the attack range of the dragon.

    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    Implementation: Anthony Goffin (v.1 - 30/03/2025)
    Implementation: Anthony Goffin (v.2 - 06/04/2025)
    """
 

    people_on_range = []  # Initialization of the list with the people in the range
    x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]  # Get the position of the dragon
    range_attack = dragons[dragon]["range"]  # Get the range of the dragon
    
    if directions is None:  # If there is no direction, check all directions
        directions = ["N", "E", "W", "S", "NW", "NE", "SW", "SE"]  # All directions
    elif type(directions) == str:  # If the direction is a string, convert it to a list for iteration in the next step
        directions = [directions]


    for direction in directions:  # Check for every direction
        for x in range(1, range_attack + 1):  # Check the tile in range
            if direction == 'S':                    
                attack = (x_dragon, y_dragon + x)
            elif direction == 'N':
                attack = (x_dragon, y_dragon - x)
            elif direction == 'E':
                attack = (x_dragon + x, y_dragon)
            elif direction == 'W':
                attack = (x_dragon - x, y_dragon)
            elif direction == 'SE':
                attack = (x_dragon + x, y_dragon + x)
            elif direction == 'SW':
                attack = (x_dragon - x, y_dragon + x)
            elif direction == 'NE':
                attack = (x_dragon + x, y_dragon - x)
            elif direction == 'NW':
                attack = (x_dragon - x, y_dragon - x)

            x_attack, y_attack = attack  # Coordinates of the attack

            if count_entity_on_case(x_attack, y_attack):  # Check if there is someone on the case
                for apprentice in apprentices:  # For every apprentice get his coordinates
                    x_apprentice, y_apprentice = apprentices[apprentice]["position_x"], apprentices[apprentice]["position_y"]
                    if (x_apprentice == x_attack) and (y_apprentice == y_attack) and (apprentice not in people_on_range):
                        people_on_range.append(apprentice)  # If they are on the attack coordinates and not in the list, add them
                
                for other_dragon in dragons:  # Same for the dragons
                    x_other_dragon, y_other_dragon = dragons[other_dragon]["position_x"], dragons[other_dragon]["position_y"]
                    if (x_other_dragon == x_attack) and (y_other_dragon == y_attack) and (other_dragon not in people_on_range):
                        people_on_range.append(other_dragon)

    return people_on_range

                        

#def in_attack_range_directional(direction: str, apprentices: dict, dragons: dict, dragon:str)-> list:
    """ check if the ennemi is in range of attack
    
    paramaters
    ----------
    apprentices (dict): data about dragons
    dragons (dict): data about dragons
    direction (str): the direction of the attack
    dragon (str): the name of the dragon the ennemies in is range is check
    returns
    -------
    people_on_range_directional (list) : list with the entities's name in the attack range of the dragons in a specific direction
    
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 30/03/2025)
    implementation: Anthony Goffin (v.1 - 30/03/2025)
    """
    people_on_range_directional = []                   #initialize a list with the name of entity in the range od the dragon
    x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]   #get the postition of the dragon
    range_attack = dragons[dragon]["range"]                                             #get the range of the dragon
    for x in range(1, range_attack + 1):                     #check for the range
        if direction   ==  'S':                    
            attack = (x_dragon, y_dragon + x)
        elif direction == 'N':
            attack = (x_dragon, y_dragon - x)
        elif direction == 'E':
            attack = (x_dragon + x, y_dragon)
        elif direction == 'W':
            attack = (x_dragon - x, y_dragon)
        elif direction == 'SE':
            attack = (x_dragon + x, y_dragon + x)
        elif direction == 'SW':
            attack = (x_dragon - x, y_dragon + x)
        elif direction == 'NE':
            attack = (x_dragon + x, y_dragon - x)
        elif direction == 'NW':
            attack = (x_dragon - x, y_dragon - x)
             
        x_attack, y_attack = attack             #the coordonate of the attack
        if count_entity_on_case(x_attack, y_attack):          #check if they are someone on a tile 
            for apprentice in apprentices:             
                x_apprentice, y_apprentice = apprentices[apprentice]["position_x"], apprentices[apprentice]["position_y"]   #get postion of apprentice
                if (x_apprentice == x_attack) and (y_apprentice == y_attack) and (apprentice not in people_on_range_directional):   #if attack position and apprentice position is the same and apprentice not already in the list add them
                    people_on_range_directional.append(apprentice)  
            for other_dragon in dragons:   #do the same for the dragon
                x_other_dragon, y_other_dragon = dragons[other_dragon]["position_x"], dragons[other_dragon]["position_y"]
                if (x_other_dragon == x_attack) and (y_other_dragon == y_attack) and (other_dragon not in people_on_range_directional):
                    people_on_range_directional.append(other_dragon)

    return people_on_range_directional                     


def attack_order(apprentices:dict, dragons:dict)->str:    #retourner ce qu'il faut en str
    """make the order to attack a entity
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    """

    
def attack_is_good(apprentices:dict, dragons: dict):   #analyse si un coup est bon calcul de la value, nombre d'ennemie, nombre de pote                                      
    """analyse if it's useful to attack a entity          #si on va achever quelqu'un un ennemie bonus un pote malus,
    parameters                                             #pensez a check le nombre de dragons associer aux apprentie et dragons
    ----------                                             #voir la puissance avec sacha
    apprentices (dict): data about dragons
    dragons (dict): data about dragons
    returns
    -------
    bool: return True if attack is a good tactic otherwise false
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    """
    value = 0
    in_range = []
    in_range = in_attack_range()
    
    
    
def choose_good_dragons(dragons)-> tuple:
    """
    sort dragons by power
    Notes:
    ------------
    take the best one with this method:
    ***
    best_list = choose_good_dragons()
    best_dragon = best_list[0]
    ***
    """
    
    old_statistor = 0
    dragons_stats_list = []
    for dragon in dragons:
        
        drag = dragons[dragon]
        drag_health = drag['health']
        drag_attack = drag['attack']
        drag_range = drag['range']
        drag_regen = drag['regen']
        
        # mise en place de coefficient pour choisir le meilleur dragon
        statistor = drag_health*2 + drag_attack*3 + drag_range + drag_regen
        
        
        dragons_stats_list += [(dragon, drag, statistor)]
    
    
    return sorted(dragons_stats_list,key= lambda x: x[2],reverse=True) 
# Exemple de structure de données
"""dragons = {
    'Sacha': {'health': 100, 'attack': 50, 'range': 10, 'regen': 5},
    'Tina': {'health': 80, 'attack': 60, 'range': 12, 'regen': 4}
}

#apprentices = {
    'Lea': {'dragons': ['Sacha']},
    'Alya': {'dragons': ['Tina']},
    'Carl': {'dragons': ['Sacha', 'Tina']}
}
"""
def targets_attack(apprentices: dict, dragons: dict) -> dict:
    """Assign the value of each apprentice based on their dragons and return a dictionary and a sorted list.
    
    Parameters
    ----------
    apprentices (dict): Data about the apprentices.
    dragons (dict): Data about the dragons.
    
    Returns
    -------
    targets_value (dict): Dictionary containing the value of each apprentice and dragon.
    sorted_targets (dict): Sorted dictionary of apprentices based on their values, from highest to lowest.
    
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    Implementation: Anthony Goffin (v.1 - 06/04/2025)
    """
    targets_value = {}  # Initialization of the target values dictionary
    dragons_value = choose_good_dragons(dragons)  # Get the sorted list of dragons

    for apprentice in apprentices:  # For each apprentice, calculate their value based on their dragons
        apprentice_value = 0  # Initialize the apprentice's value
        for dragon in apprentices[apprentice]["dragons"]:  # Check for the apprentice's dragons
            for dragon_name, drag, dragon_value in dragons_value:  # For each dragon in the sorted dragon list
                if dragon_name == dragon:  # If the dragon name matches
                    apprentice_value += dragon_value  # Add the dragon's value to the apprentice's value

        targets_value[apprentice] = apprentice_value  # Add the apprentice's value to the dictionary

    # Sort the dictionary by values, from highest to lowest
    sorted_targets = dict(sorted(targets_value.items(), key=lambda x: x[1], reverse=True))
    
    return targets_value, sorted_targets  # Return the dictionary of target values and the sorted dictionary

def get_direction(apprentices: dict, dragons: dict, base_entity: str, search_entity: str) -> str:
    """Used to get the direction of somebody
    Parameters
    ----------
    dragons (dict): data about dragons
    apprentices (dict): data about apprentices
    base_entity (str): the entity, who is the base for searching the direction
    search_entity (str): the entity you want to know the direction of
    Returns
    -------
    direction (str): the direction of the target
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 07/04/2025)
    Implementation: Anthony Goffin (v.1 - 07/04/2025)
    """
    # Get the position of the base entity
    if base_entity in apprentices:  # Check in the apprentices dict if it's an apprentice, dragons otherwise
        x_base, y_base = apprentices[base_entity]["position_x"], apprentices[base_entity]["position_y"]
    elif base_entity in dragons:
        x_base, y_base = dragons[base_entity]["position_x"], dragons[base_entity]["position_y"]
    
    # Get the position of the search entity
    if search_entity in apprentices:
        x_search, y_search = apprentices[search_entity]["position_x"], apprentices[search_entity]["position_y"]
    elif search_entity in dragons:
        x_search, y_search = dragons[search_entity]["position_x"], dragons[search_entity]["position_y"]
    
    # Calculate the distance between the two entities
    x_value = x_search - x_base
    y_value = y_search - y_base

    #give the direction
    if x_value == 0 and y_value > 0:
        return "N"
    elif x_value == 0 and y_value < 0:
        return "S"
    elif x_value > 0 and y_value == 0:
        return "E"
    elif x_value < 0 and y_value == 0:
        return "W"
    #give the direction if the direction is a diagonal
    if abs(x_value) == abs(y_value):  #condition for only have perfect diagonale, if you move 1 on x you must move 1 on y
        if x_value > 0 and y_value > 0:
            return "NE"
        elif x_value > 0 and y_value < 0:
            return "NW"
        elif x_value < 0 and y_value > 0:
            return "SE"
        elif x_value < 0 and y_value < 0:
            return "SW"
def time_to_attack(apprentice: dict, dragons: dict):  #si tes plus fort que l'adversaire si ya un gars de valeur isoler ect en gros saute 
    """analyse who attack and when depend on many factor
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    """ 
def ia_attack_phase(apprentice: dict, dragons: dict)->str: #reprend tout #attention ya plusieurs ordre elle doit effectuer tout les ordres worth it
    """regroup all the IA attack function, use for analyse who attack when
    and if a attack is worst or not and return the order to do
    parameters
    ----------
    
    returns
    -------
    order_attack (str)
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)

    """
    
    #note annexe ne jamais attacker si inutile regen > attack et ne pas prendre en compte si une attack est inférieur a notre regen
    #parcontre attention attaque combiner

def attack(in_attack_range, apprentices, dragons, base_entity):
    """Attack of the AI
    Parameters
    ----------
    in_attack_range (list): list of enemies in range
    apprentices (dict): data about apprentices
    dragons (dict): data about dragons
    base_entity (str): the entity that wants to attack
    Returns
    -------
    str: the direction of the attack if there's a target, else None
    """
    if in_attack_range:
        target = in_attack_range[0]  # Choisit la première cible (tu peux améliorer ça)
        msg = get_direction(apprentices, dragons, base_entity, target)
        return msg
    return None
def movement_phase(apprentices: dict, dragons: dict, order_mouvement: dict) -> tuple[dict, dict]:
    """Use for the displacement of the entity in one case around them.
    Parameters:
    ------------
    apprentices: data about the apprentices (dict)
    dragons: data about the dragons (dict)
    order: the order of the players (str)
    Return:
    -------
    apprentices: the new data about the apprentices, after their movement (dict)
    dragons: the new data about the dragons, after their movement (dict)
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 20/02/2025)
    Specification: Anthony Goffin (v.2 - 27/02/2025)
    implementation: Anthony Goffin (v.1 - 27/02/2025)
    """
    for apprentice in apprentices:                            # déplacement des apprentis
        x_apprentice, y_apprentice = apprentices['x', 'y']      # c'est pas le bon format
        if order =='N':
            y_apprentice += 1
        elif order =='S':
            y_apprentice -= 1
        elif order =='E':
            x_apprentice += 1
        elif order =='O':
            x_apprentice -= 1
        elif order =='NE':
            x_apprentice += 1
            y_apprentice += 1
        elif order =='NO':
            x_apprentice -= 1
            y_apprentice += 1
        elif order =='SE':
            x_apprentice += 1
            y_apprentice -= 1
        elif order =='SO':
            x_apprentice -= 1
            y_apprentice -= 1
        else:
            x_apprentice +=  0
            y_apprentice +=  0
        apprentices['x'] = x_apprentice
        apprentices['y'] = y_apprentice
    
    for dragon in dragons:                              
        x_dragon, y_dragon = dragons["position_x", "position_y"]
        if order =='N':
            y_dragon += 1
        elif order =='S':
            y_dragon -= 1
        elif order =='E':
            x_dragon += 1
        elif order =='O':
            x_dragon -= 1
        elif order =='NE':
            x_dragon += 1
            y_dragon += 1
        elif order =='NO':
            x_dragon -= 1
            y_dragon += 1
        elif order =='SE':
            x_dragon += 1
            y_dragon -= 1
        elif order =='SO':
            x_dragon -= 1
            y_dragon -= 1
        else:
            x_dragon +=  0
            y_dragon +=  0
        dragons["position_x", "position_y"]
    return apprentices, dragons
def dragon_attack(apprentices:dict, dragons: dict, order_attack: dict) -> tuple[dict, dict]:
    """Use for the attack of the dragons.
    Parameters:
    -----------
    apprentices: data about the apprentices (dict)
    dragons: data about the dragons (dict)
    order: the order of the players (str)
    Return:
    -------
    apprentices: the new data about the apprentices (dict)
    dragons: the new data about the dragons (dict)
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 20/02/2025)
    Specification: Anthony Goffin (v.2 - 27/02/2025)
    implementation: Anthony Goffin (v.1 - 12/03/2025)
    """
    attack_list = []                         #faudrait faire en fonction de l'ordre et non de tout les dragons

    for dragon in dragons:
        range_attack = dragons[dragon]["portée"]
        health_dragon = dragons[dragon]["health"]
        attack_dragon = dragons[dragon]["attack"]
        x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]
        
        for x in range(range_attack + 1):
        # Détermination de la position d'attaque selon l'ordre donné
            if order_attack == 'N':
                attack = (x_dragon, y_dragon + x)
            elif order_attack == 'S':
                attack = (x_dragon, y_dragon - x)
            elif order_attack == 'E':
                attack = (x_dragon + x, y_dragon)
            elif order_attack == 'O':
                attack = (x_dragon - x, y_dragon)
            elif order_attack == 'NE':
                attack = (x_dragon + x, y_dragon + x)
            elif order_attack == 'NO':
                attack = (x_dragon - x, y_dragon + x)
            elif order_attack == 'SE':
                attack = (x_dragon + x, y_dragon - x)
            elif order_attack == 'SO':
                attack = (x_dragon - x, y_dragon - x)
            else:
                attack = (x_dragon, y_dragon)  # Si l'ordre est invalide, le dragon n'attaque pas

            attack_list.append(attack)

    for x_attack, y_attack in attack_list:
        if check_people_on_case(x_attack, y_attack) == True:              #voir possible avec fonction sacha optimisation
            for apprentice in apprentices:
                x_apprentice, y_apprentice = apprentices[apprentice]["x"], apprentices[apprentice]["y"]
                if x_apprentice == x_attack and y_apprentice == y_attack:
                    apprentices[apprentice]["health"] -= attack_dragon
                    if apprentices[apprentice]["health"] < 0:
                        del apprentices[apprentice]

            for dragon in dragons:
                x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]
                if x_dragon == x_attack and y_dragon == y_attack:
                    dragons[dragon]["health"] -= attack_dragon
                    if dragons[dragon]["health"] < 0:
                        del dragons[dragon]

    return apprentices, dragons
                        
def show_last_turn(column: int,décalX: int, data: str) -> None:
    """ show the information about the last turn on the screen
    Parameters:
    -----------
    décalX: use it to move the text on the x axes
    column: column of the case (int)
    last_turn: data about last turn (dict)
    Return:
    -------
    None -> the function does not return anything, only display information
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 22/2/2025)
    """
    #chaque action faite dans une fonctions, la stock dans un dict qui est afficher
def order() -> dict:
    """Asks the player to input an order and categorizes the order into different dictionaries.
    Parameters:
    -----------
    None
    Returns:
    --------
    attack_order: the different orders of attack (dict)
    movement_order: the different orders of movement (dict)

    Version:
    --------
    Specification: Anthony Goffin (v.1 - 06/03/2025)
    Implementation: Mohamed Boukhatem (v.1 - 06/03/2025)
    """
    
def win()-> bool:
    """when a player as win the game
    parameters
    ----------
    
    Returns
    -------
    end -> true or false
    
    """
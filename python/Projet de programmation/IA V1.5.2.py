#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

from remote_play import create_connection, get_remote_orders, notify_remote_orders, close_connection

no_damage_turn = 0
#other functions

import random
from blessed import Terminal
file_name = 'game_data.drk'
ui = Terminal() #simplification de l'utilisation de blessed

def make_case(ligne=3,colonne=3,décalX=0,décalY=0, color='black'): #on pourrait remplacer les émojis par des couleurs dans blessed avec on_red/black('  ')
    """create a case 
    Arguments:
    -------------------
    décalX: move the case on the x axes (int)
    décalY: move the case on the y axes (int)
    column: column of the case (int)
    color: color of the case (black or red) (str)
    Version:
    -----------------
    Spécification : Sacha Ismailov (v.1 - 22/2/2025)
    Spécification : Sacha Ismailov (v.1 - 22/2/2025)
    """
    for i in range(ligne):
        if color == 'black':
            print(ui.move_xy(décalX,décalY+i)+ ui.on_black+('  '*colonne))
        elif color == 'blue':
            print(ui.move_xy(décalX,décalY+i)+ ui.on_blue+('  '*colonne))
        elif color == 'yellow':
            print(ui.move_xy(décalX,décalY+i)+ ui.on_yellow+('  '*colonne))
        else:
            print(ui.move_xy(décalX,décalY+i)+ ui.on_red+('  '*colonne))

def makeboard(row = 5, column = 5):
    """create a chess board with make_case()
    Arguments:
    -----------------
    column: number of column (int)
    row: number of row (int)
    Version:
    -----------------
    Spécification : Sacha Ismailov (v.1 - 27/2/2025)
    implementation : Sacha Ismailov (v.1 - 27/2/2025)
    """
    #il faut encore ajouter des calcul pour que la largeur des cases et leur décalage se correspondent
    for i in range(column):
        for j in range(row):
            if (i%2 == 0 and j%2==0) or (i%2==1 and j%2==1):# le modulo sert à faire des damiers
                make_case(décalY=3*j,décalX=6*i,color='noir')
            else:# le décalage ici est en fait le 3 et le 6 donc simplement la largeur d'une case car ici x = y/2 pour pouvoir faire des carrés de 3x3 on fait réellement donc 6x3
                make_case(décalY=3*j,décalX=6*i)
            #time.sleep(0.01)
    make_case(décalY= (altars['altar_1']['position_y']-1)*3, décalX= (altars['altar_1']['position_x']-1)*6,color='blue')
    make_case(décalY= (altars['altar_2']['position_y']-1)*3, décalX= (altars['altar_2']['position_x']-1)*6,color='yellow')
    print(ui.move_down(1))#je descend juste la ligne pour laisser un espace sous le tableau la ligne est optinnel   

def show_data(column=5,player=1):
    """Check all info of the concerned player and write it next to the board
    
    Arguments:
    -------------------
    column: column of the case (int)
    player: concerned player (int)

    Specification: Sacha ismailov (v.1 26/2/2025)
    Implementation: Sacha ismailov (v.1 26/2/2025)
    """
    line = 0
    if player == 2:line+=13
    print(ui.normal)
    capacity = special_capacity[('player1')]
    print(ui.home , ui.move_xy(column*6+1,line) , 'special capacity:',capacity)
    line+=1
    for apprentice in apprentices:
        
        if player == apprentices[apprentice]['joueur']:
            
            list_of_data_apprentices = [apprentice]
            for cle in ['position_y','position_x','health','regen']:
                if apprentices[apprentice]['joueur'] == 1: print(ui.on_blue)
                else:print(ui.on_yellow)
                list_of_data_apprentices += [f'{cle}: {apprentices[apprentice][cle]}']
            
            print(ui.home , ui.move_xy(column*6+1,line) , list_of_data_apprentices)
            line += 1
            
            for dragon in apprentices[apprentice]['dragons']:
                list_of_data_dragon = [dragon]
                for cle in ['position_x','position_y','health','regen','range','attack']:
                    list_of_data_dragon += [f'{cle}: {dragons[dragon][cle]}']
                
                print(ui.home , ui.move_xy(column*6+1,line) , list_of_data_dragon)
                line+=1

def count_entity_on_case(column:int,row:int)-> list:
    """create a list of data that concern a case
    Arguments:
    -----------------
    column: column of the case (int)
    row: row of the case (int)
    Return:
    -----------
    entyty_on_case: name of the entity, genre (dragon,apprentice,egg), owner ID(list)
    Version:
    -----------------
    Spécification : Sacha Ismailov (v.1 - 27/2/2025)
    implementation : Sacha Ismailov (v.1 - 27/2/2025
    """
    entity_on_case = []
    for entity in dragons:
        if dragons[entity]['position_x'] == column and dragons[entity]['position_y'] == row:
            genre = 'egg'
            player = None
            for a in apprentices:
                
                if entity in apprentices[a]['dragons']:
                    player = apprentices[a]['joueur']
                    genre = 'dragon'
                    
            entity_on_case += [(entity,genre,player)]
            
    for entity in apprentices:
        if apprentices[entity]['position_x'] == column and apprentices[entity]['position_y'] == row:
            genre = 'apprentice'
            player = apprentices[entity]['joueur']
            entity_on_case += [(entity,genre,player)]
    
    return entity_on_case

def sort_type(y: int,x: int)->dict:
    """sort the data from count_entity_on_case() by player and genre(dragon, apprentice)
    Arguments:
    -----------------
    x: column of the case (int)
    y: row of the case (int
    Return:
    -----------
    dict: sorte(dict)
    Version:
    -----------------
    Spécification : Sacha Ismailov (v.1 - 27/2/2025)
    implementation : Sacha Ismailov (v.1 - 27/2/2025
    """
    l_ent = count_entity_on_case(y, x)
    
    dragon_count1 = 0
    apprentice_count1 = 0
    dragon_count2 = 0
    apprentice_count2 = 0
    
    for entity in l_ent:
        
        if entity[2] == 1:
            if entity[1] == 'dragon':
                dragon_count1 += 1
            elif entity[1] == 'apprentice':
                apprentice_count1 +=1
        else:
            if entity[1] == 'dragon':
                dragon_count2 += 1
            elif entity[1] == 'apprentice':
                apprentice_count2 +=1
                
    
    return {'dragon_count_1':dragon_count1,'apprentice_count_1': apprentice_count1,'dragon_count_2':dragon_count2,'apprentice_count_2': apprentice_count2}

def Board(column: int, row:int):
    """show all the entity data on the board (dragons, apprentices, eggs)
    Parameters:
    -----------
    column: number of column (int)
    row: number of row (int)
    Version:
    --------
    Specification : Sacha Ismailov (v.1 - 22/2/2024)
    Specification : Sacha Ismailov (v.2 - 27/2/2024)
    """
    makeboard(row,column)
    #ajouter le principe deplayer différencier player 1 de 2 avec un simple if sort_type(x+1,y+1)['player'] == 1 placer à gauche et un else placer à droite
    drakon = []
    entyty = []
    for i in apprentices:
        entyty += [i]
    for i in dragons:
        entyty += [i]
        
    for people in apprentices:
        drakon += apprentices[people]['dragons']

    for entity in entyty:
        if entity in apprentices: genre='apprentice'

        elif entity in drakon: genre='dragon'
        else: genre = 'egg'
        
        rowline=0
        
        
        
        #show apprentice
        if genre == 'apprentice':
            
            player1Icon='👮'
            player2Icon='🤷'
            
            x = apprentices[entity]['position_x'] -1 # -1 car python compte à partir de $zéro
            y = apprentices[entity]['position_y'] -1
            
            n_people_p1 = sort_type(x+1,y+1)['apprentice_count_1']
            n_people_p2 = sort_type(x+1,y+1)['apprentice_count_2']
            
        #show dragon
        
        elif genre == 'dragon':
            x = dragons[entity]['position_x'] -1 # -1 car python compte à partir de $zéro
            y = dragons[entity]['position_y'] -1
            player1Icon='🦖'
            player2Icon='🐉'
            rowline+=1

            n_people_p1 = sort_type(x+1,y+1)['dragon_count_1']
            n_people_p2 = sort_type(x+1,y+1)['dragon_count_2']
            
        if genre == 'egg':
            x = dragons[entity]['position_x'] -1 # -1 car python compte à partir de $zéro
            y = dragons[entity]['position_y'] -1
            player1Icon='🥚  '
            player2Icon=''
            rowline+=2
            
            n_people_p1 = ""
            n_people_p2 = ""
            
        
            
            
            
        #placer apprenti
        #utiliser people on case peut être utile pour afficher le nombre de personne
        
        if ((y%2 == 0) and (x%2==0)) or ((y%2==1) and (x%2==1)):
            
            print(ui.move_xy(6*x,3*y+rowline)+ui.on_red+ui.white+f'{get_player_display(n_people_p1, n_people_p2,player1Icon,player2Icon)}')
        else:
            print(ui.move_xy(6*x,3*y+rowline)+ui.on_black+ui.white+f'{get_player_display(n_people_p1, n_people_p2,player1Icon,player2Icon)}')
    
def get_player_display(n_player_1, n_player_2,player1Icon,player2Icon)-> str:
    """show all the entity data on the board (dragons, apprentices, eggs)
    Parameters:
    -----------
    n_player_1: number of entity that belong to player 1
    n_player_2: number of entity that belong to player 2
    player1Icon: Icon for the player 1
    player2Icon: Icon for the player 2
    Return:
    -----------
    response_str: data that must be showed in Board() (str)
    Version:
    --------
    Specification : Sacha Ismailov (v.1 - 13/3/2025)
    Specification : Sacha Ismailov (v.2 - 13/3/2025)
    """
    response_str = ""
    
    if n_player_1 == 0:
        response_str += "   "
    elif n_player_1 ==1:
        response_str += f'{player1Icon} '
    else:
        response_str += f'{player1Icon}{n_player_1}'
        
    if n_player_2 == 0:
        response_str += "   "
    elif n_player_2 ==1:
        response_str += f'{player2Icon} '
    else:
        response_str += f'{player2Icon}{n_player_2}'
        
    return response_str

def regeneration_phase():
    """restore some health to the entity that are still alive
    
    Notes:
    --------------
    point of health to restore are stocked in the data base
    to know if we can restore the health we call a dictionnary (max_lifes) created before the main loop
    Version:
    -----------------
    Spécification : Sacha Ismailov (v.1 - 20/2/2025)
    immplementation Sacha Ismailov (v.1 - 10/3/2025)
    """

    for apprentice in apprentices:
        
        pv_to_regen_a = apprentices[apprentice]['regen']
        apprentices[apprentice]['health']+=pv_to_regen_a
        
        if apprentices[apprentice]['health'] > max_lifes[apprentice]:
            apprentices[apprentice]['health'] = max_lifes[apprentice]
            
        if apprentices[apprentice]['dragons'] !=[]:
            for dragon in apprentices[apprentice]['dragons']:
                
                pv_to_regen_d = dragons[dragon]['regen']
                dragons[dragon]['health'] +=pv_to_regen_d
                if dragons[dragon]['health'] > max_lifes[dragon]:
                    dragons[dragon]['health'] = max_lifes[dragon]

def special_capacity_phase(playerID: int):
    """move all the entity that belong to the concerned player to his altars and reset the fonction compteur_de_tour()
    Parameters:
    -----------
    playerID: ID of the player (1 or 2) (int)
    apprentice: Name of the apprentices that use his capacity (str)
    Return:
    -------
    compteur_de_tour(): set to 0 for concerned player
    Version:
    --------
    Specification : Sacha Ismailov (v.1 - 20/2/2025)
    Specification : Sacha Ismailov (v.2 - 10/3/2025)
    Implementation : Sacha Ismailov (v.2 - 10/3/2025)
    """
    #regarder avec momo pour remettre la fonction quand on l'appel
    altar = altars["altar_"+str(playerID)]
    altar_x = altar['position_x']
    altar_y = altar['position_y']
    #selon moi cette fonction est inutile car fait 1 ligne
    
    if order_capacity['summon']:
        
        for apprentice in apprentices:
            if apprentices[apprentice]['joueur'] == playerID:
                apprentices[apprentice]['position_x'] = altar_x
                apprentices[apprentice]['position_y'] = altar_y
                
                if apprentices[apprentice]['dragons'] !=[]:
                    for dragon in apprentices[apprentice]['dragons']:

                        dragons[dragon]['position_x'] = altar_x
                        dragons[dragon]['position_y'] = altar_y
                        
        special_capacity['player'+str(playerID)] = False
        
        special_capacity1 = 0
        special_capacity2 = 0
        return special_capacity1,special_capacity2
        
def lecture_file(file_name):
    """read the file and return the datas

    Parameter:
    ----------
    file_name: the file in .drk (str)
    
    Return:
    -------
    map_data: information about the map (dict)
    altars: initial position for playing (dict)
    apprentices: data about the apprentices (dict)
    dragons: data about the dragons (dict)
    special_capacity: each player's special ability (bool)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 20/02/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/03/2025)
    
    """
    # Initialize dictionaries
    map_info = {}   
    altars = {}
    apprentices = {}  
    dragons = {}
    section_line= '' #string is used to collect information that is in the file
    #identifier that we subsequently increment to read each piece of information from the file in the loop
    id_altar =1
    file_path = open(file_name, 'r') #open the file in read mode
    #reading the file one line at a time
    for line in file_path:
        line = line.strip() #remove unnecessary spaces
        #links a current section of the file to one of the lines scanned
        if line == 'map:':
            section_line= 'map'
        elif line== 'altars:':
            section_line= 'altars'
        elif line== 'apprentices:':
            section_line= 'apprentices'
        elif line== 'eggs:':
            section_line= 'eggs'
        #we now go through each of the sections
        elif section_line == 'map':
            if line:
                info = line.split() #divides into several pieces of information between each space
                if len(info) == 2:
                    map_info[0] = int(info[0]) #first information in the map section returning the width
                    map_info[1] = int(info[1]) #second information in the map section returning the height
        elif section_line == 'altars':                
            if line:
                info = line.split()
                if len(info) >= 3:
                    altars[f'altar_{id_altar}'] = {
                            "joueur": int(info[0]),  #altar to which the player belongs
                            "position_x": int(info[1]),  #coordinate x of altars
                            "position_y": int(info[2])#coordinate y of altars
                        }
                    id_altar += 1
        elif section_line == 'apprentices':
            if line:
                info = line.split()
                if len(info) >= 6:
                    name= info[1] # apprentice name to easily identify the data that belongs to him
                    apprentices[name] = {
                            "joueur": int(info[0]), #The player linked with this apprentice
                            "position_x": int(info[2]), #coordinate x of apprentices
                            "position_y": int(info[3]), #coordonate y of apprentices
                            "health": int(info[4]), #health of apprentices
                            "regen": int(info[5]), #regen of apprentices
                            "name": name, #Apprentice name for access to keys, because we don't have the right to .keys()
                            "dragons": [] #Empty list for dragons linked with the apprentice
                        }
        elif section_line == 'eggs':
            if line:
                info = line.split()
                if len(info) >= 8:
                    name = info[0] #dragon name to easily identify the data that belongs to him
                    dragons[name] ={
                            "position_x": int(info[1]), #coordinate x of drgons
                            "position_y": int(info[2]), #coordinate y of drgons
                            "initialisation": int(info[3]),  #initialize data for dragons
                            "health": int(info[4]), #drgon's health
                            "attack": int(info[5]), #dragon's attack
                            "range": int(info[6]), #dragon's range
                            "regen": int(info[7]), #dragon's regen
                            "name": name, #dragon's name
                            "joueur":None
                        }
    file_path.close() #clos file after read
    special_capacity = {'player1':False, 'player2':False} #special abilities  Initialize, false this ability by default
    return map_info, altars, apprentices, dragons, special_capacity #returns the information necessary for the smooth running of the game

def egg_hatch_phase():
    """Cooldown for the egg to hatch
    
    Parameters
    ----------
    case_x : Coordinate of the case on x (int)
    case_y : Coordinate of the case on y (int)

    Return
    ------
    apprentice : The apprentice who awake the drake, and who is bound with the drake
    awake : True, the drake is awaken form the egg

    Version
    -------
    Spécification : Artemiy Gimadeev (v.1 - 20/02/25)
    Implémentation : Artemiy Gimadeev (v.1 - 02/03/25)
                    Artemiy Gimadeev (v.2 - 13/03/25)
                    Artemiy Gimadeev (v.3 - 18/03/25)
                    Sacha Ismailov (v.4 - 18/03/25)
    """
    for apprentice in apprentices:
        case_x = apprentices[apprentice]['position_x']
        case_y = apprentices[apprentice]['position_y']
            
        listmember = []
        
        
        if check_people_on_case(case_x, case_y) == True: # Check if there is more than one entity on this case

            
            for apprentice in apprentices:
                posx = apprentices[apprentice]['position_x']
                posy = apprentices[apprentice]['position_y']
                if (case_x == posx) and (case_y == posy):
                    listmember += [apprentice]
            
        
            for drake in dragons:
                posx = dragons[drake]['position_x']
                posy = dragons[drake]['position_y']
                if (case_x == posx) and (case_y == posy):
                    listmember += [drake]
            
            
            apprenticecase = listmember[0]
            drakecase = listmember[1]
            
            dragons[drakecase]['initialisation']-=1
            #on peut savoir depuis combien de temps notre dragons est réveillé grace à (abs(dragons[dragon][initialisation]))
            if dragons[drakecase]['initialisation'] == 0:
                
                apprentices[apprenticecase]['dragons'] += [drakecase]
                dragons[drakecase]['joueur'] = apprentices[apprenticecase]['joueur']

def check_people_on_case(case_x,case_y):
    """Tell if there is more than one apprentice

    Parameters
    ----------
    case_x : Coordinate of the case on x (int)
    case_y : Coordinate of the case on y (int)

    Return
    ------
    result : True or False if there is more than one apprentice
    
    Version
    -------
    Spécification : Artemiy Gimadeev (v.1 - 20/02/25)
                    Artemiy Gimadeev (v.2 - 06/03/25)
                    Artemiy Gimadeev (v.3 - 18/03/25)
    Implémentation : Artemiy Gimadeev (v.3 - 20/02/25)
                    Artemiy Gimadeev (v.2 - 06/03/25)
                    Artemiy Gimadeev (v.3 - 18/03/25)
                    Sacha Ismailov (v.4 - 18/03/25)
    """
    nb_drake = 0
    entity = 0

    for apprentice in apprentices:
            posx = apprentices[apprentice]['position_x']
            posy = apprentices[apprentice]['position_y']
            if case_x == posx and case_y == posy:
                entity += 1
    
    for drake in dragons:
        posx = dragons[drake]['position_x']
        posy = dragons[drake]['position_y']
        if case_x == posx and case_y == posy:
            nb_drake += 1
    
    if (entity == 1) and (nb_drake == 1):
        return True
    else:
        return False
    
def dragon_attack(no_damage_turn: int) -> tuple[dict, dict]:
    """Use for the attack of the dragons.
    Parameters:
    -----------
    no_damage_turn: no_damage_turn: the number of turn without damage (int)
    Return:
    -------
    apprentices: the new data about the apprentices (dict)
    dragons: the new data about the dragons (dict)
    no_damage_turn: the number of turn without damage (int)
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 20/02/2025)
    Specification: Anthony Goffin (v.2 - 27/02/2025)
    implementation: Anthony Goffin (v.1 - 12/03/2025)
    Specification: Sacha Ismailov (v.3 - 23/03/2025)
    Specification: Sacha Ismailov (v.4 - 23/03/2025)
    """
    
    attack_list = []                  
    damage = False
    
    for dragon in dragons:                        #execute the action if the dragon are in order attack
        if dragon in order_attack:                        #get the information for every dragon that have order attack
            range_attack = dragons[dragon]["range"]
            health_dragon = dragons[dragon]["health"]
            attack_dragon = dragons[dragon]["attack"]
            x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]
            direction = order_attack[dragon]            #get the information of direction of order attack
            for x in range(1, range_attack + 1):        #apply the range of the dragon, +1 for not attack where the dragon is
        
                if direction   ==  'S':                    # set attack in function of the direction
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
                
                
                
                attack_list.append((attack,  attack_dragon))    #add to attack list the attack and the attack power of dragon
                

    dragons_remove = []                         #initialize the list for the apprentices and dragons to remove
    apprentices_remove = []
    
    for (x_attack, y_attack), attack_dragon in attack_list:            #check for the coordonate of the attack in attack list and chack if they are a someone
        if count_entity_on_case(x_attack, y_attack) != []:  
                
            for apprentice in apprentices:                             #look who is on the case and decrease the health with the attack power of the dragon
                init_health = apprentices[apprentice]["health"]
                x_apprentice, y_apprentice = apprentices[apprentice]["position_x"], apprentices[apprentice]["position_y"]
                if (x_apprentice == x_attack) and (y_apprentice == y_attack):
                    apprentices[apprentice]["health"] -= attack_dragon
                    
                    
                    if apprentices[apprentice]["health"] <= 0:               #if the apprentice have no health add to apprentice remove list
                        apprentices_remove.append(apprentice)
                        for dragon in apprentices[apprentice]["dragons"]:
                            if dragon in dragons: 
                                dragons_remove.append(dragon)                #if apprentice die is dragons too, so put the dragons to remove list
                if init_health != apprentices[apprentice]["health"]:
                    damage = True                      #they are a damage so put damage on true

            for dragon in dragons:
                
                init_health = dragons[dragon]['health']                                              #same than apprentice
                x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]
                if (x_dragon == x_attack) and (y_dragon == y_attack):
                    dragons[dragon]["health"] -= attack_dragon
                    
                    if dragons[dragon]["health"] <= 0:          
                        dragons_remove.append(dragon)
                        for apprentice in apprentices:
                            if dragon in apprentices[apprentice]["dragons"]:              #this time if dragons die the apprentice lose 10 health point
                                apprentices[apprentice]["health"] -= 10
                if init_health != dragons[dragon]['health']:
                    damage = True

    #delete after the loop
    
    for apprentice in apprentices_remove:     #delete the apprentice if they are in  the apprentices list remove
        
        if apprentice in  apprentices: del apprentices[apprentice]
        
    for apprentice in apprentices:             #same for the dragon
        for dragon in dragons_remove:
            if dragon in dragons:
                del dragons[dragon]
            if dragon in apprentices[apprentice]['dragons']:             #delete dragon of the apprentices dict
                apprentices[apprentice]['dragons'].remove(dragon)
    

            
            
    #increase the value of no_damage_turn if they are no damage in the attack_phase set to zero if they are dommage.
    if damage == True:         
        no_damage_turn = 0
    else :
        no_damage_turn += 1
        
    return apprentices, dragons, no_damage_turn

def movement_phase(apprentices: dict, dragons: dict, order_mouvement: dict, map_data: dict) -> tuple[dict, dict]:
    """Use for the displacement of the entity in one case around them.
    Parameters:
    ------------
    apprentices: data about the apprentices (dict)
    dragons: data about the dragons (dict)
    order_movement: the order of the players (str)
    map_data: data about the map
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
    map_width = map_data[0]
    map_height = map_data[1]
    
    drakon = []
    for people in apprentices:     #check if it's a apprentice
        drakon += apprentices
        
    for apprentice in order_mouvement:      #check if they are a order                    
        if apprentice in drakon:
            x_apprentice, y_apprentice = apprentices[apprentice]["position_x"], apprentices[apprentice]["position_y"]   #get the information of the position of apprentice
            movement_y, movement_x = order_mouvement[apprentice]   #set the movement with the order
            calculate_direction_x = movement_x - x_apprentice            #calculate if the mouvement is 1 tiles arround
            calculate_direction_y = movement_y - y_apprentice
            if (calculate_direction_x <= 1 and calculate_direction_x >= -1) and (calculate_direction_y <= 1 and calculate_direction_y >= -1):
                new_x = x_apprentice + calculate_direction_x         #if yes set the new postion
                new_y = y_apprentice + calculate_direction_y
                if 1 <= new_x <= map_width and 1 <= new_y <= map_height:     #if the new postion is in the map set to the apprentice
                    x_apprentice = new_x
                    y_apprentice = new_y

            apprentices[apprentice]["position_x"] = x_apprentice #set in teh dict
            apprentices[apprentice]["position_y"] = y_apprentice
            
    drakon = []           #check if it's a dragon
    for people in apprentices:
        drakon += apprentices[people]['dragons']
    
    for dragon in order_mouvement:                            # exactly the same than apprentice
        if dragon in drakon:
            x_dragon, y_dragon = dragons[dragon]["position_x"], dragons[dragon]["position_y"]
            movement_y, movement_x = order_mouvement[dragon]
            calculate_direction_x = movement_x - x_dragon
            calculate_direction_y = movement_y - y_dragon
            if (calculate_direction_x <= 1 and calculate_direction_x >= -1) and (calculate_direction_y <= 1 and calculate_direction_y >= -1):
                new_x =  x_dragon + calculate_direction_x
                new_y = y_dragon + calculate_direction_y
                if 1 <= new_x <= map_width and 1 <= new_y <= map_height:
                    x_dragon = new_x
                    y_dragon = new_y

            dragons[dragon]["position_x"] = x_dragon
            dragons[dragon]["position_y"] = y_dragon
    return apprentices, dragons
 
def order(player_ID,message:str) -> dict:
    """Asks the player to input an order and categorizes the order into different dictionaries.
    Parameters:
    -----------
    player_ID: (1 or 2) player identifiant (int)
    message: orders received from the AI (str)
    Returns:
    --------
    attack_order: the different orders of attack (dict)
    movement_order: the different orders of movement (dict)
    order_capacity: the different orders of capacity (dict)

    Version:
    --------
    Specification: Anthony Goffin (v.1 - 06/03/2025)
    Specification: Mohamed Boukhatem (v.2 - 24/03/2025)
    Implementation: Mohamed Boukhatem (v.1 - 06/03/2025)
    Implementation: Mohamed Boukhatem (v.2 - 23/03/2025)
    """
    #separates different commands using spaces
    commands = message.split()
    #dictionary for each of the orders
    order_attack = {}
    order_mouvement = {}
    order_capacity= {}
    #special capacity initialized
    order_capacity['summon'] = False
    try:
        #read each command one by one
        for command in commands:
            if ':' in command:
                name, action = command.split(':') #if (':') in command, read there
                try:
                #the "try" is used to separate the commands of the dragons and the apprentices, then we check if the player is the one who gave the order
                    if (apprentices[name]['joueur'] == player_ID):
                        if action and action[0] == 'x' and action[1:] in {"N","NE", "E","SE", "S", "SW","W","NW"}: 
                            order_attack[name] = action[1:] #place the attack order
                        elif action and action[0] == '@' and '-' in action:
                            coordonnee = action[1:].split('-')  #Divide the coordinates using the (-) and do action[1:] because there are coordinates with a single letter and others with several like "NW"
                            order_mouvement[name] = (int(coordonnee[0]), int(coordonnee[1])) #place the mouvement order
                            
                except:
                    #so if he is not an apprentice, treat him like a dragon
                    if dragons[name]['joueur'] == player_ID:
                        if action and action[0] == 'x' and action[1:] in {"N","NE", "E","SE", "S", "SW","W","NW"}: 
                            order_attack[name] = action[1:]
                        elif action and action[0] == '@' and '-' in action:
                            coordonnee = action[1:].split('-')
                            order_mouvement[name] = (int(coordonnee[0]), int(coordonnee[1])) 
                            
            elif command == "summon": #if we write "summon" then we check if the ability is usable
                if special_capacity[f'player{player_ID}']:
                    order_capacity["summon"] = True #activation of the special ability after verifying that the player can use it
                else:
                    print(f'le player_{player_ID} ne peut pas utiliser la capicté spécial') #if he can we print that he cannot use it
        #return of important information for the progress of the game
        return order_attack,order_mouvement,order_capacity
    except Exception as e:
        print(f"[ERREUR] Problème dans la fonction order : {e}")
        return {}, {}, {'summon': False}

def game_finish(no_damage_turn: int)-> bool:
    """for know if the game is finish or not
    parameters
    ----------
    apprentices: data about the apprentices (dict)
    dragons: data about the dragons (dict)
    no_damage_turn: the number of turn without damage (int)
    Returns
    -------
    True if the game is finished, False otherwise.
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 17/03/2025)
    Implementation: Anthony Goffin  (v.1 - 17/03/2025)
    """
    player1_apprentice = []      #initialize the list of apprentice of the player
    player2_apprentice = []
    for apprentice in apprentices:
        if apprentices[apprentice]['joueur'] == 1:     #if the apprentice is to player 1 put on apprentice player list same if it's player 2
            player1_apprentice.append(apprentice)
        elif apprentices[apprentice]['joueur'] == 2:
            player2_apprentice.append(apprentice)
    
    if player1_apprentice == [] or player2_apprentice == []:     #if a player apprentice list is empty return true
        return True
    if no_damage_turn >= 100:           #if no damage turn is equal or more than 100 return true
        return True                     
        
    return False           #otherwise returne false

def select_player(played)->tuple:
    """select player select the player based on the turn
    Parameters:
    -----------
    played: times played
    Return:
    -----------
    played: times played
    player: player that will play
    Version:
    --------
    Specification : Sacha Ismailov (v.1 - 22/3/2025)
    Specification : Sacha Ismailov (v.2 - 22/3/2025)
    """
    if played%2 == 0:
        player = 1
    else:
        player = 2
    played+=1
    return played,player

#faut rajouter count_entity on case
def check_people_on_case(case_x,case_y):
    """Tell if there is more than one apprentice

    Parameters
    ----------
    case_x : Coordinate of the case on x (int)
    case_y : Coordinate of the case on y (int)

    Return
    ------
    result : True or False if there is more than one apprentice
    
    Version
    -------
    Spécification : Artemiy Gimadeev (v.1 - 20/02/25)
                    Artemiy Gimadeev (v.2 - 06/03/25)
                    Artemiy Gimadeev (v.3 - 18/03/25)
    Implémentation : Artemiy Gimadeev (v.3 - 20/02/25)
                    Artemiy Gimadeev (v.2 - 06/03/25)
                    Artemiy Gimadeev (v.3 - 18/03/25)
                    Sacha Ismailov (v.4 - 18/03/25)
    """
    nb_drake = 0
    entity = 0

    for apprentice in apprentices:
            posx = apprentices[apprentice]['position_x']
            posy = apprentices[apprentice]['position_y']
            if case_x == posx and case_y == posy:
                entity += 1
    
    for drake in dragons:
        posx = dragons[drake]['position_x']
        posy = dragons[drake]['position_y']
        if case_x == posx and case_y == posy:
            nb_drake += 1
    
    if (entity == 1) and (nb_drake == 1):
        return True
    else:
        return False
def choose_good_dragons()-> tuple:
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
    dragons_value = choose_good_dragons()  # Get the sorted list of dragons
    for apprentice in apprentices:  # For each apprentice, calculate their value based on their dragons
        apprentice_value = 0  # Initialize the apprentice's value
        for dragon in apprentices[apprentice]["dragons"]:  # Check for the apprentice's dragons
            if apprentices[apprentice]["joueur"] != dragons[dragon]["joueur"]:
                for dragon_name, drag, dragon_value in dragons_value:  # For each dragon in the sorted dragon list
                    if dragon_name == dragon:  # If the dragon name matches
                        apprentice_value += dragon_value  # Add the dragon's value to the apprentice's value

        targets_value[apprentice] = apprentice_value  # Add the apprentice's value to the dictionary

    # Sort the dictionary by values, from highest to lowest
    sorted_targets =list(sorted(targets_value.items(), key=lambda x: x[1], reverse=True))
    
    return targets_value, sorted_targets  # Return the dictionary of target values and the sorted dictionary

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
                for entity,genre,player in count_entity_on_case(x_attack, y_attack):
                    if not genre == 'egg':
                        if player != dragons[dragon]['joueur']:
                            people_on_range.append(entity)  # If they are on the attack coordinates and not in the list, add them
                       
    
    return people_on_range
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
        return "S"
    elif x_value == 0 and y_value < 0:
        return "N"
    elif x_value > 0 and y_value == 0:
        return "E"
    elif x_value < 0 and y_value == 0:
        return "W"
    #give the direction if the direction is a diagonal
    if abs(x_value) == abs(y_value):  #condition for only have perfect diagonale, if you move 1 on x you must move 1 on y
        if x_value > 0 and y_value > 0:
            return "SE"
        elif x_value > 0 and y_value < 0:
            return "SW"
        elif x_value < 0 and y_value > 0:
            return "NE"
        elif x_value < 0 and y_value < 0:
            return "NW"





def apprentices_to_cible(apprentices: dict, dragons: dict, oeufs_occupes: dict, player_id: int):
    """finds the target closest to the sniper

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    
    Return:
    -------
    sniper_x: coordinate of the abscisions (x) where the sniper must go (int)
    sniper_y: coordinate of the ordinates (y) where the sniper must go (int)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    """
    
    message= ""
    for sniper in apprentices:
        if apprentices[sniper]['joueur'] == player_id:
            #se dirige vers l'oeuf le plus rentable pour gagner la game
            best_oeuf = best_rentability_move(apprentices, dragons, sniper, oeufs_occupes)
            #MOUVEMENT
            #faire en sorte que sniper_x aille vers dragons[cible]['position_x']
            #faire en sorte que sniper_y aille vers dragons[cible]['position_y']
            if best_oeuf in dragons : #vérifie si le dragons est bien dans le dictionnaire des dragons
                sniper_x = apprentices[sniper]['position_x']
                sniper_y = apprentices[sniper]['position_y']
                cible_x = dragons[best_oeuf]['position_x']
                cible_y = dragons[best_oeuf]['position_y']
                new_sniper_x = int(sniper_x)
                new_sniper_y = int(sniper_y)
                if sniper_x < cible_x:
                    new_sniper_x = sniper_x + 1 
                elif sniper_x > cible_x:
                    new_sniper_x = sniper_x - 1 
                if sniper_y < cible_y:
                    new_sniper_y = sniper_y + 1
                elif sniper_y > cible_y:
                    new_sniper_y = sniper_y - 1
                    
                msg = f' {sniper}:@{new_sniper_y}-{new_sniper_x}'
                message += msg + " "
    return message

def dragons_to_cible(apprentices: dict, dragons: dict,player_id):
    """finds the target closest to the sniper

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    
    Return:
    -------
    sniper_x: coordinate of the abscisions (x) where the sniper must go (int)
    sniper_y: coordinate of the ordinates (y) where the sniper must go (int)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    """
    message= ""
    choosed_attack = targets_attack(apprentices, dragons)
    cible = choosed_attack[1][0][0]
    
    min_distance = float('inf')
    best_distance = None
    for sniper in dragons:
        if dragons[sniper]['joueur'] == player_id:
            in_range = in_attack_range(apprentices, dragons, sniper)
            if in_range ==[]:
            #  si le sniper c'est le dragon il va vers l'apprenti 
                if apprentices[cible]['joueur'] != dragons[sniper]['joueur']: #vérifie qu'il se dirige vers l'allié
                    distance = abs(dragons[sniper]['position_x'] -apprentices[cible]['position_x']) + abs(dragons[sniper]['position_y'] - apprentices[cible]['position_y'])
                    best_distance = cible
                    if distance < min_distance:
                        min_distance = distance
                        best_distance = cible
                
            #MOUVEMENT
            #faire en sorte que sniper_x aille vers dragons[cible]['position_x']
            #faire en sorte que sniper_y aille vers dragons[cible]['position_y']
            print("best_distance",best_distance)
            if best_distance :
                sniper_x = dragons[sniper]['position_x']
                sniper_y = dragons[sniper]['position_y']
                cible_x = apprentices[best_distance]['position_x']
                cible_y = apprentices[best_distance]['position_y']
                new_sniper_x = int(sniper_x)
                new_sniper_y = int(sniper_y)
                if sniper_x < cible_x:
                    new_sniper_x = sniper_x + 1 
                elif sniper_x > cible_x:
                    new_sniper_x = sniper_x - 1 
                if sniper_y < cible_y:
                    new_sniper_y = sniper_y + 1
                elif sniper_y > cible_y:
                    new_sniper_y = sniper_y - 1
                    
                msg = f' {sniper}:@{new_sniper_y}-{new_sniper_x}'
                message += msg
    return message

def best_rentability_move(apprentices: dict, dragons: dict, sniper: str, oeufs_occupes: dict):
    """the function is supposed to return the best egg to go to

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    
    Return:
    -------
    best_oeuf_target: the name of the most profitable egg to reach (str)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    """
    best_rentability = -1
    best_oeuf_target = None
    for cible in dragons:
            name = dragons[cible]["name"]
            health= dragons[cible]['health']
            attack = dragons[cible]['attack']
            range = dragons[cible]['range']
            regen = dragons[cible]['regen']
            pos_x= dragons[cible]['position_x']
            pos_y= dragons[cible]['position_y']
            joueur =dragons[cible]['joueur']
            #d'abords s"assurer que c'est bien un oeuf
            if joueur is None and (pos_x, pos_y) not in oeufs_occupes:
                distance = abs(apprentices[sniper]['position_x'] -pos_x) + abs(apprentices[sniper]['position_y'] -pos_y)
                #pour des problème de division par zéro
                if distance != 0:
                    distance = distance
                else:
                    distance = 1

                #calcule de renabilit_valeur à améliorer, valeur prise arbitrairement
                rentability_valeur = 2*health +5*attack +2*range +1*regen
                rentability = rentability_valeur/distance #explique pourquoi distance ne peut être égal à un
                if rentability > best_rentability:
                    best_rentability = rentability
                    best_oeuf_target = name
        

    return best_oeuf_target

def attack_orders(apprentices: dict, dragons: dict, player_id: int)->str:
    """give the attack order
    parameters
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    returns
    -------
    order_attack: order attack of the AI (str)
    """
    order_message = ""  # Initialize the attack order message
    target_values, sorted_targets = targets_attack(apprentices, dragons)  # Get the target priority list

    for dragon in dragons:  # Loop through each dragon
        if dragons[dragon]['joueur'] == player_id:
            in_range = in_attack_range(apprentices, dragons, dragon)  # Get enemies in attack range
            print(in_attack_range(apprentices, dragons, dragon))
            #time.sleep(1)
            if in_range:  # If there are enemies in range
                best_target = None  # Initialize the best target to None

                for target_name, target_value in sorted_targets:  # Check each target by priority
                    if target_name in in_range and best_target is None:  # If target is in range and no best target yet
                        best_target = target_name  # Set as best target
                        break  # Stop checking once a valid target is found

                if best_target is None:  # If no target was chosen
                    best_target = in_range[0]  # Default to the first in range

                direction = get_direction(apprentices, dragons, dragon, best_target)  # Determine direction to target
                order_message += f"{dragon}:x{direction} "  # Add to the attack order
    
    return order_message


def oeufs_occupes(apprentices: dict, dragons: dict) -> dict:
    """
    le code marche un peu comme sniper to cibe
    c'est simple si un oeuf et un apprenti son sur une case n'y va pas et si plusieurs apprenti se dirige vers un oeuf fait en sorte qu'un seul apprenti y aille, et aussi si plusieurs apprenti sont sur une case avec un oeufs fait les partir sauf un
    """
    occupe = {}
    positions_des_oeufs = []
    trie_oeuf = choose_good_dragons()
    # best_oeuf_value = trie_oeuf[1] #c'est la list (dragon, drg, statistor)
    for dragon in dragons:
        if dragons[dragon]['joueur'] is None:
            #j'aime pas .append
            positions_des_oeufs+=positions_des_oeufs + [(dragons[dragon]['position_x'], dragons[dragon]['position_y'])]

    for cible in dragons:
        if dragons[cible]['joueur'] is None:  #faut que ça soit un oeuf
            apprenti_sur_la_case = []
            x = dragons[cible]['position_x']
            y = dragons[cible]['position_y']
            for sniper in apprentices:
                if apprentices[sniper]['position_x'] == x and apprentices[sniper]['position_y'] == y:
                    #j'aime toujours pas .append
                    apprenti_sur_la_case = apprenti_sur_la_case + [sniper]

            if apprenti_sur_la_case:
                if len(apprenti_sur_la_case) == 1:  #si il y a un seul apprenti, verrouillé la case
                    occupe[(x, y)] = apprenti_sur_la_case[0]
                else:
                    best_oeuf = None 
                    if dragons[cible]["joueur"] is None:
                        
                        best_oeuf = None
                        best_stat = -1 #float(inf)
                        for dragon_name, drag, stat in trie_oeuf:
                            if drag["joueur"] is None and drag["position_x"] == x and drag["position_y"] == y:
                                if stat > best_stat:
                                    best_stat = stat
                                    best_oeuf = dragon_name

                    apprenti_choisi = apprenti_sur_la_case[0]
                    min_distance = float('inf')
                    for apprenti in apprenti_sur_la_case:
                        distance = abs(apprentices[apprenti]['position_x'] -dragons[best_oeuf]['position_x']) + abs(apprentices[apprenti]['position_y'] -dragons[best_oeuf]['position_y'])
                        if distance < min_distance:
                            min_distance = distance
                            apprenti_choisi = apprenti

                    occupe[(x, y)] = apprenti_choisi                              
                    for apprenti in apprenti_sur_la_case:
                        if apprenti !=apprenti_choisi:
                            distance_la_plus_proche_vers_un_oeuf = float('inf')
                            oeuf_cible = None
                            for oeuf in positions_des_oeufs:
                                if oeuf not in occupe and oeuf != (x, y):
                                    distance = abs(apprentices[apprenti]['position_x']-oeuf[0]) + abs(apprentices[apprenti]['position_y'] -oeuf[1])
                                    if distance < distance_la_plus_proche_vers_un_oeuf:
                                        distance_la_plus_proche_vers_un_oeuf = distance
                                        oeuf_cible = oeuf
                            if oeuf_cible is not None:
                                sniper_x = apprentices[apprenti]['position_x']
                                sniper_y = apprentices[apprenti]['position_y']
                                cible_x, cible_y = oeuf_cible
                                if sniper_x < cible_x:
                                    sniper_x += 1
                                elif sniper_x > cible_x:
                                    sniper_x -= 1
                                if sniper_y < cible_y:
                                    sniper_y += 1
                                elif sniper_y > cible_y:
                                    sniper_y -= 1
                                apprentices[apprenti]['position_x'] = sniper_x
                                apprentices[apprenti]['position_y'] = sniper_y
    return occupe


       
def get_AI_orders(game, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    game: game data structure (dict)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)
    """
    
    occupations_oeufs = oeufs_occupes(apprentices, dragons)
    orders = dragons_to_cible(apprentices, dragons,player_id)
    orders += apprentices_to_cible(apprentices, dragons,occupations_oeufs, player_id)
    orders += attack_orders(apprentices, dragons,player_id)
    input(orders)
    return orders
    
    


"""Play a game.

Parameters
----------
map_path: path of map file (str)
group_1: group of player 1 (int)
type_1: type of player 1 (str)
group_2: group of player 2 (int)
type_2: type of player 2 (str)

Notes
-----
Player type is either 'human', 'AI' or 'remote'.

If there is an external referee, set group id to 0 for remote player.
"""


"""
# create connection, if necessary
if type_1 == 'remote':
    connection = create_connection(group_2, group_1)
elif type_2 == 'remote':
    connection = create_connection(group_1, group_2)
"""
map_data, altars, apprentices, dragons, special_capacity = lecture_file('game_data.drk')
# main function
type_1 = ''
type_2 = 'in front of the pc'

played = 0

row = map_data[0]
col = map_data[1]
no_damage_turn = 0

#déplacement des infos pour les test
game = None

#pour regeneration_phase il me faut une liste des valeurs des HP initiaux
max_lifes = {}
for apprentice in apprentices:
    max_lifes[apprentice] = apprentices[apprentice]['health'] #on va le mettre dans lecture file ou alors je le  fait à part ? (perso plutot mettre dans lecture file, c'est plus logique)
for dragon in dragons:
    max_lifes[dragon] = dragons[dragon]['health']
    
special_capacity1 = 0
special_capacity2 = 0
connection = None

while game_finish(no_damage_turn)==False:

    
    if special_capacity2 <10:special_capacity2 +=1
    if special_capacity1< 10:special_capacity1 +=1
    if special_capacity2 == 10:special_capacity['player1'] = True
    if special_capacity1 == 10:special_capacity['player2'] = True
    
    print(ui.clear)
    show_data(col,1)
    show_data(col,2)
    Board(col,row)
    
    
    played, playerID= select_player(played) 
    # get orders of player 1 and notify them to player 2, if necessary
    print(ui.normal + ui.home + ui.move_down(row*3))
    if played%2 == 1:
        if type_1 == 'remote':
            orders = get_remote_orders(connection)
        elif type_1 == 'in front of the pc':
            orders = input(f"Tour: {played}\nJoueur {playerID}\vDonnez la commande à exécuter: ")
        else:
            print(f"Tour: {played}\nJoueur {playerID}\vDonnez la commande à exécuter: ")
            orders = get_AI_orders(None,playerID)
            #time.sleep(1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)
    else:
    # get orders of player 2 and notify them to player 1, if necessary
        if type_2 == 'remote':
            orders = get_remote_orders(connection)
        elif type_2 == 'in front of the pc':
            orders = input(f"Tour: {played}\nJoueur {playerID}\vDonnez la commande à exécuter: ")
            
        else:
            print(f"Tour: {played}\nJoueur {playerID}\vDonnez la commande à exécuter: ")
            orders = get_AI_orders(None,playerID)
            #time.sleep(1)
            if type_1 == 'remote':
                notify_remote_orders(connection, orders)     

    # close connection, if necessary
    
    order_attack,order_mouvement,order_capacity = order(playerID,orders)
    
    try:
        special_capacity1,special_capacity2 = special_capacity_phase(playerID)
    except:
        special_capacity_phase(playerID)
    
    egg_hatch_phase()
    no_damage_turn = dragon_attack(no_damage_turn)[2]
    movement_phase(apprentices, dragons,order_mouvement,map_data)
    regeneration_phase()
    
    
if type_1 == 'remote' or type_2 == 'remote':
        close_connection(connection)
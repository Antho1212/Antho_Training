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

def show_data(column,player,special_capacity1,special_capacity2):
    """Check all info of the concerned player and write it next to the board
    
    Arguments:
    -------------------
    column: column of the case (int)
    player: concerned player (int)
    special_capacity1: count_down for special capacity of player 1 (int)
    special_capacity2: count_down for special capacity of player 2 (int)

    Specification: Sacha ismailov (v.1 26/2/2025)
    Implementation: Sacha ismailov (v.1 26/2/2025)
    """
    line = 0
    if player == 2:line+=13
    print(ui.normal)
    capacity = special_capacity[f'player{int(player)}']
    if 10-special_capacity1 == 0:
        counter_capacity1 = ''
    else:
        counter_capacity1 = f'({10-special_capacity1})'
        
    if 10-special_capacity2 == 0:
        counter_capacity2 = ''
    else:
        counter_capacity2 = f'({10-special_capacity2})'
    
    if player == 1:
        print(ui.home , ui.move_xy(column*6+1,line) , 'special capacity:',capacity, counter_capacity1)
    else:
        print(ui.home , ui.move_xy(column*6+1,line) , 'special capacity:',capacity, counter_capacity2)
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
                    
def special_capacity_phase(playerID: int,special_capacity1,special_capacity2,order_capacity):
    """move all the entity that belong to the concerned player to his altars and reset the fonction compteur_de_tour()
    Parameters:
    -----------
    playerID: ID of the player (1 or 2) (int)
    apprentice: Name of the apprentices that use his capacity (str)
    special_capacity1: count_down for special capacity of player 1 (int)
    special_capacity2: count_down for special capacity of player 2 (int)
    Return:
    -------
    special_capacity1: count_down for special capacity of player 1 (int)
    special_capacity2: count_down for special capacity of player 2 (int)
    Version:
    --------
    Specification : Sacha Ismailov (v.1 - 20/2/2025)
    Specification : Sacha Ismailov (v.2 - 10/3/2025)
    Implementation : Sacha Ismailov (v.2 - 10/3/2025)
    """
    
    altar = altars["altar_"+str(playerID)]
    altar_x = altar['position_x']
    altar_y = altar['position_y']
    
    
    if order_capacity['summon']:
        
        special_capacity['player'+str(playerID)] = False
        for apprentice in apprentices:
            if apprentices[apprentice]['joueur'] == playerID:
                apprentices[apprentice]['position_x'] = altar_x
                apprentices[apprentice]['position_y'] = altar_y
                
                if apprentices[apprentice]['dragons'] !=[]:
                    for dragon in apprentices[apprentice]['dragons']:

                        dragons[dragon]['position_x'] = altar_x
                        dragons[dragon]['position_y'] = altar_y
                        
        special_capacity['player'+str(playerID)] = False
        
        if playerID == 1:
            special_capacity1 = 0
            
        else:
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
    
def dragon_attack(no_damage_turn: int,order_attack:dict) -> tuple[dict, dict,int]:
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
    Specification: +ny Goffin (v.1 - 20/02/2025)
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
 
def order(player_ID,message:str) -> tuple[dict,dict,dict]:
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

def choose_good_dragons()-> tuple:
    """
    sort dragons by power
    
    Return:
    ---------
    dragons_stats_list: list of dragon's statistics(tuple)
    
    Notes:
    ------------
    take the best one with this method:
    ***
    best_list = choose_good_dragons()
    best_dragon = best_list[0]
    ***
    
    Version:
    --------
    Specification: Sacha Ismailov (v.1 - 10/04/2025)
    Implementation: Sacha Ismailov  (v.1 - 12/04/2025)
    """
    
    
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
            if apprentices[apprentice]["joueur"] == dragons[dragon]["joueur"]:
                for dragon_name, drag, dragon_value in dragons_value:  # For each dragon in the sorted dragon list
                    if dragon_name == dragon:  # If the dragon name matches
                        apprentice_value += dragon_value  # Add the dragon's value to the apprentice's value

        targets_value[apprentice] = apprentice_value  # Add the apprentice's value to the dictionary

    # Sort the dictionary by values, from highest to lowest
    sorted_targets =list(sorted(targets_value.items(), key=lambda x: x[1], reverse=True))
    
    return targets_value, sorted_targets  # Return the dictionary of target values and the sorted dictionary


def in_attack_range(apprentices: dict, dragons: dict, dragon: str, directions = None, friend = False) -> list:   
    """
 
    Check if the enemy is in the range of attack.

    Parameters
    ----------
    apprentices (dict): Data about apprentices.
    dragons (dict): Data about dragons.
    dragon (str): The name of the dragon for which enemies in range are checked.
    directions (str or list or None): the direction you want to check, if None check all the directions.
    friend
    Returns
    -------
    people_in_range (list): List of entity names within the attack range of the dragon.

    Version:
    --------
    Specification: Anthony Goffin (v.1 - 27/03/2025)
    Implementation: Anthony Goffin (v.1 - 30/03/2025)
    Implementation: Anthony Goffin (v.2 - 06/04/2025)
    """
 
    coordonate_of_attacks = []
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
            coordonate_of_attacks.append(attack)
            #print("xy attack", x_attack, y_attack)
            if count_entity_on_case(x_attack, y_attack):  # Check if there is someone on the case
                for entity,genre,player in count_entity_on_case(x_attack, y_attack):
                    if not genre == 'egg':   
                        if friend == False:  #if you dont want your team in the range
                            if player != dragons[dragon]['joueur']:
                                people_on_range.append(entity)  # If they are on the attack coordinates and not in the list, add them
                        elif friend == True:  #if you want your team in the range
                                people_on_range.append(entity)
    return people_on_range,coordonate_of_attacks

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

def apprentices_to_cible(apprentices: dict, dragons: dict, message: str, player_id: int) -> str:
    """finds the target closest to the apprentices

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    message: message received from the oeuf_occupes function to not go to the taken eggs (str)
    player_id: player number (int)
    Return:
    -------
    message: message of apprentice movements in the form of an order (str)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Specification : Mohamed Boukhatem (v.2 - 20/04/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    Implementation : Sacha Ismailov (v.2 -  17/04/2025)
    Implementation : Mohamed Boukhatem (v.3 - 20/04/2025)
    """
    position_occupe = [] #list of occupied positions
    commands = message.split() #message splitter because we are only looking for the coordinates
    for command in commands:
            if ':' in command:
                name, action = command.split(':') 
                if (apprentices[name]['joueur'] == player_id):
                    if action and action[0] == '@' and '-' in action:
                        coordonnee = action[1:].split('-') 
                        position_occupe  += (int(coordonnee[0]), int(coordonnee[1])) #coordinates extracted from the oeuf_occcupes function not to be accessed
    for sniper in apprentices:
        if apprentices[sniper]['joueur'] == player_id:
            #moves towards the most profitable egg to win the game
            best_oeuf = best_rentability_move(apprentices, dragons, sniper)
            #MOUVEMENT
            #make sniper_x go to dragons[target]['position_x']
            #make sniper_y go to dragons[target]['position_y']
            if best_oeuf in dragons : #check if dragons is in the dragon dictionary
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
                #checking that the apprentices do not go towards an egg already taken
                if (new_sniper_x, new_sniper_y) not in position_occupe:
                    msg = f' {sniper}:@{new_sniper_y}-{new_sniper_x}'
                    # This message is retrieved from oeuf_occupe and allows you to move to eggs not yet occupied
                    message += msg + " "
    return message

def dragons_to_cible(apprentices: dict, dragons: dict, player_id: int) -> str:
    """finds the target closest to the dragons

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    player_id: player number (int)
    
    Return:
    -------
    message: message of dragon movements in the form of an order (str)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Specification : Mohamed Boukhatem (v.2 - 08/04/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    Implementation : Sacha Ismailov (v.2 -  17/04/2025)
    Implementation : Mohamed Boukhatem (v.3 - 18/04/2025)
    """
    message= ""
    position_occupe = []
    #print(choosed_attack)
    #cible = choosed_attack[1][0][0]
    #all targets that are apprentices different from our allies
    for i in apprentices:
        #print(f'{i} {apprentices[i]['joueur']} != {player_id}-> {apprentices[i]['joueur'] != player_id}')
        if apprentices[i]['joueur'] != player_id:
            cible = i
    min_distance = float('inf')
    best_distance = None
    for sniper in dragons:
        if dragons[sniper]['joueur'] == player_id:
            in_range = in_attack_range(apprentices, dragons, sniper)[0] #Check if the enemy is in the range of attack and head towards
            if in_range ==[]: #check that in_range is indeed a list because the in_attack_range function returns a list and a dictionary
                if apprentices[cible]['joueur'] != dragons[sniper]['joueur']: #check that he is not heading towards the ally
                    #print(sniper, 'cible', cible)
                    #choose the best distance to go
                    distance = abs(dragons[sniper]['position_x'] -apprentices[cible]['position_x']) + abs(dragons[sniper]['position_y'] - apprentices[cible]['position_y'])
                    best_distance = cible
                    if distance < min_distance:
                        min_distance = distance
                        best_distance = cible
            #MOUVEMENT
            #the same as for apprentice_to_cible                                                                                                                                                                                       
            if best_distance :
                sniper_x = dragons[sniper]['position_x']
                sniper_y = dragons[sniper]['position_y']
                cible_x = apprentices[best_distance]['position_x']
                cible_y = apprentices[best_distance]['position_y']
                new_sniper_x = int(sniper_x)
                new_sniper_y = int(sniper_y)
                if sniper_x <= cible_x:
                    new_sniper_x = sniper_x + 1 
                elif sniper_x >= cible_x:
                    new_sniper_x = sniper_x - 1 
                if sniper_y <= cible_y:
                    new_sniper_y = sniper_y + 1
                elif sniper_y >= cible_y:
                    new_sniper_y = sniper_y - 1
                if (new_sniper_x, new_sniper_y) not in position_occupe:
                    msg = f' {sniper}:@{new_sniper_y}-{new_sniper_x}'
                    message += msg + " "
    return message

def best_rentability_move(apprentices: dict, dragons: dict, sniper: str) -> str:
    """the function is supposed to return the best egg to go to

    Parameter:
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    sniper: one of the apprentices chosen to do the movement (str)
    
    Return:
    -------
    best_oeuf_target: the name of the most profitable egg to reach (str)
    
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 27/03/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    Implementation : Mohamed Boukhatem (v.2 - 09/04/2025)
    """
    best_rentability = -1
    best_oeuf_target = None
    oeuf_occupe, message = oeufs_occupes(apprentices, dragons)
    for cible in dragons:
            name = dragons[cible]["name"]
            health= dragons[cible]['health']
            attack = dragons[cible]['attack']
            range = dragons[cible]['range']
            regen = dragons[cible]['regen']
            pos_x= dragons[cible]['position_x']
            pos_y= dragons[cible]['position_y']
            joueur =dragons[cible]['joueur']
            #first make sure that it is indeed an egg and the egg position is not already occupied by another apprentice
            if joueur is None and (pos_x, pos_y) not in oeuf_occupe:
                distance = abs(apprentices[sniper]['position_x'] -pos_x) + abs(apprentices[sniper]['position_y'] -pos_y)
                #for division by zero problems
                if distance != 0:
                    distance = distance
                else:
                    distance = 1
                #calculates profitability_value to improve, value taken arbitrarily while favoring a pattern
                rentability_valeur = 2*health +5*attack +2*range +1*regen
                rentability = rentability_valeur/distance #explains why distance cannot be equal to one
                if rentability > best_rentability:
                    best_rentability = rentability
                    best_oeuf_target = name
    return best_oeuf_target

def good_attack(apprentices :dict, dragons:dict, in_range_directional :list, dragon: str)->bool:
    """if the dragon must attack or no depend on allies and ennemies
    parameters
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionacry (dit)
    in_range_directional: the list with the entity in the range of the attack in one direction (list)
    Version:
    --------
    Specification: Anthony Goffin (v.1 - 017/04/2025)
    Implementation: Anthony Goffin (v.1 - 19/04/2025)
    """
    attack_value = 0   #initialize the value of the attack
    dragon_attack = dragons[dragon]["attack"]    #get the attack og the dragon
    target = targets_attack(apprentices, dragons)[0]    #get the target 
    
    for entity in in_range_directional:     #check the entity in the in the range
        target_value = 0    #initialize the value of the target
        if entity in apprentices:   
            entity_health = apprentices[entity]["health"]
            if apprentices[entity]["joueur"]!= dragons[dragon]["joueur"]:
                target_value += 100       #if you attack a ennemie apprentice
                if entity_health < dragon_attack:
                    target_value += 200   #if the ennemie apprentice will dye
            else:
                target_value -= 100       #if is your apprentice
                if entity_health < dragon_attack:
                    target_value -= 200
        elif entity in dragons:           #same logic than the apprentice but value change dragon are less important
            entity_health = dragons[entity]["health"]
            if dragons[entity]["joueur"]!= dragons[dragon]["joueur"]:
                target_value += 50
                if entity_health < dragon_attack:
                    target_value +=100
            else:
                target_value -= 50
                if entity_health < dragon_attack:
                    target_value -=100
                    
        if entity in target:   # add the value of the target list
            target_value += target[entity]
             
        attack_value += target_value   #add the value of the ennemie to the global attack value
        
    if attack_value >= 0:   #if it's less than 0 False, so it's no good to attack
        return True
    else:
        return False

def attack_orders(apprentices: dict, dragons: dict, player_id: int)->str:
    """give the attack order
    parameters
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionacry (dit)
    returns
    -------
    order_attack: order attack of the AI (str)
    """
    order_message = ""  # Initialize the attack order message
    target_values, sorted_targets = targets_attack(apprentices, dragons)  # Get the target priority list

    for dragon in dragons:  # Loop through each dragon
        if dragons[dragon]['joueur'] == player_id:
            in_range = in_attack_range(apprentices, dragons, dragon)[0]  # Get enemies in attack range
            #print(in_attack_range(apprentices, dragons, dragon))
            #time.sleep(1)
            if in_range:  # If there are enemies in range
                best_target = None  # Initialize the best target to None

                for target_name, target_value in sorted_targets:  # Check each target by priority
                    if target_name in in_range and best_target is None:  # If target is in range and no best target yet
                        best_target = target_name  # Set as best target

                if best_target is None:  # If no target was chosen
                    best_target = in_range[0]  # Default to the first in range
                direction = get_direction(apprentices, dragons, dragon, best_target)  # Determine direction to target
                in_range_directional = in_attack_range(apprentices, dragons, dragon, direction, True)[0] #get the entity in this range
                if good_attack(apprentices, dragons, in_range_directional, dragon):    #check if is good to attack
                    order_message += f"{dragon}:x{direction} "  # Add to the attack order
    
    return order_message

def oeufs_occupes(apprentices: dict, dragons: dict):
    """ The apprentice goes to the egg, staying there until it hatches while preventing an allied apprentice and an allied dragon from going there.
    parameters
    ----------
    apprentices: apprentice data dictionary (dict)
    dragons: dragons data dictionary (dict)
    returns
    -------
    occupe: dictionary of apprentices assigned to an egg sent to best_rentability_move (dict)
    message: message from eggs already targeted sent to apprentices_to_cible (str)
    Version:
    --------
    Specification : Mohamed Boukhatem (v.1 - 08/04/2025)
    Implementation : Mohamed Boukhatem (v.1 - 08/04/2025)
    Implementation : Mohamed Boukhatem (v.2 - 20/04/2025)
    """
    occupe = {}
    positions_des_oeufs = []
    cases_deja_prises = []
    trie_oeuf = choose_good_dragons()
    message = ""
    # we collect the eggs without the dragons
    for dragon in dragons:
        if dragons[dragon]['joueur'] is None:
             # we add all available eggs to the list
            positions_des_oeufs += [(dragons[dragon]['position_x'], dragons[dragon]['position_y'])]
    #print("occupé à la base :", occupe)
    # first step, An apprentice does not leave a square containing an egg until it has hatched
    # we treat each egg
    for cible in dragons:
        if dragons[cible]['joueur'] is None:
            apprenti_sur_la_case = []
            #coordinated with all eggs
            x = dragons[cible]['position_x']
            y = dragons[cible]['position_y']
            # check if the apprentice is already on the case
            for sniper in apprentices:
                if apprentices[sniper]['position_x'] == x and apprentices[sniper]['position_y'] == y:
                    pid = apprentices[sniper]['joueur'] #pid = player_id
                    if (x, y) not in occupe: #if there is not yet the egg assigned to it a dictionary like: (x,y): {apprenti_equipe_1,apprenti_eaquipe_2
                        occupe[(x, y)] = {}
                    if pid not in occupe[(x, y)]: #here there is no egg assigned to the apprentice of each team yet, the assigned
                        occupe[(x, y)][pid] = sniper # the sniper goes to the egg assigned to him
    # second step, we search for an egg depending on whether it has already been found or not beforehand
    # we manage the remaining apprentices
    for apprenti in apprentices:
        x = apprentices[apprenti]['position_x']
        y = apprentices[apprenti]['position_y']
        pid = apprentices[apprenti]['joueur']
        trouve = False
        # we check if the apprentice is already alone on an egg (then he does not move)
        for case in occupe:
            if pid in occupe[case] and occupe[case][pid] == apprenti and case == (x, y): #check that the player has an apprentice on the case
                trouve = True
        if trouve == False:
            #we are looking for a free egg
            distance_min = 9999
            oeuf_cible = None
            for each_oeuf in range(len(positions_des_oeufs)):
                oeuf = positions_des_oeufs[each_oeuf]
                if not (oeuf in occupe and pid in occupe[oeuf]): #so if the egg exists and it is not yet taken go there
                    distance = abs(x - oeuf[0]) + abs(y - oeuf[1])
                    if distance < distance_min:
                        distance_min = distance
                        oeuf_cible = oeuf
            if oeuf_cible is not None:
                if oeuf_cible not in occupe:
                    occupe[oeuf_cible] = {}
                occupe[oeuf_cible][pid] = apprenti
                # move to the target egg
                sniper_x = x
                sniper_y = y
                cible_x, cible_y = oeuf_cible
                if sniper_x < cible_x:
                    sniper_x += 1
                elif sniper_x > cible_x:
                    sniper_x -= 1
                if sniper_y < cible_y:
                    sniper_y += 1
                elif sniper_y > cible_y:
                    sniper_y -= 1
                message += f"{apprenti}:@{sniper_y}-{sniper_x} "
                """# mise à jour des position
                apprentices[apprenti]['position_x'] = sniper_x
                apprentices[apprenti]['position_y'] = sniper_y
                print(f"l'apprenti {apprenti} a pris l'œuf à la position {(x, y)}")
                print("occupé maintenant :", occupe)
                """
    #print("occupe final état :", occupe)
    " print(f'le message ; {message}')"
    return occupe, message


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
    
    occupations_oeufs, message= oeufs_occupes(apprentices, dragons)
    orders = dragons_to_cible(apprentices, dragons,player_id)
    orders += apprentices_to_cible(apprentices, dragons,message, player_id)
    orders += attack_orders(apprentices, dragons,player_id)
    orders += defencemove(player_id,apprentices)
    orders += defencemove(player_id,dragons)
    
    #orders += checkbestdefence(player_id)
    
    #input(orders)
    #time.sleep(0.09)
    
    return orders
    
def checkbestdefence(player):
    """Take the best defence option available    
    
    Parameters
    ----------
    player : Player IA

    Notes
    -----

    Return
    ------
    
    Version
    -------
    Spécification: Artemiy Gimadeev (v.1 - 03/04/25)
                    Artemiy Gimadeev (v.2 - 17/04/25)
    Implémentation: Artemiy Gimadeev (v.1 - 03/04/25)
                    Artemiy Gimadeev (v.2 - 10/04/25)
                    Artemiy Gimadeev (v.3 - 17/04/25)
                    Sacha Ismailov (v.4 -  20/04/2025)
    """
    
    if player == 1:
        ally = 1
        enemy = 2
    elif player == 2:
        ally = 2
        enemy = 1
    team = []
    for apprentice in apprentices:
        if apprentices[apprentice]['joueur'] == player:
            team += [apprentice]
    for dragon in dragons:
        if dragons[dragon]['joueur'] == player:
            team += [dragon]
    #print(team,player)
    message = ""
    for badguy in dragons:
            
            if dragons[badguy]['joueur'] == enemy:
                people_on_range = in_attack_range(apprentices, dragons, badguy)[0]
                
    for badguy in dragons:
        if (dragons[badguy]['joueur'] != player) and (dragons[badguy]['joueur'] != None) :
            
            
            
            
            if (len(people_on_range) == len(team)) and special_capacity['player'+str(player)] == True :
                #print(((people_on_range), (team)) )
                message += " summon " # Fait son action special
                """elif len(people_on_range) == len(team):
                    apprentices_to_cible(apprentices[ally],apprentices[enemy][dragons][badguy]) 
                    dragons_to_cible(apprentices[ally][dragons],apprentices[enemy])"""
                    
            else:
                message += defencemove(ally, enemy)
    return message

def defencemove(player,entities_to_move):
    """Try to move away from the attack of dragons
    
    Parameters
    ----------
    player :

    Notes
    -----

    Return
    ------

    Version
    -------
    Spécification : Artemiy Gimadeev (v.1 - 03/04/25)
                    Artemiy Gimadeev (v.2 - 17/04/25)
    Implémentation : Artemiy Gimadeev (v.1 - 27/03/25)
                    Artemiy Gimadeev (v.2 - 03/04/25)
                    Artemiy Gimadeev (v.3 - 10/04/25)
                    Artemiy Gimadeev (v.4 - 17/04/25)
    Implementation : Sacha Ismailov (v.5 -  20/04/2025)
    """
    
    
        
    listfor = ["N","S","W","E","NW","NE","SW","SE"]
    message = ""
    people_on_range = []
    attack_coordonates = []
    
    #creation of peopl on range and attacks coordonates to send our entyties where we can't be touched
    for badguy in dragons:
        if dragons[badguy]['joueur'] != player and dragons[badguy]['joueur'] != None:
            people_on_range += in_attack_range(apprentices, dragons, badguy)[0]
            attack_coordonates += in_attack_range(apprentices, dragons, badguy)[1]
    
    for novice in entities_to_move:
        fake_break = False
        if entities_to_move[novice]['joueur'] == player and fake_break == False:
            #print(people_on_range)
            if novice in people_on_range: # we must move
                app_x = entities_to_move[novice]['position_x']
                app_y = entities_to_move[novice]['position_y']
                possible_move = [
                        (app_x+1, app_y),# right
                        (app_x-1, app_y),#left
                        (app_x, app_y+1),# down
                        (app_x, app_y-1), #up
                        (app_x+1, app_y+1),#SE
                        (app_x+1, app_y-1),# NE
                        (app_x-1, app_y+1), # SW
                        (app_x-1, app_y-1) # NW
                    ]
                move_done = False
                for move in possible_move:
                    
                    if (move not in attack_coordonates) and (move_done == False) and (move[0] != (map_data[0]+1)) and (move[0] != 0) and (move[1] != (map_data[1]+1)) and (move[1] != 0):
                        message += f"{novice}:@{move[1]}-{move[0]} "
                        
                        #cause I want to take the first one move because I don't realy know how to make a prediction I'll create a fake break
                        move_done = True
                
                if move_done == False:
                    
                    message = 'summon '
                    fake_break == True
                
               
    #print(message)
    return message
# main function
# main function
def play_game(map_path, group_1, type_1, group_2, type_2):
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
    #check up for all entity, if the setup is not well configured we will not start the game
    every_one_on_map = True
    
    for dragon in dragons:
        if (dragons[dragon]['position_x'] >= map_data[0]) and (dragons[dragon]['position_y'] >= map_data[1]):
            every_one_on_map = False
            print('someone is out of map check your .drk')
    for apprentice in apprentices:
        if (apprentices[apprentice]['position_x'] >= map_data[0]) and (apprentices[apprentice]['position_y'] >= map_data[1]):
            every_one_on_map = False
            print('someone is out of map check your .drk')
        
    if every_one_on_map == True:
        ...
        ...
        ...

        row = map_path[0]
        col = map_path[1]
        # create connection, if necessary
        if type_1 == 'remote':
            connection = create_connection(group_2, group_1)
        elif type_2 == 'remote':
            connection = create_connection(group_1, group_2)

        ...
        ...
        ...
        special_capacity1 = 0
        special_capacity2 = 0
        no_damage_turn = 0
        played = -1
        while not game_finish(no_damage_turn):
            
            
            
            
            
            print(ui.clear)
            show_data(col,1,special_capacity1,special_capacity2)
            show_data(col,2,special_capacity1,special_capacity2)
            Board(col,row)
            
            # get orders of player 1 and notify them to player 2, if necessary
            played +=1
            player_id = 1
            if type_1 == 'remote':
                orders = get_remote_orders(connection)
            else:
                orders = get_AI_orders(None, player_id)
                if type_2 == 'remote':
                    notify_remote_orders(connection, orders)                        
            
            input(ui.normal + ui.home + ui.move_down(3*row) + f"Tour: {played}\nJoueur {player_id}\vDonnez la commande à exécuter: " + orders ) #input
            
            order_attack,order_mouvement,order_capacity = order(player_id,orders)
        
            
            
            special_capacity1,special_capacity2 = special_capacity_phase(player_id,special_capacity1,special_capacity2,order_capacity)
            
            egg_hatch_phase()
            no_damage_turn = dragon_attack(no_damage_turn,order_attack)[2]
            movement_phase(apprentices, dragons,order_mouvement,map_data)
            regeneration_phase()
            
            if special_capacity1< 10:special_capacity1 +=1
            if special_capacity1 == 10:special_capacity['player1'] = True
            if special_capacity2 <10:special_capacity2 +=1
            if special_capacity2 == 10:special_capacity['player2'] = True
            
            
            print(ui.clear)
            show_data(col,1,special_capacity1,special_capacity2)
            show_data(col,2,special_capacity1,special_capacity2)
            Board(col,row)
                    
            # get orders of player 2 and notify them to player 1, if necessary
            played +=1
            player_id = 2
            
            if type_2 == 'remote':
                orders = get_remote_orders(connection)
            else:
                orders = get_AI_orders(None, player_id)
                if type_1 == 'remote':
                    notify_remote_orders(connection, orders)
            
            input(ui.normal + ui.home + ui.move_down(3*row) + f"Tour: {played}\nJoueur {player_id}\vDonnez la commande à exécuter: " + orders) #input
            #time.sleep(1)       
            
            order_attack,order_mouvement,order_capacity = order(player_id,orders)
            
            
            special_capacity1,special_capacity2 = special_capacity_phase(player_id,special_capacity1,special_capacity2,order_capacity)
            egg_hatch_phase()
            no_damage_turn = dragon_attack(no_damage_turn,order_attack)[2]
            movement_phase(apprentices, dragons,order_mouvement,map_data)
            regeneration_phase()
            
            if special_capacity1< 10:special_capacity1 +=1
            if special_capacity1 == 10:special_capacity['player1'] = True
            if special_capacity2 <10:special_capacity2 +=1
            if special_capacity2 == 10:special_capacity['player2'] = True
            

        # close connection, if necessary
        if type_1 == 'remote' or type_2 == 'remote':
            close_connection(connection)
        print(ui.clear)
        show_data(col,1,special_capacity1,special_capacity2)
        show_data(col,2,special_capacity1,special_capacity2)
        Board(col,row)
        
        #print(apprentices)
        if no_damage_turn != 100 or 101:
            for i in apprentices:
                player_id = apprentices[i]['joueur']

        # get orders of player 1 and notify them to player 2, if necessary
            print(ui.normal + ui.home + ui.move_down(row*3)+ 'we have a winner player ' + str(player_id)+ '!' + f"\n the game lasted {played+1} laps , {no_damage_turn}")
        else:
            print(ui.normal + ui.home + ui.move_down(row*3)+ f"Equality, No winner\n the game lasted {played+1} laps, no damage turn -> {no_damage_turn}")
        #time.sleep(1)       

map_data, altars, apprentices, dragons, special_capacity = lecture_file('game_data.drk')

#needed for regeneration_phase to stop regeneration
max_lifes = {}
for apprentice in apprentices:
    max_lifes[apprentice] = apprentices[apprentice]['health'] #on va le mettre dans lecture file ou alors je le  fait à part ? (perso plutot mettre dans lecture file, c'est plus logique)
for dragon in dragons:
    max_lifes[dragon] = dragons[dragon]['health']

played = 0

no_damage_turn = 0

special_capacity1 = 0
special_capacity2 = 0

connection = None
group_1 = 0
group_2 = 0

game = None

type_1 = ''
type_2 = ''

play_game(map_data, group_1, type_1, group_2, type_2)
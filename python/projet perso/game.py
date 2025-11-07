import time
import pygame
import os
#import colarama et playsound
pygame.mixer.init()
os.chdir("C:\\Users\\goffi\\Documents\\Programmation\\python")
player_name = str(input("please enter a name : "))

# Initialisation de pygame pour le son
pygame.mixer.init()

# Charger les sons
son = pygame.mixer.Sound("machineecrire.mp3")  # Assurez-vous que le son est court (0.1-0.2s)
son.set_volume(0.1)  # Ajustez le volume si nécessaire

# Fonction pour jouer un son court
def jouer_son_court(son):
    canal = pygame.mixer.find_channel()  # Trouver un canal disponible
    if canal:
        canal.play(son)



# Fonction pour afficher du texte lentement avec un son coordonné
def afficher_texte_lentement(texte, delai=0.1, son=None):
    for caractere in texte:
        print(caractere, end='', flush=True)  # Affiche sans retour à la ligne
        if son:
            jouer_son_court(son)  # Joue un son court pour chaque caractère
        time.sleep(delai)  # Ajoute un délai pour simuler une frappe
    print()  # Retour à la ligne
    




def game():
    """
    main function fot playing, this function call all the scene function
    """ 
    scene_1()

def scene_1():
    afficher_texte_lentement(f"{player_name} it's time to wake up ! you're gonna be late for school!")
    afficher_texte_lentement("what do you want to do? wake up now or in five minute?")
    x = 0 
    while x < 3:
        choose = str(input("choose 1 or 2? : "))
        if choose =="1":
            afficher_texte_lentement("you wake up")
            player = "wake"
            return player
        elif choose =="2":
            afficher_texte_lentement("you fall asleep ")
            player = "sleep"
            return player
        else:
            x+=1
    afficher_texte_lentement("you can't take a decisions and fall asleep")
    return"sleep"


    

game()
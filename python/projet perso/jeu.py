import time
import pygame
import os
os.chdir("C:\\Users\\goffi\\Documents\\Programmation\\python")
# Initialiser pygame pour le son
pygame.mixer.init()

# Charger un fichier audio
def jouer_son(son):
    try:
        pygame.mixer.Sound(son).play()
    except pygame.error as e:
        print(f"Erreur lors de la lecture du son : {e}")

# Demander le nom du joueur
player_name = str(input("Please enter a name: "))

# Fonction pour afficher du texte lentement
def afficher_texte_lentement(texte, delai=0.1, son=None):
    for caractere in texte:
        print(caractere, end='', flush=True)  # Affiche sans retour à la ligne
        if son:
            jouer_son("touchemachineecrire.mp3")  # Joue un son si spécifié
        time.sleep(delai)
    print()  # Retour à la ligne

# Jeu principal
def game():
    """
    Main function for playing, this function calls all the scene functions.
    """
    player = ""
    scene_1()
   
        

def scene_1():
    afficher_texte_lentement(f"{player_name}, it's time to wake up! You're gonna be late for school!", son="clavier.mp3")
    afficher_texte_lentement("What do you want to do? Wake up now or in five minutes?", son="clavier.mp3")
    x = 0
    while x < 3:
        choose = str(input("Choose 1 or 2: "))
        if choose == "1":
            afficher_texte_lentement("You wake up.", son="wake.mp3")
            player = "wake"
            return player
        elif choose == "2":
            afficher_texte_lentement("You fall asleep.", son="sleep.mp3")
            player = "sleep"
            return player
        else:
            afficher_texte_lentement("Invalid choice. Please try again.", son="error.mp3")
            x += 1
    afficher_texte_lentement("You can't make a decision and fall asleep.", son="fall.mp3")
    return "sleep"

game()
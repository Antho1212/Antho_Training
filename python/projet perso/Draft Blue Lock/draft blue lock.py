import pygame
import random

pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
RED = (220, 20, 60)
GRAY = (200, 200, 200)

# Définition de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Blue Lock Draft")

# Chargement de la police
font = pygame.font.Font(None, 32)

# Chargement de l'icône
icon = pygame.image.load("icon.ico")  # Charge l'icône
pygame.display.set_icon(icon)  # Applique l'icône à la fenêtre

# Dictionnaire des joueurs (Nom : Note)
player_dict = {
    "Michael Kaiser": 98, "Don Lorenzo": 96, "Charles Chevalier": 93,
    "Alexis Ness": 93, "Shoei Barou": 92, "Seishiro Nagi": 92,
    "Rensuke Kunigami": 91, "Hyoma Chigiri": 90, "Yoichi Isagi": 88,
    "Gin Gagamaru": 87, "Meguru Bachira": 86, "Oliver Aiku": 85
}

# Variables de jeu
my_team = []
total_rating = 0
number_of_players = 5  # Nombre de joueurs à sélectionner
game_over = False  #  Variable pour stopper le jeu quand l'équipe est complète

# Fonction pour choisir 5 joueurs non sélectionnés
def generate_choices():
    available_players = {p: r for p, r in player_dict.items() if p not in my_team}
    return random.sample(list(available_players.keys()), min(5, len(available_players)))

choices = generate_choices()  # Initialisation des choix

running = True  # Boucle principale
while running:
    screen.fill(WHITE)  # Nettoie l'écran

    # Gérer les événements (fermeture, clics)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  #  Bloque les clics quand game_over = True
            x, y = event.pos
            for i, player in enumerate(choices):
                if 40 < x < 340 and 100 + (i * 40) < y < 130 + (i * 40):
                    if player not in my_team:
                        my_team.append(player)
                        total_rating += player_dict[player]
                        
                        # Vérifier si l'équipe est complète
                        if len(my_team) == number_of_players:
                            game_over = True  #  Empêche de choisir plus de joueurs
                        else:
                            choices = generate_choices()  # Mise à jour des choix
    
    pygame.draw.rect(screen, BLACK,(600,480,100,50),0)
    

    # Affichage des joueurs disponibles (si le jeu n'est pas terminé)
    if not game_over:
        y_offset = 100
        for i, player in enumerate(choices):
            player_text = font.render(f"{player} - {player_dict[player]}", True, BLACK)
            screen.blit(player_text, (50, y_offset))
            pygame.draw.rect(screen, GRAY, (40, y_offset - 5, 300, 30), 2)
            y_offset += 40
    else:
        #  Affichage du message de fin
        end_text = font.render("Équipe complète !", True, RED)
        screen.blit(end_text, (WIDTH // 2 - 80, HEIGHT // 2))
        avg_rating = round(total_rating / number_of_players, 1)
        rating_text = font.render(f"Note moyenne : {avg_rating}/100", True, BLACK)
        screen.blit(rating_text, (WIDTH // 2 - 100, HEIGHT // 2 + 40))

    # Affichage de l'équipe sélectionnée
    team_title = font.render("Your Team:", True, RED)
    screen.blit(team_title, (WIDTH - 250, 100))
    

    y_offset = 150
    for player in my_team:
        team_text = font.render(f"{player} - {player_dict[player]}", True, BLACK)
        screen.blit(team_text, (WIDTH - 250, y_offset))
        y_offset += 40

    # Dessiner la barre de progression
    pygame.draw.rect(screen, BLACK, (50, HEIGHT - 100, 300, 30), 2)
    progress_width = (len(my_team) / number_of_players) * 300
    pygame.draw.rect(screen, BLUE, (50, HEIGHT - 100, progress_width, 30))

    pygame.display.flip()  # Mise à jour de l'écran
    
    


pygame.quit()  # Quitter Pygame proprement

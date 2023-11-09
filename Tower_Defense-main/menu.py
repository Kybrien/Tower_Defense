import pygame as pg
import constants as c

def run_menu():
    # Initialisation de Pygame
    pg.init()

    # Définir la taille de la fenêtre
    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pg.display.set_caption("Menu d'Accueil")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pg.font.Font(None, 36)

    # Bouton "Commencer"
    start_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 - 50, 200, 50)
    start_text = font.render("Commencer", True, BLACK)
    start_text_rect = start_text.get_rect(center=start_button.center)

    # Bouton "Paramètres"
    settings_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 20, 200, 50)
    settings_text = font.render("Paramètres", True, BLACK)
    settings_text_rect = settings_text.get_rect(center=settings_button.center)

    # Bouton "Quitter"
    quit_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 90, 200, 50)
    quit_text = font.render("Quitter", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)

    in_settings_menu = False  # Indique si l'utilisateur est dans le menu des paramètres

    # Menu loop
    running = True
    while running:
        # Gestion des événements
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if in_settings_menu:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    if back_button.collidepoint(mouse_pos):
                        in_settings_menu = False  # Quittez le menu des paramètres et revenez au menu principal
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    print("Début du jeu!")
                    running = False  # Quittez le menu et commencez le jeu
                elif settings_button.collidepoint(mouse_pos):
                    in_settings_menu = True  # Accédez au menu des paramètres
                elif quit_button.collidepoint(mouse_pos):
                    pg.quit()

        # Afficher le texte et les boutons du menu
        screen.fill(WHITE)
        if in_settings_menu:
            # Menu des paramètres
            back_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 150, 200, 50)
            back_text = font.render("Retour", True, BLACK)
            back_text_rect = back_text.get_rect(center=back_button.center)
            screen.blit(back_text, back_text_rect)
        else:
            # Menu principal
            pg.draw.rect(screen, BLACK, start_button, 2)
            screen.blit(start_text, start_text_rect)
            pg.draw.rect(screen, BLACK, settings_button, 2)
            screen.blit(settings_text, settings_text_rect)
            pg.draw.rect(screen, BLACK, quit_button, 2)
            screen.blit(quit_text, quit_text_rect)

        # Mettre à jour l'affichage
        pg.display.flip()

# Vérifiez si ce fichier est exécuté en tant que script principal
if __name__ == "__main__":
    run_menu()

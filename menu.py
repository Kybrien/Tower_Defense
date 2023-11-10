import pygame as pg
import constants as c
import load
import game

pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pg.font.Font(None, 36)
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT ))
background_image = pg.image.load("assets/images/background/background_image.png").convert_alpha()
volume = 0.5  # Volume initial (50%)
volume_step = 0.1  # Étape d'ajustement du volume

def run_menu():
    global volume

    # Définir la taille de la fenêtre
    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pg.display.set_caption("Menu d'Accueil")

    # Bouton "Commencer"
    start_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 - 330, 200, 50)
    start_text = font.render("Commencer", True, BLACK)
    start_text_rect = start_text.get_rect(center=start_button.center)

    # Bouton "Paramètres"
    settings_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 - 260, 200, 50)
    settings_text = font.render("Paramètres", True, BLACK)
    settings_text_rect = settings_text.get_rect(center=settings_button.center)

    # Bouton "Quitter"
    quit_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 - 185, 200, 50)
    quit_text = font.render("Quitter", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)

    # Bouton "Credits"
    credit_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 250, 200, 50)
    credit_text = font.render("Crédits", True, BLACK)
    credit_text_rect = credit_text.get_rect(center=credit_button.center)



    in_settings_menu = False  # Indique si l'utilisateur est dans le menu des paramètres
    in_credits_menu = False

    # Menu loop
    running = True
    while running:
        # Gestion des événements
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if in_settings_menu:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    if back_button.collidepoint(mouse_pos):
                        in_settings_menu = False  

            if in_credits_menu:
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    if back_button.collidepoint(mouse_pos):
                        in_credits_menu = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    print("Début du jeu!")
                    game.game_run()  # Quittez le menu et commencez le jeu
                elif settings_button.collidepoint(mouse_pos):
                    in_settings_menu = True  # Accédez au menu des paramètres
                elif credit_button.collidepoint(mouse_pos): 
                    in_credits_menu = True #Accédez au crédits
                elif quit_button.collidepoint(mouse_pos):
                    pg.quit()

        # Afficher le texte et les boutons du menu
        screen.blit(background_image, (0, 0))

        if in_settings_menu:
            # Bouton "+"
            volume_up_button = pg.Rect(c.SCREEN_WIDTH // 2 - 150, c.SCREEN_HEIGHT // 2 + 100, 50, 50)
            volume_up_text = font.render("##### + #####", True, BLACK)
            volume_up_text_rect = volume_up_text.get_rect(center=volume_up_button.center)
            screen.blit(volume_up_text, volume_up_text_rect)

            # Bouton "-"
            volume_down_button = pg.Rect(c.SCREEN_WIDTH // 2 + 100, c.SCREEN_HEIGHT // 2 + 100, 50, 50)
            volume_down_text = font.render("##### - #####", True, BLACK)
            volume_down_text_rect = volume_down_text.get_rect(center=volume_down_button.center)
            screen.blit(volume_down_text, volume_down_text_rect)
            
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()

                # Vérifier le clic sur le bouton "+"
                if volume_up_button.collidepoint(mouse_pos):
                    volume = min(1.0, volume + volume_step)
                    pg.mixer.music.set_volume(volume)
                    load.adjust_sound_effects_volume(volume)


                # Vérifier le clic sur le bouton "-"
                elif volume_down_button.collidepoint(mouse_pos):
                    volume = max(0.0, volume - volume_step)
                    pg.mixer.music.set_volume(volume)
                    load.adjust_sound_effects_volume(volume)



            # Menu des paramètres
            back_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 300, 200, 50)
            back_text = font.render("Retour", True, BLACK)
            back_text_rect = back_text.get_rect(center=back_button.center)
            screen.blit(back_text, back_text_rect)

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()

                # Vérifier le clic sur le bouton "+"
                if volume_up_button.collidepoint(mouse_pos):
                    volume = min(1.0, volume + volume_step)  # Augmenter le volume (maximum 1.0)
                    # Appliquer le nouveau volume au son du jeu
                    pg.mixer.music.set_volume(volume)

                # Vérifier le clic sur le bouton "-"
                elif volume_down_button.collidepoint(mouse_pos):
                    volume = max(0.0, volume - volume_step)  # Diminuer le volume (minimum 0.0)
                    # Appliquer le nouveau volume au son du jeu
                    pg.mixer.music.set_volume(volume)

        if in_credits_menu:
            back_button = pg.Rect(c.SCREEN_WIDTH // 2 - 100, c.SCREEN_HEIGHT // 2 + 300, 200, 50)
            back_text = font.render("Retour", True, BLACK)
            back_text_rect = back_text.get_rect(center=back_button.center)
            screen.blit(back_text, back_text_rect)

            credits_text = [
            "Crédits:",
            "Développé par Lucie, Gwendal, Julen",
            "Musique par Mathias",
            "Graphismes par Adrien PATTé",
            "Merci d'avoir joué!",
            ]
            y_offset = 30
            for line in credits_text:
                text = font.render(line, True, BLACK)
                text_rect = text.get_rect(center=(c.SCREEN_WIDTH // 2, y_offset))
                screen.blit(text, text_rect)
                y_offset += 40

        else:
            # Menu principal
            pg.draw.rect(screen, BLACK, start_button, 2)
            screen.blit(start_text, start_text_rect)
            pg.draw.rect(screen, BLACK, settings_button, 2)
            screen.blit(settings_text, settings_text_rect)
            pg.draw.rect(screen, BLACK, quit_button, 2)
            screen.blit(quit_text, quit_text_rect)
            pg.draw.rect(screen,BLACK, credit_button, 2)
            screen.blit(credit_text, credit_text_rect)
        # Mettre à jour l'affichage
        pg.display.flip()

            
# Vérifiez si ce fichier est exécuté en tant que script principal
if __name__ == "__main__":
    run_menu()



    

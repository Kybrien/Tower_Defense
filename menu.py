import pygame as pg
from constants import SCREEN_WIDTH,SIDE_PANEL

class Menu:
    def __init__(self, screen_width, side_panel):
        # Initialize pygame
        pg.init()

        # Define the window size
        self.screen = pg.display.set_mode((screen_width + side_panel, screen_width))
        pg.display.set_caption("Slay Eater")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pg.font.Font(None, 36)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.running = False

    def update(self):
        # Add any game logic or updates here
        pass

    def draw(self):
        self.screen.fill(self.WHITE)
        text = self.font.render("Appuyez sur Entrée pour commencer", True, self.BLACK)
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pg.display.flip()

    def quit(self):
        pg.quit()

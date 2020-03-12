import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa do reprezentacji pojedynczego obcego"""

    def __init__(self, ai_game):
        """Utwórz obcego i ustaw jego pozycję początkową"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Załaduj obrazek obcego i ustaw atrybuty
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Utwórz każdego obcego w lewym górnym narożniku ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Zachowaj pozycję obcego jako liczbę zmiennoprzecinkową
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca prawdę, jeśli obcy przekroczy krawędź ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Przesuwa obcego w prawo lub lewo"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

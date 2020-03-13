import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    """Klasa do zarządzania statkiem"""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie
        początkowe"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # Pozycja statku
        self.x = float(self.rect.x)

        # Flagi ruchu
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Zmiana pozycji statku na podstawie flag ruchu"""
        # Aktualizuj pozycje x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Wyświetlanie statku kosmicznego w jego aktualnym  położeniu"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Wyśrodkowanie statku na ekranie"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

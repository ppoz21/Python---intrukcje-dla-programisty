import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AllienInvasion:
    """Główna klasa do zarządzania zasobami i zachowaniem"""

    def __init__(self):
        """Inicjalizacja gry, utworzenie zasobów"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Pętla główna gry"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Odpowiada na przyciski klawiatury i zachowanie myszy"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Odpowiada na naciśnięcia przycisków"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utwórz nowy pocisk i dodaj do grupy pocisków"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bulets(self):
        """Aktualizacja pozycji pocisków w grupach"""
        # Aktualizuj grupy pocisków
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Aktualizacja obrazów na ekranie, przeskoczenie do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Utwórz instancję klasy, uruchom grę
    ai = AllienInvasion()
    ai.run_game()

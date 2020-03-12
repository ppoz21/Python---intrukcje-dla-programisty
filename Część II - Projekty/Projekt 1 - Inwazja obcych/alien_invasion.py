import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # Utworzenie obiektu do przechowywania statystyk
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Pętla główna gry"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
        "Odpowiada na puszczenie przycisku"
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utwórz nowy pocisk i dodaj do grupy pocisków"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Aktualizacja pozycji pocisków w grupach"""
        # Aktualizuj grupy pocisków
        self.bullets.update()

        # Usuwanie pocisków poza ekranem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Sprawdza, czy zaszła kolizja obcy-pocisk"""

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Zniszcz istniejące pociski i utwórz nową flotę
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """
        Sprawdza czy flota jest na krawędzi
        potem aktualizuje wszystkich obcych we flocie
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Sprawdzaie kolizji obcy-statek
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Spradzanie, czy obcy doleciał do dołu ekranu
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Sprawdza, czy jakiś obcy doleciał do dołu ekranu"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # To samo, co w przypadku uderzenia w kosmitę
                self._ship_hit()
                break

    def _ship_hit(self):
        """Uderzenie kosmity w statek"""
        if self.stats.ships_left > 0:
            # Zmniejszenie liczby statków
            self.stats.ships_left -= 1

            # Usunięcie kosmitów i pocisków
            self.aliens.empty()
            self.bullets.empty()

            # Utworzenie nowej floty obcych, centrowanie statku
            self._create_fleet()
            self.ship.center_ship()

            # Pauza
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _create_fleet(self):
        """Utwórz floty obcych"""
        # Utworzenie obcego
        # Odstęp między obcymi wynosi długość obcego
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens = available_space_x // (2 * alien_width)

        # Ustalenie ilości wierszy z obcymi, które mieszczą się na ekrania
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2* alien_height)

        # Utworzenie floty obcych
        for row_number in range(number_rows):
            for alien_number in range(number_aliens):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego w wierszu"""
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Sprawdza, czy jakikolwiek obcy osiągnął krawędź ekranu"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Zmienia kierunek poziomy floty"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Aktualizacja obrazów na ekranie, przeskoczenie do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Utwórz instancję klasy, uruchom grę
    ai = AllienInvasion()
    ai.run_game()

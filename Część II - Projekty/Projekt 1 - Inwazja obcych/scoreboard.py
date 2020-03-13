import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Klasa do przechowywania informacji o wynikach"""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów przechowywania wyniku"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Ustawienia czcionki
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazów z punktacją
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_score = round(self.stats.score, -1)
        score_str = ":,".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Wyświetlenie wyniku w prawym górnym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.screen_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najwyższego wyniku na wygenerowany obraz"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = ":,".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        # Centrowanie najwyższego wyniku na górze ekranu
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Zmień poziom w wyrenderowany obraz"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)

        # Pozycjonowanie poziomu pod wynikiem
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Pokaż ile statków zostało"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def chceck_high_score(self):
        "Sprawdź czy jest nowy najwyższy wynik"
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Rysuj wynik, poziom i pozostałe statki na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

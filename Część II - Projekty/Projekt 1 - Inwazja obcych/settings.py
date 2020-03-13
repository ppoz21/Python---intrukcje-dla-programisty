class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia statku
        self.ship_limit = 3

        # Ustawienia pocisku
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ustawienia obcego
        self.fleet_drop_speed = 10

        # Jak szybko gra przyspiesza
        self.speedup_scale = 1.1
        # Jak szybko wzrastają punkty za obcych
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które zmieniają się w trakcie gry"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Kierunek floty, 1 reprezentuje prawy, -1 lewy
        self.fleet_direction = 1

        # Punktacja
        self.alien_points = 50

    def increase_speed(self):
        """Zwiększanie ustawień prędkości"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

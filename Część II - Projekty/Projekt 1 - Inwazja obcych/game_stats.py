class GameStats:
    """Śledzi statystki gry"""

    def __init__(self, ai_game):
        """Inicjalizacja statystyk"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Status game_active
        self.game_active = False

        # Najwyższy wynik nie powinien być usuwany
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja statystk, zmienianych w trakcie gry"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

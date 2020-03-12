class GameStats:
    """Śledzi statystki gry"""

    def __init__(self, ai_game):
        """Inicjalizacja statystyk"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Status game_active
        self.game_active = True

    def reset_stats(self):
        """Inicjalizacja statystky, zmienianych w trakcie gry"""
        self.ships_left = self.settings.ship_limit

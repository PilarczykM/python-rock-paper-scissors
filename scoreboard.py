from collections import defaultdict
from typing import Dict


class Scoreboard:
    """Scoreboard class to register player, track points
    """

    def __init__(self):
        self.points: dict[str, int] = {}

    def register_player(self, player_name: str) -> None:
        self.points[player_name] = 0

    def win_round(self, player_name: str) -> None:
        self.points[player_name] += 1

from collections import defaultdict
from typing import Dict


class Scoreboard:
    """Scoreboard class to register player, track points
    """

    def __init__(self):
        self.points: Dict[str, int] = defaultdict(int)

    def register_player(self, user_name: str) -> None:
        self.points[user_name] = 0

from scoreboard import Scoreboard
from rules import RULES, get_winner
from user_interface.ui import UI


class Game:
    def __init__(self, ui: UI, user: str) -> None:
        self.ui = ui
        self.scoreboard = Scoreboard()
        self.rules = RULES
        self.player_name: str = user
        self.cpu_name: str = "cpu"

    def _do_turn(self) -> None:
        user_entity = self.ui.pick_player_entity()
        cpu_entity = self.ui.pick_cpu_entity()

        self.ui.display_current_round(self.player_name, self.cpu_name, user_entity, cpu_entity)

        winner, message = get_winner(user_entity, cpu_entity)
        if not winner:
            self.ui.display_tie()
        elif winner == user_entity:
            self.ui.display_round_winner(self.player_name, user_entity, message)
            self.scoreboard.points[self.player_name] += 1
        else:
            self.ui.display_round_winner(self.cpu_name, cpu_entity, message)
            self.scoreboard.points[self.cpu_name] += 1

    def play(self, max_round: int = 5):
        # register players
        self.scoreboard.register_player(self.player_name)
        self.scoreboard.register_player(self.cpu_name)

        # display game rules
        self.ui.display_rules()
        for _ in range(max_round):
            self._do_turn()
            self.ui.display_score(self.scoreboard.points)

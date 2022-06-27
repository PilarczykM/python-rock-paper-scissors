from dataclasses import dataclass

from rules import get_winner
from scoreboard import Scoreboard
from user_interface.ui import UI


@dataclass
class Game:
    player_name: str
    scoreboard: Scoreboard
    ui: UI
    cpu_name: str = "cpu"

    def _do_turn(self) -> None:
        user_entity = self.ui.pick_player_entity()
        cpu_entity = self.ui.pick_cpu_entity()

        self.ui.display_current_round(self.player_name, self.cpu_name, user_entity, cpu_entity)

        winner, message = get_winner(user_entity, cpu_entity)
        if not winner:
            self.ui.display_tie()
        elif winner == user_entity:
            self.ui.display_round_winner(self.player_name, user_entity, message)
            self.scoreboard.win_round(self.player_name)
        else:
            self.ui.display_round_winner(self.cpu_name, cpu_entity, message)
            self.scoreboard.win_round(self.cpu_name)

    def play(self, max_round: int = 5):
        # register players
        self.scoreboard.register_player(self.player_name)
        self.scoreboard.register_player(self.cpu_name)

        # display game rules
        self.ui.display_rules()
        for _ in range(max_round):
            self._do_turn()
            self.ui.display_score(self.scoreboard.points)

from game import Game
from scoreboard import Scoreboard
from user_interface.cli_ui import Cli


def main() -> None:
    ui = Cli()
    scoreboard = Scoreboard()
    player_name = ui.read_user_name()
    game = Game(ui=ui, scoreboard=scoreboard, player_name=player_name)
    game.play()


if __name__ == "__main__":
    main()

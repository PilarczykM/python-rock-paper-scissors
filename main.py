from game import Game
from user_interface.cli_ui import Cli


def main() -> None:
    """Main function to start the game
    """
    ui = Cli()
    user_name = ui.read_user_name()
    game = Game(ui, user_name)
    game.play()


if __name__ == "__main__":
    main()

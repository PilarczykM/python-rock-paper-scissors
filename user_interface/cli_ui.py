import random

from entity import Entity
from user_interface.ui import UI


def _entities_str() -> str:
    """Return the user choices
    """
    return ", ".join(f"({entity.value} for {entity.name})" for entity in Entity)


class Cli(UI):
    @staticmethod
    def pick_player_entity() -> Entity:
        available_choices = [entity.value for entity in Entity]
        while True:
            try:
                print(f"Select {_entities_str()}:", end='\t')
                choice = int(input())

                if choice not in available_choices:
                    print("Please select from available choices")
                else:
                    return Entity(choice)
            except ValueError:
                print("You entered something other than a number")

    @staticmethod
    def pick_cpu_entity() -> Entity:
        cpu_choice = random.randint(1, len(Entity))
        return Entity(cpu_choice)

    @staticmethod
    def display_rules() -> None:
        print("Rock paper scissor spock and lizard...\n Welcome to the game.")
        print("Rules are simple...")
        print(
            "Scissors decapitate Lizard, Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons "
            "Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, "
            "Spock vaporizes rock, and as it always has, rock crushes scissors.")
        print("To begin press [Enter]")
        _ = input()

    @staticmethod
    def display_current_round(player_name: str, cpu_name: str, player_entity: Entity, cpu_entity: Entity) -> None:
        print(f"{player_name} ({player_entity.name}) x {cpu_name} ({cpu_entity.name})")
        print("....")

    @staticmethod
    def display_tie() -> None:
        print("It's a tie..")

    @staticmethod
    def display_round_winner(winner_name: str, winner_entity: Entity, message) -> None:
        print(f"{winner_name} ({winner_entity.name}) wins the round as {message}")

    @staticmethod
    def display_score(scores: dict[str, int]) -> None:
        print("Scoreboard:")
        print("======================================")
        for user, score in scores.items():
            print(f"{user} : {score}", end='\t')
        print("\n======================================")

    @staticmethod
    def read_user_name() -> str:
        print("Please enter your name:", end='\t')
        return str(input().strip())

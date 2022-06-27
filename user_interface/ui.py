from typing import Protocol

from entity import Entity


class UI(Protocol):
    @staticmethod
    def pick_player_entity() -> Entity:
        """Selects a player entity
        Returns:
            Entity: A random entity
        """
        raise NotImplemented()

    @staticmethod
    def pick_cpu_entity() -> Entity:
        """Selects a random entity
        Returns:
            Entity: A random entity
        """
        raise NotImplemented()

    @staticmethod
    def display_rules() -> None:
        """Display rules message
        """
        raise NotImplemented()

    @staticmethod
    def display_current_round(player_name: str, cpu_name: str, player_entity: Entity, cpu_entity: Entity) -> None:
        """Display the current round
        Args:
            player_name (str): Player Name
            cpu_name (str): CPU Name
            player_entity (Entity): Entity selected by the player
            cpu_entity (Entity): Entity selected by the cou
        """
        raise NotImplemented()

    @staticmethod
    def display_tie() -> None:
        """Display tie message
        """
        raise NotImplemented()

    @staticmethod
    def display_round_winner(winner_name: str, winner_entity: Entity, message) -> None:
        """Display the winner of the round
        Args:
            winner_name (str): Winner Name
            winner_entity (Entity): Entity selected by the winner
            message (str): Reason for wins
        """
        raise NotImplemented()

    @staticmethod
    def display_score(scores: dict[str, int]) -> None:
        """Display the scoreboard
        Args:
            scores (dict[str, int]): Scoreboard dictionary
        """
        raise NotImplemented()

    @staticmethod
    def read_user_name() -> str:
        """Static method to get username as input
        Returns:
            str: Name entered by user
        """
        raise NotImplemented()

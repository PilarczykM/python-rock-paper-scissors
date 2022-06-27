from typing import Protocol

from entity import Entity


class UI(Protocol):
    def pick_player_entity(self) -> Entity:
        raise NotImplemented()

    def pick_cpu_entity(self) -> Entity:
        raise NotImplemented()

    def display_rules(self) -> None:
        raise NotImplemented()

    def display_current_round(self, player_name: str, player_entity: Entity) -> None:
        raise NotImplemented()

    def display_tie(self) -> None:
        raise NotImplemented()

    def display_round_winner(self, winner_name: str, winner_entity: Entity, message) -> None:
        raise NotImplemented()

    def display_score(self, scores: dict[str, int]) -> None:
        raise NotImplemented()

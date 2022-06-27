from typing import Optional

from entity import Entity

RULES: dict[tuple[Entity, Entity], str] = {
    (Entity.PAPER, Entity.ROCK): "covers",
    (Entity.PAPER, Entity.SPOCK): "disapproves",
    (Entity.ROCK, Entity.LIZARD): "crushes",
    (Entity.ROCK, Entity.SCISSOR): "crushes",
    (Entity.SCISSOR, Entity.PAPER): "cuts",
    (Entity.SCISSOR, Entity.LIZARD): "decapitates",
    (Entity.SPOCK, Entity.SCISSOR): "smashes",
    (Entity.SPOCK, Entity.ROCK): "vaporizes",
    (Entity.LIZARD, Entity.SPOCK): "poisons",
    (Entity.LIZARD, Entity.PAPER): "eats"
}


def get_winner(entity1: Entity, entity2: Entity) -> tuple[Optional[Entity], str]:
    """A function to find the winner between two entities and reason for win
            Args:
                entity1 (Entity): First entity
                entity2 (Entity): Second entity
            Raises:
                KeyError: Invalid combination of entity
            Returns:
                Entity: Winner of entity1 and entity2
                str: Reason for win
    """
    if entity1 == entity2:
        return None, "It's a tie"
    elif (entity1, entity2) in RULES:
        return (
           entity1,
           f"{entity1.name} {RULES[(entity1, entity2)]} {entity2.name}"
        )
    elif (entity2, entity1) in RULES:
        return (
            entity2,
            f"{entity2.name} {RULES[(entity2, entity1)]} {entity1.name}"
        )
    raise KeyError('Invalid entities')

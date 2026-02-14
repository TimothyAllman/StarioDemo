import random

from stariodemo.DataStructsPkg.AdjectivesModule import ADJECTIVES
from stariodemo.DataStructsPkg.AnimalsModule import ANIMALS


def generate_username() -> str:
    """Generate a random fun username like 'HappyPanda'."""
    return f"{random.choice(ADJECTIVES)}{random.choice(ANIMALS)}"

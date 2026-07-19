import random

from stariodemo.BasicStructsPkg.AdjectivesModule import ADJECTIVES
from stariodemo.BasicStructsPkg.AnimalsModule import ANIMALS


def generate_username() -> str:
    """Generate a random fun username like 'HappyPanda'."""
    return f"{random.choice(ADJECTIVES)}{random.choice(ANIMALS)}"

import random

from stariodemo.WebsiteFeatureChatAppPkg.AdjectivesModule import ADJECTIVES
from stariodemo.WebsiteFeatureChatAppPkg.AnimalsModule import ANIMALS


def generate_username() -> str:
    """Generate a random fun username like 'HappyPanda'."""
    return f"{random.choice(ADJECTIVES)}{random.choice(ANIMALS)}"

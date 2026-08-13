import random

from stariodemo.WebsiteFeatureChatAppPkg.ColorsModule import COLORS


def generate_color() -> str:
    """Pick a random color for the user's avatar."""
    return random.choice(COLORS)

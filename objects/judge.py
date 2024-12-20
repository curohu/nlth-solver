from .community import Community
from .deck import Card


class Judge:
    def __init__(self, pocket: list[Card, Card], community: Community):
        self.pocket = pocket
        self.community = community

    def identify_best_hand_value():
        pass

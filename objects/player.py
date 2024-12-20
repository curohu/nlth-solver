from .deck import Card
from .community import Community


class Player:
    def __init__(self):
        self.hand: list[Card] = []
        self.balance = 0.0
        self.state = ""
        self.actions: list[str] = []

    def bet(self):
        pass

    def call(self, bet_match_amount):
        if bet_match_amount > self.balance:
            self.state = "call;all-in"
            self.actions.append(self.state)
            call_amount = self.balance
            self.balance = 0.0
            return call_amount

    def fold(self):
        pass

    def new_round(self):
        self.hands = []
        self.state = ""
        self.actions = []

    def decide(self, game_state: str, community: Community):
        pass


class Hero(Player):
    def __init__(self):
        super().__init__()


class Villian(Player):
    def __init__(self):
        super().__init__()

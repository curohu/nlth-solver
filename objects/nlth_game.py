from objects.deck import Card, Deck
from objects.player import Player
from objects.community import Community


class Game:
    def __init__(self):
        self.players: list[Player] = []
        self.players_in_play: list[Player] = []
        self.deck: Deck = Deck()
        self.community: Community = Community()
        self.state: str = "new_round"

    def generate_random_players(self, count: int = 2):
        for c in range(count):
            self.players.append(Player())

    def deal_cards_to_players(self):
        for player in self.players:
            player.hand = self.deck.deal(2)

    def new_round(self):
        self.state = 0
        self.community.new_round()
        for player in self.players:
            player.new_round()
        self.deck.generate()

    def increment_game_state(self):
        match self.state:
            case "new_round":
                self.state = "preflop"
                self.deal_cards_to_players()
                for player in self.players:
                    action = player.decide(self.state, self.community)

            case "preflop":
                self.state = "flop"
                self.community.deal()
                for player in self.players:
                    action = player.decide(self.state, self.community)

            case "flop":
                self.state = "turn"
                self.community.deal()
                for player in self.players:
                    action = player.decide(self.state, self.community)

            case "turn":
                self.state = "river"
                self.community.deal()
                for player in self.players:
                    action = player.decide(self.state, self.community)

            case "river":
                self.state = "new_round"
                self.new_round()

            case _:
                raise IndexError

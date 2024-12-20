from .deck import Card, Deck


class Community(list):
    def __init__(self):
        self.cards: list[Card] = []

    def deal(self, deck: Deck):
        match len(self.cards):
            case 0:
                deck.burn()
                self.cards.extend(deck.deal(3))
            case 3:
                deck.burn()
                self.cards.append(deck.deal())
            case 4:
                deck.burn()
                self.cards.append(deck.deal())
            case _:
                raise IndexError

    def new_round(self):
        self.cards = []

    def shuffle_back_into_deck(self):
        shuffle_back = self.cards
        self.cards = []
        return shuffle_back

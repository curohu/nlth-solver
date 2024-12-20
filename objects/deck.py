import random


class Card:
    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip

    def __str__(self):
        return f"{self.pip}{self.suit}"

    def __repr__(self):
        return f"{self.pip}{self.suit}"


class Deck(list):
    def __init__(self):
        self.deck: list[Card] = []
        self.burn_pile: list[Card] = []
        self.suits = ["c", "s", "d", "h"]
        self.pips = [str(n) for n in range(2, 10)]
        self.pips.extend(["T", "J", "Q", "K", "A"])
        self.generate()

    def generate(self):
        self.deck = []
        for suit in self.suits:
            for pip in self.pips:
                self.deck.append(Card(suit, pip))
        self.shuffle()

    def shuffle(self):
        random.seed()
        random.shuffle(self.deck)

    def extend(self, iterable):
        return self.deck.extend(iterable)

    def deal(self, count: int = 1):
        hand: list[Card] = []
        if len(self.deck) > count - 1:
            for c in range(count):
                hand.append(self.deck.pop())
            return hand

    def burn(self):
        if len(self.deck) > 0:
            self.burn_pile.append(self.deck.pop())

    def draw(self):
        if len(self.deck) > 0:
            return self.deck.pop()

    def shuffle_community_back_in(self, community):
        self.deck.extend(community.shuffle_back_into_deck())
        self.deck.extend(self.burn_pile)
        self.burn_pile = []

    def __len__(self):
        return len(self.deck)

    def __next__(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    deck = Deck()
    deck.generate()
    deck.shuffle()
    print(len(deck))
    for card in deck:
        print(card)

import time
import json

from objects.deck import Deck, Card
from objects.player import Hero, Villian
from objects.community import Community
from objects.judge import Judge

"""
Workflow:
Hero is dealt 2 cards from the Deck
Solve for 1000 iterations of the game making it to the river (5 cards in community)

"""


class PreFlopHand:
    def __init__(self, hand: list[Card, Card]):
        self.hand = hand
        if len(hand) != 2:
            raise ValueError
        self.suited = False
        self.normalized_pips: str = ""
        self.normalized_hand: str = ""
        self.normalize_preflop_hand()

    def normalize_preflop_hand(self):
        if self.hand[0].suit == self.hand[1].suit:
            self.suited = True
        pips = [self.hand[0].pip, self.hand[1].pip]
        pips.sort(reverse=True)
        self.normalized_pips = f"{pips[0]}{pips[1]}"
        if self.suited:
            self.normalized_hand = self.normalized_pips + "s"
        else:
            self.normalized_hand = self.normalized_pips + "o"

    def __repr__(self):
        self.hand: list
        hand = sorted(self.hand, key=lambda card: card.pip, reverse=True)
        return str(sorted(hand, key=lambda card: card.suit, reverse=True))


class PreFlopGameState(str):
    def __init__(self, preflophand: PreFlopHand):
        self.preflophand = preflophand
        self.deck = self._generate_matching_deck()
        self.simulation_iteration = 0
        self.simulated_results = []

    def _generate_matching_deck(self):
        deck = Deck()
        for pf_card in self.preflophand.hand:
            card_to_remove = None
            for card in deck.deck:
                if str(pf_card) == str(card):
                    card_to_remove = card
                    break
            deck.deck.remove(card_to_remove)
        return deck

    def simulate(self):
        self.deck.shuffle()
        villian_cards: list[Card, Card] = self.deck.deal(2)
        community = Community()
        while len(community.cards) < 5:
            community.deal(self.deck)
        v_judge = Judge(villian_cards, community)
        villian_value = v_judge.identify_best_hand_value()
        h_judge = Judge(self.preflophand.hand, community)
        hero_value = h_judge.identify_best_hand_value()
        result = ""
        if hero_value > villian_value:
            result = "win"
        elif hero_value == villian_value:
            result == "tie"
        elif hero_value < villian_value:
            result = "lose"
        self.simulation_iteration += 1
        self.simulated_results.append(result)
        self.deck.extend(villian_cards)
        self.deck.shuffle_community_back_in(community)

    def __repr__(self):
        return self.preflophand.__repr__()


"""
generate all possible preflop game states
1. generate all possible preflop hand
2. generate matching decks

"""

pf_states: list[PreFlopGameState] = []
normalized_pf_states: list[PreFlopGameState] = []


def generate_all_possible_preflop_states():
    deck1 = Deck()
    deck2 = Deck()
    count = 0
    for card1 in deck1.deck:
        for card2 in deck2.deck:
            if str(card1) == str(card2):
                continue
            count += 1
            hand = [card1, card2]
            pf_hand = PreFlopHand(hand)
            gs = PreFlopGameState(pf_hand)
            duplicate = False
            for pf_state in pf_states:
                if str(gs) == str(pf_state):
                    duplicate = True
                    break
            if not duplicate:
                pf_states.append(PreFlopGameState(pf_hand))
    print(count)


def normalize_preflop_states():
    for pf_state in pf_states:
        found = False
        for n_state in normalized_pf_states:
            if (
                pf_state.preflophand.normalized_hand
                == n_state.preflophand.normalized_hand
            ):
                found = True
                break
        if not found:
            normalized_pf_states.append(pf_state)


if __name__ == "__main__":
    stime = time.time()
    generate_all_possible_preflop_states()
    print(len(pf_states))
    # json.dump(pf_states, open("./data/all_pf_states.json", "w"), indent=4)
    normalize_preflop_states()
    print(len(normalized_pf_states))
    print(f"{time.time()-stime:.2f}")

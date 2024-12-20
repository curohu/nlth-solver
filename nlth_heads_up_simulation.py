from objects.deck import Deck, Card
from objects.community import Community
from objects.player import Player, Hero, Villian
from objects.nlth_game import Game


game = Game()

hero = Hero()
villian = Villian()
game.players = [hero, villian]

game.increment_game_state()
print(hero.hand)
print(villian.hand)

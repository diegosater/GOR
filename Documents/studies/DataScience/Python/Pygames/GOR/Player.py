import deck
import battlefield


'''
Player class - attributes and actions made by a players
of GoR
'''


class Player:
    def __init__(self, name, card_of_player_deck):
        self.player_name = name
        self.player_deck = deck.Deck(card_of_player_deck)
        self.battlefield = battlefield.Battlefield()

    def atack():
        pass

    def change_mode():
        pass

    def put_card_on_battlefield():
        pass

    def use_power():
        pass

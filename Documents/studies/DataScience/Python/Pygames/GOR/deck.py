import Player,card,power,battlefiled

class Deck():
    def __init__(self,card_list):
        self.deck_cards =[]
        self.deck_cards = card_list


class Hand(Deck):
    def __init__(self,card_list):
        self.cards_on_hand =[]
        self.cards_on_hand = card_list


class Semetary(Deck):
    def __init__(self,card):
        self.has_it_atacked =[]
        self.has_it_not_attacked =[]
        self.killed_by_avalanche =[]
        if card

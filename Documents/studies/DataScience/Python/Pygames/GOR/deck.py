import Player
import card
import power
import battlefield


class Deck():

    def __init__(self, name, card_list):
        # Can be P1_deck or P1_hand (as so to others Ps) or Semetary
        self.deck_name = name
        self.deck_cards = []
        self.deck_cards = card_list

    def evil_key():
        '''Exchange decks between a Player chosen by who use the evil_key and itself'''
        pass


class Semetary(Deck):
    def __init__(self, dead_card):
        self.has_it_atacked = []
        self.has_it_not_attacked = []
        self.killed_by_avalanche = []
        if card[7] == True:
            self.has_it_itattacked.append(card)
        elif card[7] == False:
            self.has_it_not_attacked.append(card)
        else:
            print('There was an error while sendind the card to attacked semetary')
        if card[8] == True:
            self.killed_by_avalanche.append(card)
        elif card[8] == False:
            pass
        else:
            print('There was an error while sendind the card to avalanche semetary')

import Player
import card
import power
import battlefield


class Deck():

    def __init__(self, player_name, deck_type, players_cards_ids):

        # Can be P1_deck or P1_hand (as so to others Ps) or Semetary types
      
        self.deck_player_name = player_name
        self.deck_type = deck_type  # Can be player_hand or player_full_deck     
        self.first_deck_of_cards = self.create_new_deck(players_cards_ids)

    def create_new_deck(self, player_cards_ids):

        self.set_of_cards_ids = player_cards_ids
        self.deck_of_cards = []

        for card_id in self.set_of_cards_ids:
            self.cards_on_deck = card.Card(card_id)     
            self.deck_of_cards.append(self.cards_on_deck)
            print("First deck of player: "+ str(self.deck_player_name)+"\n ->"
                                          +str(self.deck_of_cards))
        return self.deck_of_cards

    def __iter__(self):
        return self

    def add_card_to_deck(self,card_to_add):    
        pass

    def add_cards_to_battlefield():
        pass

    def evil_key():
        '''Exchange decks between a Player chosen by who use the evil_key and itself'''
        pass


class Semetary(Deck):
    def __init__(self, dead_card):
        super().__init__(self, self.deck_player_name, self.deck_type, self.deck_cards)
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

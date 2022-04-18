import deck
import battlefield
import card


'''
Player class - attributes and actions made by a players
of GoR
'''


class A_player:
    index_next_card_on_deck = 0
    num_cards_on_hand = 0
    player_cards_on_hand = []

    def __init__(self, player_name, player_cards_ids):
        self.player_name = player_name
        self.player_cards_ids = player_cards_ids
        self.first_players_deck_of_cards  = deck.Deck(player_name, 'player_full_deck',self.player_cards_ids)
        self.battlefield = battlefield.Battlefield(self.player_name)
        
    def player_cards_moves(self):    
        # Make Player's hand of cards:
        self.player_cards_on_hand = self.take_cards_from_deck(self.player_deck)
        # Show which cards are on players hands:
        self.player_hand = self.show_cards_on_hand(self.player_cards_on_hand)

    def take_cards_from_deck(self, player_deck):
        
        self.cards_on_hand = []
        ask_about_cards = input("Would you like to take cards to complete hand?(Y/N)")

        '''Tests how many cards are on players hand'''
        if ask_about_cards == 'Y' or 'y':
            '''Give to player only cards needed to complete 5 cards on hand'''
            cards_to_add_to_hand = 5 - self.num_cards_on_hand

            for new_card_taken in range(cards_to_add_to_hand):
                '''Take cards from first_deck previously created'''
                for cards_to_be_added in self.first_players_deck_of_cards:
                    card = card.Card('''somethin brought from deck''')
                    '''After create a Deck formed with those cards'''
                self.card_on_hand = deck.Deck(self.player_name, self.player_deck_ids, 'player_hand')
                self.index_next_card_on_deck = self.index_next_card_on_deck + cards_to_add_to_hand
                return( )

        elif take_cards == 'N' or 'n':
            '''Or take one card at a time'''
            return(self.player_deck[self.first_card_on_deck:
                                     self.first_card_on_deck
                                     + 1])
        else:
            print("Choose a valid option (Y/y or N/n)")
            self.take_cards_from_deck(self.player_deck)

        '''Refresh num_cards to next call'''
        self.num_cards_on_hand = cards_to_add_to_hand

    def show_cards_on_hand(self, cards_on_hand):
        cards_seen = []
        self.cards_on_hand_to_show = cards_on_hand
        cards_info = super().cards_data  # Copy cards_data
        '''For each card id on hand creates a new card'''
        for index, (key, value) in enumerate(self.players_names_and_decks.items()):
            cards_seen[index] = card.Card(cards_info[key])
            print("--Gathering of-------")
            print("-----Realms----------")
            print("--Realm:"+cards_seen[value][1]+"----")
            print("---------------------")
            print("--Id:"+cards_seen[value][0]+"--")
            print("--Name"+cards_seen[key]+"----")
            print("---------------------")
            print("--Attack"+cards_seen[value][1] + "----")
            print("--Deffense"+cards_seen[value][1]+"----")

    def show_players_battlefield(self):
        pass

    def player_move(self):
        pass

    def atack(self):
        pass

    def change_mode(self):
        pass

    def put_card_on_battlefield(self):
        pass

    def use_power():
        pass

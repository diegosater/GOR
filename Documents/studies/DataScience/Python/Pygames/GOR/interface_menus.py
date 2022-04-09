import sys
import random


class Menu:
    '''Display a menu and respond to choices when run.'''
    players_names = []
    number_of_players = 0
    deck_size_ids = list(range(55))
    list_of_cards_ids = []

    def __init__(self):
        self.choices = {
            "1": self.set_number_of_players,
            "2": self.write_players_names,
            "3": self.shuffle_cards,
            "4": self.start_game,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Gathering of Realms START Menu,
            Follow the sequence to play:
        1. Set Number of Players - 2 or 3
        2. Write Players names - name your army
        3. Shuffle cards - the catastrophe happens
        4. Start game - go to battlefield
        5. Quit
        """)

    def set_number_of_players(self):
        '''Sets the number of players of the Match'''
        self.number_of_players = input("Number of players: ")
        '''Test for invalid number of players and sets class variables'''
        if (self.number_of_players < '2') or (self.number_of_players > '3'):
            print("Number of players incorrect, please set it 2 or 3")
            self.set_number_of_players()

    def write_players_names(self):
        '''Build a list with Players names'''
        for i in range(int(self.number_of_players)):
            self.players_names.append(
                input("Type the name of Player number " + str(i+1)+":"))

    def shuffle_cards(self):
        ''' Shuffle the cards by user iteraction'''
        '''Cards Ids, all 54 '''
        random.shuffle(self.deck_size_ids)
        self.list_of_cards_ids = self.deck_size_ids
        #print(self.list_of_cards_ids)

    def start_game(self):
        '''Firstly we must divide the list of cards (full_deck) among each player'''
        ''' Total number of cards (54) divided by number of Players '''
        player_deck_size = int(54/int(self.number_of_players))
        for i in range(0, 54, player_deck_size):
            '''Secondly build up a structure (dictionary) to return to __init__'''
            players_data = {self.players_names[i]: self.list_of_cards_ids[i:i + player_deck_size]
                            for i in range(len(self.players_names))}
            return players_data

    def quit(self):
        '''Exit the game Menu'''
        sys.exit(0)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

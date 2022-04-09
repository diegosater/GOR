'''Remember the __init__.py file that defines a directory as a package? That file
can contain any variables or class declarations we like, and they will be available
as part of the package. In our example, if the ecommerce/__init__.py file
contained this line:
from .database import db
We could then access the db attribute from main.py or any other file using
this import:
from ecommerce import db
It might help to think of the __init__.py file as if it was an ecommerce.py file if that
file were a module instead of a package. This can also be useful if you put all your
code in a single module and later decide to break it up into a package of modules.
The __init__.py file for the new package can still be the main point of contact for
other modules talking to it, but the code can be internally organized into several
different modules or subpackages.'''
import Player
import interface_menus
import card
import power
import battlefield
import deck
import pprint
from tracemalloc import start
from turtle import end_fill
from typing import overload


#card_dict ={'character_name':[id,'realm',atack_value,defense_value, magic_power]
#is_hidden=False, mode='atack', has_attacked=False, avalanche=True}
cards_data = {'IRONION': [1, 'human', 500, 3000, 'win_smith', False, 'atack', False, False],
              'ABRATIKAN': [2, 'inhuman', 700, 300, 'show_hidden_cards', 'atack', False, False],
              'JRAMARJ': [3, 'betume', 1600, 900, 'change_modes', 'atack', False, False],
              'SOUTHER': [4, 'fire_devil', 2500, 1500, None, 'atack', False, False]
              }

realms_list = ['human', 'inhuman', 'betume', 'fire_devil']


class GOR():

    game_status = 'finished'

    def __init__(self, players_names):
        self.players_names = players_names
        for i, player in self.players_names:
            ''' Creates the Players to start the game'''
            self.players[i] = Player(players_names[i])
        if self.players:
            self.game_status = 'started'
        else:
            print("It seems something wrong occuren during creating players")
            GOR.self.game_status = 'finished'

#Define status of a battlefiled in a game
    def create_Players_deck():
        pass

    def create_battlefield():
        pass

    def get_result():
        pass


if __name__ == '__main__':
    '''Don't forget parenthesis after instanciate calls'''
    players_names = interface_menus.Menu().run()
    new_GOR_game = GOR(players_names)

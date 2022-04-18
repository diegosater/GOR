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


class GOR():
    
    game_status = 'finished'

    def __init__(self, **players_names_and_decks):
        self.players_names_and_decks = players_names_and_decks
        self.players_started = []
        for index, (key, value) in enumerate(self.players_names_and_decks.items()):
            ''' Creates the Players to start the game'''
            print("\nCreating Players..."+str(index)+
                   "\nPlayer's name : "+str(key)+
                   "\nPlayer's cards sent to Player class:"+str(value))
            new_player = Player.A_player(players_names_and_decks.keys(),
                                          players_names_and_decks.values())
            self.players_started.append(new_player)
            print("Cards created for player: {}".format(self.players_started[index]))
        if self.players_started:
            self.game_status = 'started'
        else:
            print("It seems something wrong occured during creating players")
            GOR.self.game_status = 'finished'

#Define status of a battlefiled in a game
    def get_result():
        pass


if __name__ == '__main__':
    '''Don't forget parenthesis after instanciate calls'''
    players_names_and_decks = interface_menus.Menu().run()
    # print(players_names_and_decks)
    new_GOR_game = GOR(**players_names_and_decks)  # dict{player_name:[deck_ids]}

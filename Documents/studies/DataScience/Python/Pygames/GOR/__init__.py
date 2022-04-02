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


import gor_main

#card_dict ={'character_name':[id,'realm',atack_value,defense_value, magic_power]}
cards_data = {'IRONION':[01,'human',500,3000,'win_smith'],
         'ABRATIKAN':[02,'inhuman',700,300,'show_hidden_cards'],
         'JRAMARJ':[03,'betume',1600,900,'change_modes'],
         'SOUTHER':[04,'fire_devil',2500,1500,None]
        }

realms_list = ['human','inhuman','betume','fire_devil']

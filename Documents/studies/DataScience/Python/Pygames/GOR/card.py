import deck

class Card():

    #card_dict ={'character_name':[id,'realm',atack_value,defense_value, magic_power]
    #is_hidden=False, mode='atack', has_attacked=False, avalanche=True}
    cards_data = {'IRONION': [0, 'human', 500, 3000, 'win_smith', False, 'atack', False, False],
                  'ABRATIKAN': [1, 'inhuman', 700, 300, 'show_hidden_cards', 'atack', False, False],
                  'JRAMARJ': [2, 'betume', 1600, 900, 'change_modes', 'atack', False, False],
                  'SOUTHER': [3, 'fire_devil', 2500, 1500, None, 'atack', False, False]
                  }
    realms_list = ['human', 'inhuman', 'betume', 'fire_devil']

    def __init__(self, card_id):

        self.card_id_to_be_created = card_id
        
        for key,value in enumerate(self.cards_data.items()):
            self.card_character_name = key
            if value[0] == self.card_id_to_be_created:
                self.card_id = value[0]
                self.realm = value[1]
                self.atack_value = value[2]
                self.defense_value = value[3]
                self.magic_power = value[4]
                self.is_hidden = value[5]
                self.mode = value[6]
                self.has_attacked = value[7]
                self.avalanche = value[8]
    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        self.other_card_character_name = other
        return self.card_character_name == self.other_card_character_name
    def __iter__(self):
        return self

    def show_card():

        pass

    def fusion(card_is_fused_with):
        Card.self.card_fused = card_is_fused_with
        #kill the original cards and makes a new one with powers added
        # change names to A fused B
        pass

    def hide_card():

        pass

    def show_card():
        pass



class Card():

    #card_dict ={'character_name':[id,'realm',atack_value,defense_value, magic_power]
    #is_hidden=False, mode='atack', has_attacked=False, avalanche=True}
    def __init__(self, card=[]):
        self.card_id = card[0]
        self.realm = card[1]
        self.atack_value = card[2]
        self.defense_value = card[3]
        self.magic_power = card[4]
        self.is_hidden = card[5]
        self.mode = card[6]
        self.has_attacked = card[7]
        self.avalanche = card[8]

    def fusion(card_is_fused_with):
        Card.self.card_fused = card_is_fused_with
        #kill the original cards and makes a new one with powers added
        # change names to A fused B
        pass

    def hide_card():

        pass

    def show_card():
        pass

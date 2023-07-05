
# Creates a Card class that has suit and value. Represents itself as a string "value of suit". Ex: "ace of spades"
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        suit_dict = {0:"spades", 1:"hearts", 2:"diamonds", 3:"clubs"}
        value_dict = {0:"ace", 1:"king", 2:"queen", 3:"jack", 4:"10", 5:"9", 6:"8", 7:"7", 8:"6", 9:"5", 10:"4", 11:"3", 12:"2"}
        suit_name = suit_dict[self.suit]
        value_name = value_dict[self.value]
        return value_name + " of " + suit_name
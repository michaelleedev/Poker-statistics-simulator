import Card
import random
from operator import *

# function used to determine if there is a straight
def isSequence(l):
    first = l[0]
    for i in range(1,5):
        if l[i] != first + 1:
            return False
        first = l[i]
    return True

# Deck class that creates deck of 52 cards and saves it as a list.
class Deck(list): 
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card.Card(i,j)) for j in values] for i in suits]

# shuffles the order of the deck list
    def shuffle(self):
        random.shuffle(self)

    
# picks five cards in front of the shuffled list and determines what the highest poker hand is.
# Returns a string of poker hand.
    def deal(self):
        hand = self[:5]
        suit_count = {}
        value_count = {}
        for x in hand:
            if x.value in value_count:
                value_count[x.value] += 1
            else:
                value_count[x.value] = 1
            
            if x.suit in suit_count:
                suit_count[x.suit] += 1
            else: 
                suit_count[x.suit] = 1
        l = sorted(list(value_count.keys()))
        if len(l) == 5:
            sequence = isSequence(l)
        else:
            sequence = False

        if sequence:
            if l[0] == 0 and len(suit_count) == 1:
                return "royal flush"
            elif len(suit_count) == 1:
                return "straight flush"
            else:
                return "straight"
        else:
            if len(suit_count) == 1:
                return "flush"
                
        if 4 in value_count.values():
            return "four of a kind"
        elif 3 in value_count.values():
            if 2 in value_count.values():
                return "full house"
            else:
                return "three of a kind"
        elif 2 in value_count.values():
            if countOf(value_count.values(), 2) == 2:
                return "two pairs"
            else:
                return "pair"
        else: 
            return "high card"
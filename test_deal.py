# for testing decision making 'deal' function


import unittest
from operator import *
import Card

def isSequence(l):
    first = l[0]
    for i in range(1,5):
        if l[i] != first + 1:
            return False
        first = l[i]
    return True

def deal(data):
    hand = data
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

class TestDeal(unittest.TestCase):
    def test_card_integrity(self):
        c = Card.Card(0,0)
        self.assertEqual(c.__repr__(), 'ace of spades')

    def test_deal_highCard(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,12), Card.Card(1,5), Card.Card(1, 8)]
        self.assertEqual(deal(data), 'high card')

    def test_deal_pair(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,0), Card.Card(1,5), Card.Card(1, 8)]
        self.assertEqual(deal(data), 'pair')

    def test_deal_twoPairs(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,0), Card.Card(1,4), Card.Card(1, 8)]
        self.assertEqual(deal(data), 'two pairs')
    
    def test_deal_threeOfaKind(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,0), Card.Card(1,0), Card.Card(1, 8)]
        self.assertEqual(deal(data), 'three of a kind')

    def test_deal_straight(self):
        data = [Card.Card(0,0), Card.Card(0,1), Card.Card(2,2), Card.Card(1,3), Card.Card(1, 4)]
        self.assertEqual(deal(data), 'straight')

    def test_deal_fullHouse(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,0), Card.Card(1,0), Card.Card(1, 4)]
        self.assertEqual(deal(data), 'full house')

    def test_deal_fourOfaKind(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(2,0), Card.Card(1,0), Card.Card(3, 0)]
        self.assertEqual(deal(data), 'four of a kind')

    def test_deal_flush(self):
        data = [Card.Card(0,0), Card.Card(0,4), Card.Card(0,5), Card.Card(0,9), Card.Card(0, 1)]
        self.assertEqual(deal(data), 'flush')

        data = [Card.Card(0,0), Card.Card(0,1), Card.Card(0,2), Card.Card(0,3), Card.Card(0, 9)]
        self.assertEqual(deal(data), 'flush')

    def test_deal_straightFlush(self):
        data = [Card.Card(0,12), Card.Card(0,11), Card.Card(0,10), Card.Card(0,9), Card.Card(0,8)]
        self.assertEqual(deal(data), 'straight flush')

        data = [Card.Card(0,12), Card.Card(0,9), Card.Card(0,11), Card.Card(0,8), Card.Card(0, 10)]
        self.assertEqual(deal(data), 'straight flush')
        
        data = [Card.Card(0,6), Card.Card(0,5), Card.Card(0,4), Card.Card(0,3), Card.Card(0, 2)]
        self.assertEqual(deal(data), 'straight flush')

    def test_deal_royalFlush(self):
        data = [Card.Card(0,0), Card.Card(0,1), Card.Card(0,2), Card.Card(0,3), Card.Card(0, 4)]
        self.assertEqual(deal(data), 'royal flush')

        data = [Card.Card(0,6), Card.Card(0,5), Card.Card(0,4), Card.Card(0,3), Card.Card(0, 2)]
        self.assertNotEqual(deal(data), 'royal flush')
        


if __name__ == '__main__':
    unittest.main()
    
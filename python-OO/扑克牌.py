#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
# ♠ ♥ ♦ ♣
# u'\U00002660',u'\U00002665',u'\U00002666',u'\U00002663'
Club, Diamond, Heart, Spade = Suit('Spade',u'\U00002660'), Suit('Diamond', u'\U00002666'), Suit('Heart', u'\U00002665'), Suit('Club', u'\U00002663')


cards = [AceCard('A', Spade), NumberCard('2', Diamond), NumberCard('3', Heart)]

def Card(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank),suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range!")

# deck = [Card(rank, suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade)]

# for card in deck:
#     print("rank is %s, suit is %s \n"%(card.rank, card.suit.symbol))
#
# print("The length is {}".format(len(deck)))

class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str={
            1:(AceCard, 'A'),
            11:(FaceCard, 'J'),
            12:(FaceCard, 'Q'),
            13:(FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self
    def suit(self, suit):
        return self.class_(self.rank_str, suit)

card = CardFactory()
deck = [card.rank(r+1).suit(s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]

for card in deck:
    print("rank is %s, suit is %s \n"%(card.rank, card.suit.symbol))

print("The length is {}".format(len(deck)))

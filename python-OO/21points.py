#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import random

class Card(object):
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

class NumberCard(Card):
    def __init__(self, rank, suit):
        super(NumberCard, self).__init__(str(rank), suit, rank, rank)

class AceCard(Card):
    def __init__(self, rank, suit):
        super(AceCard, self).__init__("A", suit, 1, 11)

class FaceCard(Card):
    def __init__(self, rank, suit):
        super(FaceCard, self).__init__({11: "J", 12: "Q", 13: "K"}[rank], suit, 10, 10)

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


# ♠ ♥ ♦ ♣
# u'\U00002660',u'\U00002665',u'\U00002666',u'\U00002663'
Spade, Diamond, Heart, Club = Suit('Spade',u'\U00002660'), Suit('Diamond', u'\U00002666'), Suit('Heart', u'\U00002665'), Suit('Club', u'\U00002663')


def Card(rank, suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    else:
        raise Exception("Rank out of range!")

class Deck(object):
    def __init__(self):
        self._cards = [Card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]
        random.shuffle(self._cards)
    def pop(self):
        return self._cards.pop()

class Deck2(list):
    def __init__(self):
        super(Deck2, self).__init__(Card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)

class Deck3(list):
    def __init__(self, decks=1):
        super().__init__()
        for i in range(decks):
            self.extend(Card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()

class Hand(object):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    def hard_total(self):
        return sum(c.hard for c in self.cards)
    def soft_total(self):
        return sum(c.soft for c in self.cards)


d = Deck3(decks=3)
# p = Hand(d.pop())
# p.cards.append(d.pop())
# p.cards.append(d.pop())
h = Hand(d.pop(), d.pop(), d.pop())
print(h.hard_total(), h.soft_total())

class GameStrategy:
    def insurance(self, hand):
        return False
    def split(self, hand):
        return False
    def double(self, hand):
        return False
    def hit(self, hand):
        return sum(c.hard for c in hand.cards) <= 17

dumb = GameStrategy()

print(dumb.insurance(h))

class Table(object):
    def __init__(self):
        self.deck = Deck3()
    def place_bet(self, amount):
        print("Bet", amount)
    def get_hand(self):
        try:
            self.hand = Hand(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except IndexError:
            self.deck = Deck3()
            return self.get_hand()
        print("Deal", self.hand)
        return self.hand
    def can_insure(self, hand):
        return hand.dealer_card.insure

class BettingStrategy(object):
    def bet(self):
        raise NotImplementedError("No bet method!")
    def record_win(self):
        pass
    def record_lose(self):
        pass

class Flat(BettingStrategy):
    def bet(self):
        return 1

class Hand3(object):
    def __init__(self, *args, **kw):
        if len(args)==1 and isinstance(args[0], Hand3):
            other = args[0]
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            dealer_card, *cards = args
            self.dealer_card = dealer_card
            self.cards = list(cards)

h = Hand(Deck3.pop(), Deck3.pop(), Deck3.pop())
memento = Hand(h)

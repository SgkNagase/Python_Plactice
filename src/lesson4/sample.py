# -*- coding: utf-8 -*-
from trump_card_data import Suits
from trump_card_data import Ranks
from trump_card_data import Hands
from trump_card_objects import TrumpCard
from trump_card_objects import Deck
from trump_card_objects import Player
from trump_card_objects import Hand


class Sample(object):
    def get_suits(self):
        suits = [
            Suits.SPADE,
            Suits.HEART,
            Suits.DIAMOND,
            Suits.CLUB,
        ]
        return suits

    def get_ranks(self):
        ranks = [
            Ranks.ONE,
            Ranks.TWO,
            Ranks.THREE,
            Ranks.FOUR,
            Ranks.FIVE,
            Ranks.SIX,
            Ranks.SEVEN,
            Ranks.EIGHT,
            Ranks.NINE,
            Ranks.TEN,
            Ranks.JACK,
            Ranks.QUEEN,
            Ranks.KING,
        ]
        return ranks

    def get_hands(self):
        hands = [
            Hands.STRAIGHT_FLUSH,
            Hands.FOUR_OF_A_KIND,
            Hands.FULL_HOUSE,
            Hands.FLUSH,
            Hands.STRAIGHT,
            Hands.THREE_OF_A_KIND,
            Hands.TWO_PAIR,
            Hands.ONE_PAIR,
            Hands.HIGH_CARD,
        ]
        return hands

    def set_trumpcard(self, rank, suit):
        TrumpCard.__init__(self, rank, suit)

    def set_deck(self, trump_cards):
        Deck.__init__(self, trump_cards)

    def set_player(self, trump_cards):
        Player.__init__(self, trump_cards)

    def set_hand(self, rank, name):
        Hand.__init__(self, rank, name)

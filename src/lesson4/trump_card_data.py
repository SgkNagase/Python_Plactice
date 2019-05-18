# -*- coding: utf-8 -*-
from trump_card_objects import Hand


class Suits(object):
    '''トランプカードのスーツが定義されています。
    '''
    SPADE = 'スペード'
    HEART = 'ハート'
    DIAMOND = 'ダイヤモンド'
    CLUB = 'クラブ'


class Ranks(object):
    '''トランプカードのランクが定義されています。
    '''
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Hands(object):
    '''ポーカーの役が定義されています。

    参考URL:
        https://www.pokerstars.com/ja/poker/games/rules/hand-rankings/
    '''
    STRAIGHT_FLUSH = Hand(1, 'ストレートフラッシュ')
    FOUR_OF_A_KIND = Hand(2, 'フォーカード')
    FULL_HOUSE = Hand(3, 'フルハウス')
    FLUSH = Hand(4, 'フラッシュ')
    STRAIGHT = Hand(5, 'ストレート')
    THREE_OF_A_KIND = Hand(6, 'スリーカード')
    TWO_PAIR = Hand(7, 'ツーペア')
    ONE_PAIR = Hand(8, 'ワンペア')
    HIGH_CARD = Hand(9, 'ハイカード')

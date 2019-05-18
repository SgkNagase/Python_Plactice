# -*- coding: utf-8 -*-


class TrumpCard(object):
    '''1枚のトランプカードを表すクラスです。
    '''

    def __init__(self, rank, suit):
        '''トランプカードを作成します。

        Args:
            rank (int): トランプカードのランク
            suit (int): トランプカードのスーツ

        Examples:
            TrumpCard(1, 'スペード')
        '''
        self.rank = rank
        self.suit = suit

    def __str__(self):
        '''文字列で表します。

        主にデバック用です。
        設定されている rank, suit を標準出力するときに使用します。

        Usage:
            trump_card = TrumpCard(1, 'スペード')
            print(trump_card)
        '''
        strings = []
        strings += ['ランク: {}'.format(self.rank)]
        strings += ['スーツ: {}'.format(self.suit)]
        return '; '.join(strings)


class Deck(object):
    '''トランプカードのデッキを表します。
    '''

    def __init__(self, trump_cards):
        '''デッキを作成します。

        Args:
            trump_cards (List): TrumpCardクラスを要素として持つリストです。
                                デッキの山札です。
        '''
        self.trump_cards = trump_cards

    def __str__(self):
        '''文字列で表します。

        主にデバック用です。
        trump_cards からカード枚数を標準出力するときに使用します。
        '''
        strings = []
        strings += ['トランプカード枚数: {}'.format(len(self.trump_cards))]
        return '\n'.join(strings)


class Player(object):
    '''ポーカーを行うときの手札を表します。
    '''

    def __init__(self, trump_cards):
        '''手札を初期化します。

        Args:
            trump_cards (List): TrumpCardクラスを要素として持つリストです。
                                手札のトランプカードを表します。

        Attributes:
            hand (str): 手札のトランプカードから決定されたポーカーの役を設定します。
        '''
        self.trump_cards = trump_cards
        self.hand = None

    def __str__(self):
        '''文字列で表します。

        主にデバック用です。
        設定されている trump_cards, hand を標準出力するときに使用します。
        '''
        strings = []
        strings = ['手札のトランプカード:']
        strings += ['  ' + str(trump_card) for trump_card in self.trump_cards]
        strings += ['役: {}'.format(self.hand)]
        return '\n'.join(strings)


class Hand(object):
    def __init__(self, rank, name):
        '''ポーカー役を表します。

        Args:
            rank (int): ポーカーの役のランクです。数値が低いが方がランクが高いです。
            name (str): ポーカーの役の名前です。
        '''
        self.rank = rank
        self.name = name

    def __str__(self):
        '''文字列で表します。

        主にデバック用です。
        設定されている rank, name, を標準出力するときに使用します。
        '''
        strings = []
        strings += ['ランク: {}'.format(self.rank)]
        strings += ['役: {}'.format(self.name)]
        return '\n'.join(strings)

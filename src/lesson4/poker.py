# -*- coding: utf-8 -*-
'''
課題4に矛盾が多い為、形だけ作成
 →修正は課題4の内容が明確になってから
'''

import sys
import random

from sample import Sample


class Poker(object):
    def __init__(self):
        '''変数を初期化します
        '''
        self.deck = None
        self.player1 = None
        self.player2 = None

    def execute_sample(self):
        '''モジュールやクラスを分ける場合のサンプルコードです
        '''
        suits = Sample().get_suits()
        return suits

    def create_deck(self):
        '''Lesson4-1
        '''
        # カウント用変数初期化
        i = 0
        j = 0

        # デッキ用リストを初期化
        DECK = []

        try:
            # スーツをリスト化
            Suits = Sample().get_suits()
            # ランクをリスト化
            Ranks = Sample().get_ranks()

            # カードを設定
            while i < 4:
                while j < 13:
                    Sample().set_trumpcard(Ranks[j], Suits[i])
                    DECK.append([Ranks[j], Suits[i]])
                    j += 1
                i += 1
                j = 0

            # デッキを設定
            Sample().set_deck(DECK)

            # 設定
            self.deck = DECK

        except ValueError:
            # 強制終了
            sys.exit()

    def draw_five_cards(self):
        '''Lesson4-2
        '''
        i = 0
        P1 = []
        P2 = []

        try:
            # デッキをシャッフル
            MainDeck = random.sample(self.deck, len(self.deck))

            # カードを配る
            while i < 10:
                if(i % 2 == 0):
                    P1.append(MainDeck[i])
                elif(i % 2 == 1):
                    P2.append(MainDeck[i])
                i += 1

            return (P1, P2)

        except ValueError:
            # 強制終了
            sys.exit()

    def setup_players(self):
        '''Lesson4-3
        '''
        P_Card = []
        global P1_Rank
        global P2_Rank

        try:
            # draw_five_cardsを呼び出し
            P_Card = poker.draw_five_cards()

            # プレイヤー１の設定
            Sample().set_player(P_Card[0])
            self.player1 = P_Card[0]

            # プレイヤー２の設定
            Sample().set_player(P_Card[1])
            self.player2 = P_Card[1]

            # check_handsを呼び出し
            P1Hand = poker.check_hands(self.player1)
            Sample().set_hand(P1Hand[0], P1Hand[1])
            Hands = Sample().get_hands()
            for P1 in Hands:
                if P1.name == P1Hand[1]:
                    P1_Rank = P1.rank

            P2Hand = poker.check_hands(self.player2)
            Sample().set_hand(P2Hand[0], P2Hand[1])
            Hands = Sample().get_hands()
            for P2 in Hands:
                if P2.name == P2Hand[1]:
                    P2_Rank = P2.rank

            # judge_winnerを呼び出し
            WIN = poker.judge_winner()

            if WIN == 0:
                print("引き分け")
            elif WIN == 1:
                print("プレイヤー１の勝ち")
            elif WIN == 2:
                print("プレイヤー２の勝ち")

        except ValueError:
            # 強制終了
            sys.exit()

    def check_hands(self, Card):
        '''Lesson4-4
        '''
        # 初期化
        Rank = 0
        Name = ""

        # 判定の為ソート
        Card.sort()

        try:
            # ロイヤルストレートフラッシュ
            # ストレートフラッシュ
            '''
            9-8=1 and 8-7=1 and 7-6=1 and 6-5=1
            全て同じスーツ
            '''
            if((Card[4][0] - Card[3][0]) == 1 and
               (Card[3][0] - Card[2][0]) == 1 and
               (Card[2][0] - Card[1][0]) == 1 and
               (Card[1][0] - Card[0][0]) == 1) and\
              (Card[0][1] ==
               Card[1][1] ==
               Card[2][1] ==
               Card[3][1] ==
               Card[4][1]):
                Rank = 1
                Name = "ストレートフラッシュ"
                return (Rank, Name)

            # フォーカード
            '''
            13=13=13=13
            '''
            if(Card[0][0] ==
               Card[1][0] ==
               Card[2][0] ==
               Card[3][0]) or\
              (Card[1][0] ==
               Card[2][0] ==
               Card[3][0] ==
               Card[4][0]):
                Rank = 2
                Name = "フォーカード"
                return (Rank, Name)

            # フルハウス
            '''
            12=12=12 and 10=10 or 12=12 and 10=10=10
            '''
            if(Card[0][0] ==
               Card[1][0] ==
               Card[2][0]) and\
              (Card[3][0] ==
               Card[4][0]) or\
              (Card[0][0] ==
               Card[1][0]) and\
              (Card[2][0] ==
               Card[3][0] ==
               Card[4][0]):
                Rank = 3
                Name = "フルハウス"
                return (Rank, Name)

            # フラッシュ
            '''
            全て同じスーツ
            '''
            if(Card[0][1] ==
               Card[1][1] ==
               Card[2][1] ==
               Card[3][1] ==
               Card[4][1]):
                Rank = 4
                Name = "フラッシュ"
                return (Rank, Name)

            # ストレート
            '''
            6-5=1 and 5-4=1 and 4-3=1 and 3-2=1
            '''
            if((Card[4][0] - Card[3][0]) == 1 and
               (Card[3][0] - Card[2][0]) == 1 and
               (Card[2][0] - Card[1][0]) == 1 and
               (Card[1][0] - Card[0][0]) == 1):
                Rank = 5
                Name = "ストレート"
                return (Rank, Name)

            # スリーカード
            '''
            11=11=11
            '''
            if(Card[0][0] ==
               Card[1][0] ==
               Card[2][0]) or\
              (Card[2][0] ==
               Card[3][0] ==
               Card[4][0]):
                Rank = 6
                Name = "スリーカード"
                return (Rank, Name)

            # ツーペア
            '''
            6=6 and 10=10
            '''
            if(Card[0][0] ==
               Card[1][0]) and\
              (Card[2][0] ==
               Card[3][0]) or\
              (Card[0][0] ==
               Card[1][0]) and\
              (Card[3][0] ==
               Card[4][0]):
                Rank = 7
                Name = "ツーペア"
                return (Rank, Name)

            # ワンペア
            '''
            13=13
            '''
            if(Card[0][0] ==
               Card[1][0]) or\
              (Card[1][0] ==
               Card[2][0]) or\
              (Card[2][0] ==
               Card[3][0]) or\
              (Card[3][0] ==
               Card[4][0]):
                Rank = 8
                Name = "ワンペア"
                return (Rank, Name)

            # ハイカード
            if Rank == 0 and Name == "":
                Rank = 9
                Name = "ハイカード"
                return (Rank, Name)

        except ValueError:
            # 強制終了
            sys.exit()

    def judge_winner(self):
        '''Lesson4-5
        '''
        if P1_Rank < P2_Rank:
            return 1
        elif P1_Rank > P2_Rank:
            return 2
        elif P1_Rank == P2_Rank:
            return 0


if __name__ == '__main__':
    poker = Poker()
    print(poker.execute_sample())

    # create_deckを呼び出し
    poker.create_deck()
    # setup_playersを呼び出し
    poker.setup_players()

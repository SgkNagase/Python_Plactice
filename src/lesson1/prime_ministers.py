# -*- coding: utf-8 -*-
import collections


PRIME_MINISTERS = [
    ('うの', 'そうすけ'),
    ('かいふ', 'としき'),
    ('みやざわ', 'きいち'),
    ('ほそかわ', 'もりひろ'),
    ('はた', 'つとむ'),
    ('むらやま', 'とみいち'),
    ('はしもと', 'りゅうたろう'),
    ('おぶち', 'けいぞう'),
    ('もり', 'よしろう'),
    ('こいずみ', 'じゅんいちろう'),
    ('あべ', 'しんぞう'),
    ('ふくだ', 'やすお'),
    ('あそう', 'たろう'),
    ('はとやま', 'ゆきお'),
    ('かん', 'なおと'),
    ('のだ', 'よしひこ'),
    ('あべ', 'しんぞう'),
]

# *****修正開始*****
# 空リスト作成
'''GET_AS_STRING = []
   GET_WITH_REVERSE_ORDER = []
   GET_PRIME_MINISTERS_OF_MIN_LENGTH = []

   # 処理用
   list1 = []
   list2 = {}
'''
# *****修正終了*****


class PrimeMinisters(object):
    def order_by_last_name(self):
        '''Tutorial
        '''
        prime_ministers = sorted(PRIME_MINISTERS)
        return prime_ministers

    def get_as_string(self):
        '''Lesson1-1
        '''
        # リスト内の文字列に空白を追加し、リストに追加
# *****修正開始*****
        '''for K, V in PRIME_MINISTERS:
            GET_AS_STRING.append(K + " " + V)
        '''
        # 空リスト作成
        GET_AS_STRING = []

        for p_m in PRIME_MINISTERS:
            GET_AS_STRING.append(p_m[0] + " " + p_m[1])
# *****修正終了*****

        return GET_AS_STRING

    def order_by_fisrt_name(self):
        '''Lesson1-2
        '''
        # 名前順にソート
        ORDER_BY_FISRT_NAME = sorted(PRIME_MINISTERS, key=lambda x: x[1])

        return ORDER_BY_FISRT_NAME

    def get_with_reverse_order(self):
        '''Lesson1-3
        '''
        # 名前の文字数が名字の文字数より多い場合、リストに追加
# *****修正開始*****
        '''for k, v in PRIME_MINISTERS:
               if len(k) < len(v):
                   GET_WITH_REVERSE_ORDER.append((k, v))
        '''
        # 空リスト作成
        GET_WITH_REVERSE_ORDER = []

        for p_m in PRIME_MINISTERS:
            if len(p_m[0]) < len(p_m[1]):
                GET_WITH_REVERSE_ORDER.append((p_m[0], p_m[1]))
# *****修正終了*****

        return GET_WITH_REVERSE_ORDER

    def get_prime_ministers_of_min_length(self):
        '''Lesson1-4
        '''
# *****修正開始*****
        '''# 文字数カウント用
           COUNT = 0

           # 最大文字数取得
           for k, v in PRIME_MINISTERS:
               if COUNT < (len(k) + len(v)):
                   COUNT = (len(k) + len(v))

           # 最大文字数対象をリストに追加
           for k, v in PRIME_MINISTERS:
               if COUNT == (len(k) + len(v)):
                   GET_∂PRIME_MINISTERS_OF_MIN_LENGTH.append((k, v))
        '''
        # 空リスト作成
        GET_PRIME_MINISTERS_OF_MIN_LENGTH = []
        # 文字数カウント用
        COUNT = 100

        # 最小文字数取得
        for p_m in PRIME_MINISTERS:
            if COUNT > (len(p_m[0]) + len(p_m[1])):
                COUNT = (len(p_m[0]) + len(p_m[1]))

        # 最小文字数対象をリストに追加
        for p_m in PRIME_MINISTERS:
            if COUNT == (len(p_m[0]) + len(p_m[1])):
                GET_PRIME_MINISTERS_OF_MIN_LENGTH.append((p_m[0], p_m[1]))
# *****修正終了*****

        return GET_PRIME_MINISTERS_OF_MIN_LENGTH

    def remove_duplication(self):
        '''Lesson1-5
        '''
# *****修正開始*****
        '''for k, v in PRIME_MINISTERS:
               list1.append(k[0:1])
        '''
        # 処理用
        list1 = []
        list2 = {}
        list3 = []

        # 対象の苗字から１文字取得
        for p_m in PRIME_MINISTERS:
            list1.append(p_m[0][0:1])

        # 重複対象の集約
        list2 = dict(collections.Counter(list1).most_common(None))

        # 重複しない対象を抽出
        for l2 in list2.items():
            if l2[1] == 1:
                for p_m in PRIME_MINISTERS:
                    if l2[0] == (p_m[0][0:1]):
                        list3.append((p_m[0], p_m[1]))

        return list3
# *****修正終了*****


if __name__ == '__main__':
    # クラスをインスタンス化
    prime_ministers = PrimeMinisters()

    # order_by_last_name呼び出し
    print(prime_ministers.order_by_last_name())

    # get_as_string呼び出し
    print("課題1-1")
    print(prime_ministers.get_as_string())

    # order_by_fisrt_name呼び出し
    print("課題1-2")
    print(prime_ministers.order_by_fisrt_name())

    # get_with_reverse_order呼び出し
    print("課題1-3")
    print(prime_ministers.get_with_reverse_order())

    # get_prime_ministers_of_min_length呼び出し
    print("課題1-4")
    print(prime_ministers.get_prime_ministers_of_min_length())

    # remove_duplication呼び出し
    print("課題1-5")
    print(prime_ministers.remove_duplication())

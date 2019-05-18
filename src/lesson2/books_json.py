# -*- coding: utf-8 -*-

import os
import json
import shutil
import os.path


class BooksJson(object):
    def __init__(self, json_path):
        '''変数の初期値を設定します。
        Args:
            json_path(str): 読み込むJSONファイルのパスです。
                            例は、'./input/夏目漱石.json' です。
        '''
        self.json_path = json_path
        self.items = None

    def get_items(self):
        '''Lesson2-1
        '''
        # 選択したファイルを読み込み
        OPEN_FILE = open(self.json_path, 'r')
        # データを格納
        self.items = json.load(OPEN_FILE)

    def delete_unnecessary_data(self):
        '''Lesson2-2
        '''
        # flake8(E501)回避
        It = "items"
        Vo = "volumeInfo"
        De = "description"
        Pa = "pageCount"

        # カウント初期化
        i = 0

        while i < len(self.items[It]):
            # self.items["items"][i]["volumeInfo"]["description"]の存在チェック
            if De in self.items[It][i][Vo]:
                # データがある場合、空白を設定
                if not self.items[It][i][Vo][De] == "":
                    self.items[It][i][Vo][De] = ""

            # self.items["items"][i]["volumeInfo"]["pageCount"]の存在チェック
            if Pa in self.items[It][i][Vo]:
                # データがある場合、空白を設定
                if not self.items[It][i][Vo][Pa] == "":
                    self.items[It][i][Vo][Pa] = ""

            # カウントアップ
            i += 1

    def add_elapsed_years(self):
        '''Lesson2-3
        '''
        # flake8(E501)回避
        It = "items"
        Vo = "volumeInfo"
        Pu = "publishedDate"
        El = "elapsed_years "

        # カウント初期化
        i = 0

        while i < len(self.items[It]):
            # self.items["items"][i]["volumeInfo"]["publishedDate"]の存在チェック
            if Pu in self.items[It][i][Vo]:
                # 文字数が１０の場合
                if len(self.items[It][i][Vo][Pu]) == 10:
                    self.items[It][i][Vo][El] = self.items[It][i][Vo][Pu]
                    # 文字数が７の場合
                elif len(self.items[It][i][Vo][Pu]) == 7:
                    self.items[It][i][Vo][El] = self.items[It][i][Vo][Pu] \
                        + "-01"
                # 文字数が４の場合
                elif len(self.items[It][i][Vo][Pu]) == 4:
                    self.items[It][i][Vo][El] = self.items[It][i][Vo][Pu] \
                        + "-01-01"
                # 例外
                else:
                    print("エラー2")
                    pass
            else:
                # ["publishedDate"]が存在しない場合
                self.items[It][i][Vo][El] = "-1"

            # カウントアップ
            i += 1

    def export(self):
        '''Lesson2-4
        '''
        global OUTPUT

        # flake8(E501)回避
        It = "items"

        # カウント初期化
        i = 0

        # 出力用ディレクトリ削除
        if os.path.exists(OUTPUT):
            shutil.rmtree(OUTPUT)

        # 出力用ディレクトリ作成
        os.mkdir(OUTPUT)

        # 出力データ作成
        while i < len(self.items[It]):
            OUTFILE = open(OUTPUT + str(i + 1).zfill(2) + ".json", 'w')
            json.dump(self.items[It][i], OUTFILE)

            # カウントアップ
            i += 1


'''初期宣言
'''
Select = 0
Name_A = "芥川龍之介"
Name_N = "夏目漱石"
Name_M = "宮沢賢治"
json_data = os.path.dirname(__file__)

# インスタンス化
books = BooksJson(object)

'''初期処理
'''
# 読み込むファイルを指定
print("どの文字に追加したいですか？")
Select = int(input("0:{0},1:{1},2{2}>".format(Name_A,
                                              Name_N,
                                              Name_M)))

# 読み込みファイルのパスを作成
if Select == 0:
    json_path = json_data + "/input/" + Name_A + ".json"
    OUTPUT = json_data + "/input/" + Name_A + "/"
elif Select == 1:
    json_path = json_data + "/input/" + Name_N + ".json"
    OUTPUT = json_data + "/input/" + Name_N + "/"
elif Select == 2:
    json_path = json_data + "/input/" + Name_M + ".json"
    OUTPUT = json_data + "/input/" + Name_M + "/"
else:
    print("エラー1")

'''主処理
'''
# path設定
books.__init__(json_path)
# get_items呼び出し
print("課題2-1")
books.get_items()
# delete_unnecessary_data呼び出し
print("課題2-2")
books.delete_unnecessary_data()
# dd_elapsed_years呼び出し
print("課題2-3")
books.add_elapsed_years()
# export呼び出し
print("課題2-4")
books.export()

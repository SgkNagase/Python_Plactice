# -*- coding: utf-8 -*-
import sqlite3
import csv
import os.path
import os
import sys
import world_happiness_report

# ***** データベース ***** #
DB_Directory = os.path.dirname(__file__) + "/"
DB_Name = "world_happiness_report.db"
SQLite = ""

# ***** クエリ ***** #
Query1 = "SELECT * FROM world_happiness_report"
Query2 = "DROP TABLE world_happiness_report"
Query3 = "CREATE TABLE "\
         "world_happiness_report"\
         "("\
         "id INTEGER PRIMARY KEY unique,"\
         "country TEXT unique,"\
         "region  TEXT,"\
         "happiness_rank INTEGER,"\
         "happiness_score REAL"\
         ")"
Query4 = ""
Query5 = "SELECT * FROM "\
         "world_happiness_report "\
         "WHERE "\
         "region = 'Eastern Asia' or "\
         "region = 'Southeastern Asia' "\
         "ORDER BY "\
         "happiness_rank desc "\
         "limit 5"
Query6 = "DELETE FROM "\
         "world_happiness_report "\
         "WHERE region = 'Central and Eastern Europe' "\
         "OR region = 'Western Europe'"
Query6_1 = "SELECT COUNT(*) FROM "\
          "world_happiness_report "\
          "WHERE region = 'Central and Eastern Europe' "\
          "OR region = 'Western Europe'"
Query7 = "UPDATE world_happiness_report "\
         "SET happiness_rank = ('%s') "\
         "WHERE id = ('%s')"
Query7_1 = "SELECT id, happiness_rank FROM world_happiness_report"

# ***** CSV ***** #
CSV_Directory = os.path.dirname(__file__) + "/"
CSV_Name = "2016.csv"
CSV_LIST = []


class Main(object):
    def create_table(self):
        '''Lesson3-1
        '''
        # テーブル作成
        try:
            # 対象のテーブルが存在するか確認
            DB.execute(Query1)
            # 対象のテーブル削除
            DB.execute(Query2)
            # 対象のテーブル作成
            DB.execute(Query3)

        except sqlite3.Error:
            # 対象テーブルが存在しない
            try:
                # 対象のテーブル作成
                DB.execute(Query3)

            except sqlite3.Error:
                print("エラー１")
                # ロールバック
                DB.rollback()
                # DBを閉じる
                DB.close()
                # 強制終了
                sys.exit()

        # コミット
        SQLite.commit()

    def insert_csv_data(self):
        '''Lesson3-2
        '''
        # CSVの存在チェック
        if not os.path.exists(CSV_Directory + CSV_Name):
            print("CSVが存在しません")
            # DBを閉じる
            SQLite.close()
            # 強制終了
            sys.exit()

        else:
            # CSVファイルを開く
            with open(CSV_Directory + CSV_Name, 'r') as CSV_FILE:
                DATA_READER = csv.reader(CSV_FILE)
                for DATA in DATA_READER:
                    # CSVの１行目はスルー
                    if DATA_READER.line_num == 1:
                        continue

                    # データを対象テーブルにインサート
                    Query4 = "INSERT INTO "\
                             "world_happiness_report "\
                             "VALUES("\
                             "" + DATA[0] + ","\
                             "'" + DATA[1] + "',"\
                             "'" + DATA[2] + "',"\
                             "" + DATA[3] + ","\
                             "'" + DATA[4] + "')"

                    # クエリ実行
                    try:
                        # インサート
                        DB.execute(Query4)

                    except sqlite3.Error:
                        print("エラー2")
                        # ロールバック
                        SQLite.rollback()
                        # DBを閉じる
                        SQLite.close()
                        # 強制終了
                        sys.exit()

            # コミット
            SQLite.commit()

    def select_top_five_in_asia(self):
        '''Lesson3-3
        '''
        # クエリ実行
        for Limit5 in DB.execute(Query5):
            # 別関数にデータを設定
            WHR.__init__(self,
                         Limit5[0],
                         Limit5[1],
                         Limit5[2],
                         Limit5[3],
                         Limit5[4])
            # 戻り値確認
            print("-----------------------------\n" + WHR.__str__(self))

    def delete_european_countries(self):
        '''Lesson3-4
        '''
        try:
            # 削除前件数確認
            for Count in DB.execute(Query6_1):
                print("削除前の件数：{0}".format(Count[0]))

            # 対象データ削除
            DB.execute(Query6)

            # 削除後件数確認
            for Count in DB.execute(Query6_1):
                print("削除後の件数：{0}".format(Count[0]))

        except sqlite3.Error:
            print("エラー3")
            # ロールバック
            SQLite.rollback()
            # DBを閉じる
            SQLite.close()
            # 強制終了
            sys.exit()

        # コミット
        SQLite.commit()

    def update_happiness_rank(self):
        '''Lesson3-5
        '''
        try:
            # 初期化
            SetData = []

            # 変更前データ確認
            for Select in DB.execute(Query7_1):
                print("{0}|{1}".format(Select[0],
                                       Select[1]))
                SetData.append(Select)

            # UPDATE
            for i, Set in enumerate(SetData):
                DB.execute(Query7 % (i + 1, Set[0]))

            # 変更後データ確認
            for Select in DB.execute(Query7_1):
                print("{0}|{1}".format(Select[0],
                                       Select[1]))

        except sqlite3.Error:
            print("エラー4")
            # ロールバック
            SQLite.rollback()
            # DBを閉じる
            SQLite.close()
            # 強制終了
            sys.exit()

        # コミット
        SQLite.commit()


'''初期宣言
'''
# インスタンス化
MAIN = Main()
WHR = world_happiness_report.WorldHappinessReport

'''初期処理
'''
# DBの存在チェック
if not os.path.exists(DB_Directory + DB_Name):
    # DBが存在しない場合作成
    sqlite3.connect(DB_Directory + DB_Name)

# DB指定
SQLite = sqlite3.connect(DB_Directory + DB_Name)

# DBオブジェクト作成
DB = SQLite.cursor()

'''主処理
'''
# create_table呼び出し
print("課題3-1")
MAIN.create_table()
# insert_csv_data呼び出し
print("課題3-2")
MAIN.insert_csv_data()
# select_top_five_in_asia呼び出し
print("課題3-3")
MAIN.select_top_five_in_asia()
# delete_european_countries呼び出し
print("課題3-4")
MAIN.delete_european_countries()
# update_happiness_rank呼び出し
print("課題3-5")
MAIN.update_happiness_rank()

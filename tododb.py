import sqlite3
import datetime
import re
import time

DEFAULT = {"title": "Noname", "limit_at": "2999/12/31 23:59",
           "update_at": "2000/01/01 0:00", "status": "未", "noticetime":3}
DEFAULT_TYPE = {"title": "text NOT NULL", "limit_at": "text",
                "update_at": "text NOT NULL", "status": "text", "noticetime":"integer NOT NULL"}


class DB(object):
    def __init__(self, name):
        self.__conn = sqlite3.connect(name)
        self.__c = self.__conn.cursor()

    def __create_table(self):
        keys = DEFAULT.keys()
        msg = "(id integer NOT NULL PRIMARY KEY AUTOINCREMENT"
        for key in keys:
            if key == "id":
                continue
            msg += f",{key} {DEFAULT_TYPE[key]}"
        msg += ")"
        self.__c.execute(f"create table todo {msg}")

    def __drop_table(self):
        self.__c.execute("drop table todo")

    def init(self):
        self.__create_table()

    def reset(self):
        self.__drop_table()
        self.__create_table()

    
    # idでデータを取得してdict形式で返す
    # idが存在しない値であるときは全要素Noneで返すので注意
    def select_id(self, id):
        dict_list = []
        columns = self.__conn.execute("select * from todo").description
        for r in self.__c.execute(f"select * from todo where id=={id}"):
            item = list(map(str, r))
            dict = {}
            for i in range(len(columns)):
                dict[columns[i][0]] = item[i]
                i += 1
            dict_list.append(dict)
        if len(dict_list) == 0:
            dict = {}
            for i in range(len(columns)):
                dict[columns[i][0]] = None
                i += 1
            dict_list.append(dict)
        return dict_list[0]


    # 追加するデータをdictionaryで受け取る
    # 引数 (self,追加したいデータ)
    def add_dict(self, dict):
        # 基本としてデフォルトを読み込む
        newdata = {}
        for key in DEFAULT.keys():
            newdata[key] = DEFAULT[key]
        dict_items = dict.items()
        # dictの中身をnewdataに上書き
        for item in dict_items:
            if item[0] in newdata.keys():
                newdata[item[0]] = item[1]
        # ここで、limit_atがちゃんとフォーマットにあっているか見る
        if not re.match(r'^\d{4}/\d{2}/\d{2} \d{1,2}:\d{2}$', newdata["limit_at"]):
            newdata["limit_at"] = DEFAULT["limit_at"]
        # 現在時刻取得
        update_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # sql文を作文
        msg1 = "insert into todo ("
        msg2 = "values("
        datalist = []
        for tag in newdata.keys():
            if tag == "update_at":
                continue
            msg1 += f"{tag},"
            msg2 += "?,"
            datalist.append(newdata[tag])
        msg1 += "update_at)"
        msg2 += "?)"
        datalist.append(update_at)
        sql = msg1+msg2
        self.__c.execute(sql, datalist)
        self.__conn.commit()


    def change_id(self, id, column, value):
        """idを指定してcolumnの値をvalueに変更
        """
        sql = f'UPDATE todo SET {column} = "{value}" WHERE id = {id}'
        self.__c.execute(sql)
        self.__conn.commit()


    def add(self, title, limit_at):
        update_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.add_dict({"title":title,"limit_at":limit_at,"update_at":update_at})


    def list(self):
        str_list = "TODO list:\n"
        for r in self.__c.execute("select * from todo"):
            str_list += ', '.join(map(str, r))
            str_list += '\n'
        return str_list


    def dict_list(self):
        dict_list = []
        columns = self.__conn.execute("select * from todo").description
        for i in range(20):
            fromnum = i*50+1
            tonum = (i+1)*50
            for r in self.__c.execute(f"select * from todo WHERE id BETWEEN {fromnum} and {tonum}"):
                item = list(map(str, r))
                dict = {}
                for i in range(len(columns)):
                    dict[columns[i][0]] = item[i]
                    i += 1
                dict_list.append(dict)
        return dict_list


    def search(self, column, text):
        """columnの値にtextが含まれる場合そのデータをlist形式(要素はdict形式)で返す

        マッチするものがない場合、空のリストで返す
        """
        matched = []
        dict_list = self.dict_list()
        text_compile = re.compile(text)
        for dict in dict_list:
            value = dict[column]
            if text_compile.search(value):
                matched.append(dict)
        return matched



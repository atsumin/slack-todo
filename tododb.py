import sqlite3
import datetime
import re

DEFAULT = {"title": "Noname", "limit_at": "2999/12/31 23:59",
           "update_at": "2000/01/01 0:00", "status": "未"}
DEFAULT_TYPE = {"title": "text NOT NULL", "limit_at": "text",
                "update_at": "text NOT NULL", "status": "text"}


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


    def add(self, title, limit_at):
        update_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.add_dict({"title":title,"limit_at":limit_at,"update_at":update_at})


    def list(self):
        str_list = "TODO list:\n"
        for r in self.__c.execute("select * from todo"):
            str_list += ', '.join(map(str, r))
            str_list += '\n'
        return str_list



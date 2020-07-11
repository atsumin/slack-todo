import sqlite3
import datetime

class DB(object):
    def __init__(self, name):
        self.__conn = sqlite3.connect(name)
        self.__c = self.__conn.cursor()

    def __create_table(self):
        self.__c.execute("create table todo" \
                         "(id integer NOT NULL PRIMARY KEY AUTOINCREMENT, " \
                          "title text NOT NULL, limit_at text, update_at text NOT NULL)")

    def __drop_table(self):
        self.__c.execute("drop table todo")

    def init(self):
        self.__create_table()

    def reset(self):
        self.__drop_table()
        self.__create_table()

    def add(self, title, limit_at):
        update_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into todo (title, limit_at, update_at) values (?, ?, ?)"
        self.__c.execute(sql, [title, limit_at, update_at])
        self.__conn.commit()

    def list(self):
        str_list = "TODO list:\n"
        for r in self.__c.execute("select * from todo"):
            str_list += ', '.join(map(str, r))
            str_list += '\n'
        return str_list



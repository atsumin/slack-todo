from tododb import DB
import os

dbname = os.environ['TODO_DB']
database = DB(dbname)
if not os.path.exists(dbname):
    database.init()

database.add('test-title1', '2020-06-01')
database.list()

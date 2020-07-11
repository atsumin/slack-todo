from slackbot.bot import Bot
from tododb import DB
import os

dbname = os.environ['TODO_DB']
db = DB(dbname)
if not os.path.exists(dbname):
    db.init()

mybot = Bot()
mybot.run()

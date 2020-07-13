from slacker import Slacker
from slackbot.bot import Bot
from tododb import DB
import os

slack = Slacker(os.environ['API_TOKEN'])
channel = os.environ['SLACK_CHANNEL']
slack.chat.post_message(channel, 'new version bot is deployed.', as_user=True)

dbname = os.environ['TODO_DB']
need_init = not os.path.exists(dbname)
database = DB(dbname)
if need_init:
    database.init()

mybot = Bot()
mybot.run()

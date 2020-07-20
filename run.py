from slacker import Slacker
from slackbot.bot import Bot
from tododb import DB
import os

slack = Slacker(os.environ['API_TOKEN'])
channel = os.environ['SLACK_CHANNEL']
slack.chat.post_message(channel, 'new version bot is deployed.', as_user=True)

dbname = os.environ['TODO_DB']

if not os.path.exists(dbname):
    db = DB(dbname)
    db.init()
else:
    db = DB(dbname)

mybot = Bot()
mybot.run()

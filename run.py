from slacker import Slacker
from slackbot.bot import Bot
from tododb import DB
import os

slack = Slacker(os.environ['API_TOKEN'])
channel = os.environ['SLACK_CHANNEL']
slack.chat.post_message(channel, 'new version bot is deployed.', as_user=True)

dbname = os.environ['TODO_DB']
db = DB(dbname)
if not os.path.exists(dbname):
    db.init()

mybot = Bot()
mybot.run()

from slackbot.bot import respond_to
from slackbot.bot import listen_to

import datetime
@respond_to('今何時？')
def mention_func(message):
  dt_now = datetime.datetime.now()
  message.reply(dt_now.strftime('%H時%M分') + 'です')

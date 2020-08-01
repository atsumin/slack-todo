from slackbot.bot import respond_to
import calendar
from datetime import datetime

@respond_to('^カレンダー$')
def calendar_test(message):


    today = datetime.today()
    month = today.month
    year = today.year


    output = '```' + calendar.month(year, month) + '```'

    message.send(output)
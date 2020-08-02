import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to


def dice(num,m):
    mess = ""
    h = 0
    for i in range(num):
         f = random.randint(1,m)
         h = h + f
         if i==0:
             mess = "(" + str(f) + ","
         elif i==num-1:
             mess = mess+ str(f) + ")"
         else:
             mess = mess + str(f) + ","

         
         
    mess = str(h)+mess
    return mess


@respond_to(r'^dice\s(\d+)\s+(\d+)$')
def diceroll(message,roll,sty):  
    message.reply(dice(int(roll),int(sty)))
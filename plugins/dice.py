import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to


def dice(num,m):
    mess = ""
    h = 0
    for i in range(num):
         f = random.randint(1,m)
         h = h + f
         if num == 1:
             mess = "(" + str(f) + ")"
         elif i == 0:
             mess = "(" + str(f) + ","
         elif i == num-1:
             mess = mess+ str(f) + ")"
         else:
             mess = mess + str(f) + ","

         
         
    mess = str(h)+mess
    return mess

def dice_u(num):
    messu = ""
    mess1 = ""
    mess2 = ""
    mess3 = ""
    mess4 = ""
    mess5 = ""
    mess6 = ""
    for i in range(num):
        f = random.randint(1,6)
        if f == 1:
            mess1 += "`1`"
        elif f == 2:
            mess2 += "`2`"
        elif f == 1:
            mess3 += "`3`"
        elif f == 1:
            mess4 += "`4`"
        elif f == 1:
            mess5 += "`5`"
        else f == 1:
            mess6 += "`6`"

    messu = [mess1,mess2,mess3,mess4,mess5,mess6]
    string = "\n".join(list)
    return string


@respond_to(r'^dice\s(\d+)\s+(\d+)$')
def diceroll(message,roll,sty):  
    message.reply(dice(int(roll),int(sty)))

@respond_to(r'^dice\s(\d+)$')
def diceroll_once(message,roll):
    message.reply(dice(1,int(roll)))

@respond_to(r'^dice$')
def diceroll_unselected(message):
    message.reply(dice(1,100))

@respond_to(r'^dice\s(u)\s(\d+)$')
def diceroll_utakaze(message,roll):
    message.reply(dice_u(int(roll))

@respond_to(r'^dice\s(help)$')
def dice_help:
    message.reply('helpメッセージ')


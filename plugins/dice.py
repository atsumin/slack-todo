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

         
         
    mess = str(num) + "d" + str(m) + "=" + str(h) + mess
    return mess

def dice_u(num):
    messu = ""
    mess1 = 0
    mess2 = 0
    mess3 = 0
    mess4 = 0
    mess5 = 0
    mess6 = 0
    for i in range(num):
        f = random.randint(1,6)
        if f == 1:
            mess1 += 1
        elif f == 2:
            mess2 += 1
        elif f == 3:
            mess3 += 1
        elif f == 4:
            mess4 += 1
        elif f == 5:
            mess5 += 1
        else:
            mess6 += 1


    messu = str(num) + "d6=" + \
    " " + "`1`" + str(mess1)+ \
    " " + "`2`" + str(mess2)+ \
    " " + "`3`" + str(mess3)+ \
    " " + "`4`" + str(mess4)+ \
    " " + "`5`" + str(mess5)+ \
    " " + "`6`" + str(mess6)

    listu = messu.split()
    string = "\n".join(listu)
    return string


@respond_to(r'^dice\s(\d+)(d)(\d+)$')
def diceroll(message,roll,d,sty):  
    message.reply(dice(int(roll),int(sty)))

@respond_to(r'^dice\s(d)(\d+)$')
def diceroll_once(message,d,roll):
    message.reply(dice(1,int(roll)))

@respond_to(r'^dice$')
def diceroll_unselected(message):
    message.reply(dice(1,100))

@respond_to(r'^dice\s(u)\s(\d+)$')
def diceroll_utakaze(message,comm,roll):
    message.reply(dice_u(int(roll)))

@respond_to(r'^dice\s(help)')
def dice_help(message,comm):
    msg = "\n〇Dice機能について使用可能なコマンド\n"\
     "`dice (ダイスを振る回数)d(ダイスの面数)`\n"\
     "これが正規の表現です。指定したとおりにダイスを振ります。この表現を省略した形が以下にあります\n"\
     "`dice d(ダイスの面数)`\n"\
     "ダイスを振る回数を省略すると、指定した面数のダイスを1回振ります\n"\
     "`dice`\n"\
     "単にdiceと入力すると100面ダイスを1回振ります\n"\
     "`dice u (ダイスを振る回数)`\n"\
     "指定されただけ6面ダイスを振り、その内訳をダイス目ごとに表示します。ウタカゼTRPGにどうぞ\n"\
    message.reply(msg)

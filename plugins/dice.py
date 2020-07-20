import random

h=0
message = ""
def dice(num,men)
    for i in range(num):
        f = random.randint(1,men)
        if i==0:
             message = "(" + str(f) + ","
        elif i==num:
             message = message + str(f) + ")"
        else:
             message = message + str(f) + ","
     h = h + f

   message = str(h) + message
   return message


@respond_to(r'dice\s+(\d+)\s+d\s+(\d+)')
def diceroll(decl,roll,cedec,sty)
    if isinstance(roll,int)==false:
        message.reply('第一引数が不正です')
    elif isinstance(sty,int)==false:
        message.reply('第二引数が不正です')
    else:
        message.reply(dice(roll,sty))
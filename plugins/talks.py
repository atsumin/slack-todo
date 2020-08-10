from slackbot.bot import listen_to
import random

@listen_to('おはよう')
def listen_goodmorning(message):
    message.reply('おはようにゃ')

@listen_to('こんにちは')
def listen_hello(message):
    message.reply('こんにちにゃ')

@listen_to('こんばんは')
def listen_goodevening(message):
    message.reply('こんばんにゃ')

@listen_to('おやすみ')
def listen_goodnight(message):
    message.reply('おやすみなさいにゃ')

@listen_to('疲れた')
def listen_tired(message):
    message.reply('お疲れ、よく頑張ったにゃ！')

@listen_to('じゃんけん')
def listen_janken(message):
    messagelist=["グー","チョキ","パー"]
    num=random.randint(0,2)
    message.reply(messagelist[num])

@listen_to('あいこ')
def listen_aiko(message):
    messagelist=["グー","チョキ","パー"]
    num=random.randint(0,2)
    message.reply(messagelist[num])

@listen_to('勉強')
def listen_study(message):
    messagelist=["線形","微積","有機化学","物理化学","ILAS","中国語","英語"]
    num=random.randint(0,6)
    message.reply(messagelist[num])

@listen_to('暇')
def listen_freetime(message):
    messagelist=["youtubeみやぁ","寝やぁ","お菓子食べやぁ","本読みやぁ","携帯いじりやぁ","飲み物飲みやぁ"]
    num=random.randint(0,5)
    message.reply(messagelist[num])

@listen_to('休憩')
def listen_rest(message):
    messagelist=["5分","10分","30分"]
    num=random.randint(0,2)
    message.reply(messagelist[num])

@listen_to('ご飯')
def listen_meal(message):
    messagelist=["オムライス","カレー","麻婆豆腐","うどん","ラーメン","ハンバーグ","天ぷら"]
    num=random.randint(0,6)
    message.reply(messagelist[num])

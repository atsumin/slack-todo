<<<<<<< HEAD
import config_Hangman
import random
from slackbot.bot import respond_to

words=['slack','python','root','clock','environment','pencil','hangman','twitter','vacation','vaccine','quality','excellent',
       'justice','ax','boy','github','panda','kangaroo','bamboo','pentagon','freedom','communication','quater','weekend',
       'fake','champion','queen','elephant','typhoon','children','cherry','chapsticks','carbondioxide','kingdom','prestige',
       'fireworks','doctor','chemistry','mouse','genius','chocolate','ambitious','history','dinasour','vanilla',
       'mathematics','newton','halloween','physics','rhythm','gorilla','taxi','xylophone','tower','balloon']
def random_word():
    global guess
    global answer
    answer=words[random.randint(0,len(words)-1)]
    config_Hangman.hoge=config_Hangman.hoge*(len(answer))
    cofig_Hangman.fuga=answer
    message.reply(config_Hangman.hoge)
    message.reply("What's your guess?")



                
=======
words=list=["ax","boy","github","fake","champion","queen","elephant","typhoon","children","cherry","fireworks","doctor","chemistry",
            "mouse","genius","chocolate","mathematics","newton","halloween","physics","rhythm"]
            
>>>>>>> origin/omatsu

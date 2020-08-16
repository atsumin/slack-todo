from slackbot.bot import respond_to
import random_number
import check_number
import config_Numer0n

#乱数生成＆入力

#桁数ランダム

@respond_to(r'Num\s+random$')
def random(message):
    random_number.generate_number_random()


#桁数指定
    
@respond_to(r'Num\s+choose\s+(\d+)$')
def choose(message,digistr):
    random_number.generate_number_choose(digistr)





#判定プログラム
    
@respond_to(r'^Num\s+(\d+)$')
def check(message,digistr):   
    guess=digistr
    check_number.check_and_count(guess,random_number.answer)


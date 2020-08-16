from slackbot.bot import respond_to
import random_word
import check_word
import config_Hangman

@respond_to('Hangman')
def Hangman(message):
    message.reply("Let's play Hangman!")

#答えをリストからランダムに選ぶ

    random_word.random_word()







#判定プログラム

@respond_to(r'Hangman\s+check\s+(\S+)$' )
def check_word(message,guess):
    check_word.check_word(config_Hangman.fuga,guess)



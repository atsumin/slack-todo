<<<<<<< HEAD
from slackbot.bot import respond_to
import config_Hangman

def check_word(answer,guess):
    config_Hangman.count_try_word=config_Hangman.count_try_word+1
    if len(guess)==1:
        if guess in answer:            
            for i in range(len(answer)):                
                if answer[i]==guess:                    
                    config_Hangman.hoge=config_Hangman.hoge[0:i]+guess+config_Hangman.hoge[i+1:len(config_Hangman.hoge)]
    else:
           if guess==answer:
                config_Hangman.hoge=answer



    if config_Hangman.hoge!=answer:
        message.reply(config_Hangman.hoge)
        message.reply("Try again!")
        
    else:
        message.reply(answer)
        message.reply("Right! You took "+str(config_Hangman.count_try_word)+" times.")
=======
check the word 
>>>>>>> origin/omatsu

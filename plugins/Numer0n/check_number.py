from slackbot.bot import respond_to
import config_Numer0n

def check(guess,answer):
    global bite_counter,eat_counter
    bite_counter=0
    eat_counter=0
    for i in range(0,len(guess)):
        for j in range(0,len(guess)):
            if guess[i]==answer[j]:
                if i ==j:
                    eat_counter=eat_counter+1
                else:
                    bite_counter=bite_counter+1

    message.reply(str(eat_counter)+" eat&"+str(bite_counter)+" bite")

def check_and_count(guess,answer):
    config_Numer0n.count_try=config_Numer0n.count_try+1
    check(guess,answer)
    if eat_counter==len(answer):     
        if config_Numer0n.count_try!=1:
            message.reply("Right. The answer is "+answer+". You took "+str(config_Numer0n.count_try)+" times.")

        else:
            message.reply("Unbelievable! The answer is "+answer+". You took only once!")
    else:
        message.reply("Try Again!")




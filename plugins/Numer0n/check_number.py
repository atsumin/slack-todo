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

    print(str(eat_counter)+" eat&"+str(bite_counter)+" bite") 


def check_and_count(guess,answer):
    count_try=1
    check(guess,answer)
    while eat_counter!=len(answer):
            guess=input("Try agaein!")
            check(guess,answer)
            count_try=count_try+1
    if count_try!=1:
        print("Right. The answer is "+answer+". You took "+str(count_try)+" times.")

    else:
        print("Unbelievable! The answer is "+answer+". You took only once!")




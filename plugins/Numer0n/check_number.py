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


def check_and_count():
    count_try=1
    hoge=input("正解")
    fuga=input("推察")
    check(fuga,hoge)
    while eat_counter!=len(hoge):
            fuga=input("Try agaein!")
            check(fuga,hoge)
            count_try=count_try+1
    if count_try!=1:
        print("Right. The answer is "+hoge+". You took "+str(count_try)+" times.")

    else:
        print("Unbelievable! The answer is "+hoge+". You took only once!")




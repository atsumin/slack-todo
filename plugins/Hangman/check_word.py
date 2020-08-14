def check_word(answer):
    hoge="*"*(len(answer))
    print(hoge)
    counter=0
    while hoge != answer:
        guess=input("guess alphabet or answer! ")
        if len(guess)==1:
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i]==guess:
                        hoge=hoge[0:i]+guess+hoge[i+1:len(hoge)]
        else:
            if guess==answer:
                hoge=answer                
        print(hoge)
        counter=counter+1
    print("Right! You took "+str(counter)+" times")

from slackbot.bot import respond_to
import random

def generate_number_choose(N):
    global answer
    
    N=int(N)
    A=""
    for i in range(N):
        B=random.randint(0,9)
        B=str(B)
        while B in A:
            B=random.randint(0,9)
            B=str(B)
        A=A+B
    answer=A
    message.reply("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    

def generate_number_random():
    global answer
    

    N=random.randint(1,10)
    A=""
    for i in range(N):
        B=random.randint(0,9)
        B=str(B)
        while B in A:
            B=random.randint(0,9)
            B=str(B)
        A=A+B
    answer=A
    message.reply("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    
    



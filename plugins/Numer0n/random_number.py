<<<<<<< HEAD
from slackbot.bot import respond_to
import random

def generate_number_choose(N):
    global answer
    
    N=int(N)
    A=""
    for i in range(N):
=======
import random
def generate_number_choose():
    n=input("桁数を選択")
    n=int(n)
    while n >=11:
        n=input("1から10の半角数字で入力してください")
        n=int(n)
    A=""
    for i in range(n):
>>>>>>> origin/omatsu
        B=random.randint(0,9)
        B=str(B)
        while B in A:
            B=random.randint(0,9)
            B=str(B)
        A=A+B
    answer=A
<<<<<<< HEAD
    message.reply("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    

def generate_number_random():
    global answer
    

    N=random.randint(1,10)
    A=""
    for i in range(N):
=======
    print("数字の重複がない"+str(n)+"ケタの数が生成されました。答えは何でしょう？")

def generate_number_random():
    n=random.randint(1,10)
    A=""
    for i in range(n):
>>>>>>> origin/omatsu
        B=random.randint(0,9)
        B=str(B)
        while B in A:
            B=random.randint(0,9)
            B=str(B)
        A=A+B
    answer=A
<<<<<<< HEAD
    message.reply("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    
    


=======
    print("数字の重複がない"+str(n)+"ケタの数が生成されました。答えは何でしょう？")

generate_number_random()
>>>>>>> origin/omatsu

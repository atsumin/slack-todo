import random
def generate_number_choose():
    global answer
    global guess
    
    N=input("桁数を選択")
    N=int(N)
    while N >=11:
        N=input("1から10の半角数字で入力してください")
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
    guess=input("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    

def generate_number_random():
    global answer
    global guess

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
    guess=input("数字の重複がない"+str(N)+"ケタの数が生成されました。答えは何でしょう？")
    
    



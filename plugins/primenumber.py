import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from time import time
import sys
sys.path.append('../../')
import run

quizwaiting = False
quizanswer = False
quiznum = -1
quizcorr = 0
quizlev = 0
#素数表作成
def Eratosthenes(k):
    pn = 0
    primelist = list(range(int(k)))
    del primelist[0]
    del primelist[0]
    p = 2
    while p*p <= k:
     for i in range(2,-(-k//p)):
        if not primelist.count(int(i*p)) == 0:
            tag = primelist.index(int(i*p))
            del primelist[tag]
     pn = pn + 1
     p = primelist[pn]
    
    return primelist

#クイズ機能
def primequizgenerate(lev):
    global quizanswer
    rad = 10
    while (rad % 2 == 0)or(rad % 5 == 0): 
     if lev == 1:
        rad = random.randint(10,99)
     elif lev == 2:
        rad = random.randint(100,999)
     elif lev == 3:
        rad = random.randint(1000,9999)
    msg = str(rad)
    quizanswer = primesearch(rad)
    return msg

#走査機能
def primesearch(i):
    prilist = run.primelist
    if not prilist.count(i) == 0:
        judge = True
    else:
        judge = False

    return judge

#素因数分解機能
def prime_factorization(num):
    prilist = run.primelist
    if not prilist.count(int(num)) == 0:
        mess = 'この数は素数です'
    else:
        i = int(num)
        mess = ""
        for k in range(len(prilist)):
            if (i % int(prilist[k])) == 0:
                tempmes = str(prilist[k])
                i = int(i/prilist[k])
                if  (i%int(prilist[k])) == 0:
                    tempmes += '^'
                    powercount = 2
                    i = int(i/prilist[k])
                    while (i%int(prilist[k])) == 0:
                        i = int(i/prilist[k])
                        powercount += 1

                    tempmes += str(powercount)

                mess += tempmes+'×'

        mess = mess[:-1]
    return mess


#help機能
@respond_to(r'^prime\s(help)$')
def prime_help(message,comm):
    msg = '\n〇Prime機能について使用可能なコマンド\n'\
    '`prime (4桁までの自然数)`\n'\
    '入力した自然数が素数かどうか判定します\n'\
    '`prime list`\n'\
    '4桁までの素数を全て表示します\n'\
    '`prime era (自然数)`\n'\
    '入力された自然数以下の素数を実際に素数表作成アルゴリズムを用いて求め表示します\n'\
    'どれくらいの大きさの数を入れるとどれほど時間がかかるのか実際に体験してみましょう\n'\
    '`prime quiz [1-3]`\n'\
    'クイズ機能です。自然数が表示されるので、それが素数がどうか判定してください。\n'\
    '[1-3]でレベルを選択できます。\n'\
    'レベル１：2桁の自然数\n'\
    'レベル２：3桁の自然数\n'\
    'レベル３：4桁の自然数\n'\
    '\n〇素数表作成に使用しているアルゴリズム\n'\
    'Prime機能で使用している素数表作成アルゴリズムは「エラトステネスのふるい」と呼ばれるものです\n'\
    '以下がその手順です\n'\
    '```1:ある自然数N(ここでは9999)を用意する\n'\
    '2:2からNまでの自然数を並べてリストにする\n'\
    '3:p = 2 とする\n'\
    '4:p自身を除くpの倍数をリストから削除する\n'\
    '5:リストに残っている自然数のなかで最小のものを新たなpとする\n'\
    '6:p^2がnを超えるまで手順4,5を繰り返す```\n'\
    'このアルゴリズムによって以下の素数全てを発見することができます。演算時間はO(nloglogn)であることが知られています\n'\
    '\n〇「エラトステネスのふるい」の数学的妥当性\n'\
    'この手順で行っていることはその場その場で最小の素数の倍数（ここでいう倍数はその数自身を除くものとする）を消去していることにすぎません\n'\
    '素数の倍数を順番に消去しているのですから、リストに素数だけが残るのは当然のことです\n'\
    'ではどうしてリスト全ての自然数について調べるのではなく、p^2がnを超えた時点で操作を終了するのでしょうか\n'\
    '少し考えてみましょう。いまpとして素数mが指定され、今からmの倍数を除くとします\n'\
    'このときmの平方数、すなわちm^2より小さいmの倍数はmとmより小さい素数の積です\n'\
    'mより小さい素数の倍数は既に前の操作で取り除いていますから、すでにリストに残っているmの倍数はm^2より大きいはずです\n'\
    'ここでm^2 > n だとすると、このリストにmの倍数は存在しないことになります\n'\
    'mより大きな素数についても以上のことが成り立ちます\n'\
    'よってp^2 > n が成り立つとき、リストには除くべき自然数が存在しません。つまりN以下の素数の表が完成しているということです\n'\
    '\n〇最後に\n'\
    'このツールは素数で遊びたい理系諸君、理系の卵たちのために作成しました\n'\
    'これで少しでも整数論や素数に興味を持ってくれると幸いです\n'
    message.reply(msg)



@respond_to(r'^prime\s(list)$')
def prime_list(message,comm):
    global quizwaiting
    if not quizwaiting == False:
        prilist = run.primelist
        mess = ','.join(map(str,prilist))
        message.reply(mess)
    else:
        message.reply('ずるはよくないなあ')
    
@respond_to(r'^prime\s(\d+)$')
def prime_judge(message,num):
    global quizwaiting
    if not 1 <= int(num) <= 9999:
        message.reply('4桁までの自然数を入力してください!')
    elif quizwaiting == True:
        message.reply('ずるは良くないなあ')
    else:
        if primesearch(int(num)) == True:
            msg = str(num) + 'は素数です!'
        else:
            msg = str(num) + 'は素数ではありません!'
            msg += '\n' + str(num) + 'は次のように素因数分解できます!\n'
            msg += str(num) + '=' + prime_factorization(int(num))
        message.reply(msg)

@respond_to(r'^prime\s(era\s)(\d+)$')
def prime_erastho(message,comm,num):
    if int(num) < 0:
        message.reply('正の自然数を入力してください')
    elif int(num) > 30000:
        message.reply('数が大きすぎるよ!')
    else:
        message.reply('Please Wait...')
        starttime = time()
        mess = ','.join(map(str,Eratosthenes(int(num)+1)))
        proctime = time() - starttime
        mess = '\n'+str(int(num))+'以下の素数を表示します\n'+mess
        mess += '\n\n' + '計算時間:' + str(proctime) + 'sec'
        message.reply(mess)

@respond_to(r'^prime\s(quiz\s)(\d+)$')
def prime_quiz_selectedlevel(message,comm,lev):
    global quizwaiting
    global quiznum
    global quizlev
    global quizcorr
    if not 1 <= int(lev) <= 3:
        msg = 'レベルは1から3までだよ!'
    else:
     quizwaiting = True
     quizlev = int(lev)
     if quiznum == -1:
        quiznum = 3
        quizcorr = 0
        msg = '\nレベル'+lev+'の問題だよ! 全部で3問\n'\
        +'まずは第一問\n'
        msg += primequizgenerate(int(lev))
        msg += 'は素数?素数じゃない?\n'\
        '素数ならY,素数じゃないならNと答えてね'
     elif quiznum == 2:
        msg = '\n続いて第二問\n'
        msg += primequizgenerate(int(lev))
        msg += 'は素数?素数じゃない?\n'\
        '素数ならY,素数じゃないならNと答えてね'
     elif quiznum == 1:
        msg = '\n最後に第三問\n'
        msg += primequizgenerate(int(lev))
        msg += 'は素数?素数じゃない?\n'\
        '素数ならY,素数じゃないならNと答えてね'
     elif quiznum == 0:
        quizwaiting = False
        quiznum = -1
        msg = '\n結果：3問中' + str(quizcorr) + '問正解\n'
        if quizcorr == 0:
            msg += 'ありゃありゃ...次は頑張ってみよう!'
        elif quizcorr == 1:
            msg += 'まずは1問正解! 次はもっと正解してみよう!'
        elif quizcorr == 2:
            msg += 'いい結果だ! 次は全問正解を目指してみよう!'
        elif quizcorr == 3:
            if not quizlev == 3:
             msg += 'すごい！全問正解だ!\n'\
             +'ぜひレベル'+str(int(quizlev)+1)+'に挑戦してみてね!'
            else:
             msg += 'レベル３で全問正解!　ワンダフル!\n'\
             '素数クイズパーフェクトクリアだ! おめでとう!'
    message.reply(msg)

@respond_to(r'^prime\s(quiz)$')
def prime_quiz_unselectedlevel(message,comm):
  prime_quiz_selectedlevel(message,'comm',1)

@respond_to(r'^Y$')
def prime_quiz_answerasy(message):
    global quizanswer
    global quizwaiting
    global quizcorr
    global quizlev
    global quiznum
    if (quizwaiting == True)and(quizanswer == True):
        quizwaiting = False
        quiznum -= 1
        msg = '正解!'
        quizcorr += 1
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    elif (quizwaiting == True)and(quizanswer == False):
        quizwaiting = False
        quiznum -= 1
        msg = '残念!'
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    else:
        msg ='クイズはまだ出題されていないよ!'
        message.reply(msg)
    

@listen_to(r'^Y$')
def prime_quiz_answerasy_listened(message):
    global quizanswer
    global quizwaiting
    global quizcorr
    global quizlev
    global quiznum
    if (quizwaiting == True)and(quizanswer == True):
        quizwaiting = False
        quiznum -= 1
        msg = '正解!'
        quizcorr += 1
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    elif (quizwaiting == True)and(quizanswer == False):
        quizwaiting = False
        quiznum -= 1
        msg = '残念!'
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    else:
        msg ='クイズはまだ出題されていないよ!'
        message.reply(msg)

@respond_to(r'^N$')
def prime_quiz_answerasn(message):
    global quizanswer
    global quizwaiting
    global quizcorr
    global quizlev
    global quiznum
    if (quizwaiting == True)and(quizanswer == False):
        quizwaiting = False
        quiznum -= 1
        msg = '正解!'
        quizcorr += 1
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    elif (quizwaiting == True)and(quizanswer == True):
        quizwaiting = False
        quiznum -= 1
        msg = '残念!'
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    else:
        msg ='クイズはまだ出題されていないよ!'
        message.reply(msg)

@listen_to(r'^N$')
def prime_quiz_answerasn_listened(message):
    global quizanswer
    global quizwaiting
    global quizcorr
    global quizlev
    global quiznum
    if (quizwaiting == True)and(quizanswer == False):
        quizwaiting = False
        quiznum -= 1
        msg = '正解!'
        quizcorr += 1
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    elif (quizwaiting == True)and(quizanswer == True):
        quizwaiting = False
        quiznum -= 1
        msg = '残念!'
        message.reply(msg)
        prime_quiz_selectedlevel(message,'comm',str(quizlev))
    else:
        msg ='クイズはまだ出題されていないよ!'
        message.reply(msg)

#ある日の母との会話
#僕「素数判定機作ったよ」
#母「ふーん。私には必要ないね」
#僕「じゃあ10023は素数か。素数じゃないか」
#母「素数じゃない」
#僕「101は？」
#母「素数」
#僕「2019は？」
#母「素数じゃない」
#僕「なんで分かるん」
#母「勘」
#僕「勘か...」
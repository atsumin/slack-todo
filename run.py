from slacker import Slacker
from slackbot.bot import Bot
from tododb import DB
from plugins.notice import Notice
import os
import threading
import datetime
import time
import sys
# 高速起動のためにnumpy,numbaをここで読み込む
import numpy
import numba

# 素数表の作成
k = 10000
pn = 0
primelist = list(range(int(k)))
del primelist[0]
del primelist[0]
p = 2
while p*p <= k:
    for i in range(2, -(-k//p)):
        if not primelist.count(int(i*p)) == 0:
            tag = primelist.index(int(i*p))
            del primelist[tag]
    pn = pn + 1
    p = primelist[pn]


def noticeThread():
    time.sleep(10)
    while True:
        nt = Notice()
        del nt
        # デバックを容易にするため、待機は30秒のみ
        time.sleep(30)


def botThread():
    mybot = Bot()
    mybot.run()


def stop():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('プログラムを終了します...')
        sys.exit()


if __name__ == '__main__':
    slack = Slacker(os.environ['API_TOKEN'])
    channel = os.environ['SLACK_CHANNEL']
    slack.chat.post_message(
        channel, 'new version bot is deployed.', as_user=True)

    dbname = os.environ['TODO_DB']
    need_init = not os.path.exists(dbname)
    database = DB(dbname)
    if need_init:
        database.init()
    # 列追加、減少を自動反映
    database.clean()

    n_t = threading.Thread(target=noticeThread)
    b_t = threading.Thread(target=botThread)
    n_t.setDaemon(True)
    b_t.setDaemon(True)
    n_t.start()
    b_t.start()

    stop()

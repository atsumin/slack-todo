#explain How to play Numer0n

@respond_to(r'^Num\s(help)$')
def Num_help(message):
    msg = \
    "\n Numer0n の遊び方"\
    "ランダムに重複のない数列が生成されます。その答えを当ててください\n"\
    "解答するたびにヒントが与えられます。 \n"\
    "eat:数字と位置が一致しています\n"\
    "bite:数字のみ一致しています\n"\
    "Num choose　または Num random と入力すると開始します\n"\
    "Num choose: 桁数指定モード;生成される答えの桁数を指定できます\n"\
    "Num random:桁数ランダムモード;生成される答えの桁数はランダムに設定されます\n"\
    "解答は　Num {半角数字}　の形で答えてください\n"\
    message.reply(msg)

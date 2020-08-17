from slackbot.bot import respond_to

#explain command about How to play Hangman

@respond_to(r'^Hangman\s(help)$')
def Hangman_help(message):
    msg=\
    "\n Hangmanの遊び方"\
    "リストからランダムで出題される英単語を当てるゲームです\n"\
    "入力したアルファベットが答えの英単語に含まれていた場合、何文字目かを知ることができます。\n"\
    "英単語を入力した場合、完全一致のときのみ正解になります。 \n"\
    "Hangman start で開始（答えが設定されます）\n"\
    "Hangman check {半角アルファベットまたは英単語} で解答 \n"\
    message.reply(msg)

from .sub_yonmoku import game_yonmoku as g
from .sub_yonmoku import monta as AI1
from .sub_yonmoku import atnom as AI2
from slackbot.bot import respond_to

yonmokugame = None

@respond_to(r"^\s*yonmoku\s+help$")
def yonmoku_help(message):
    msg = "四目並べは、先手黒、後手赤として先に5*5の盤面で4つ以上まっすぐにつなげたほうが勝ちのゲームです。"
    msg += "縦、横、斜めどれでもカウントされます。\n"
    msg += "ゲームを開始するには、\n```@(bot名) yonmoku```\nと打って下さい。\n"
    msg += "もし、四目並べに自信がない方は、\n```@(bot名) yonmoku easy```\nと打ってください。\n"
    msg += "なお、この二人のcomは完全読み切りではないです。通常のComに勝つことは出来るのか、弱いComに負けることは出来るのか！？\n是非とも一度挑戦してみてください。\n"
    msg += "Hint: 勝ちたい場合は先手、負けたい場合は後手を選ぶと有利です。"
    message.reply(msg)


@respond_to(r"^\s*yonmoku$")
def start_game(message ,depth = 3):
    global yonmokugame
    if yonmokugame !=None:
        message.reply("現在のゲームを中断して新しいゲームを開始します")
    message.reply("ゲームの開始にはしばらく時間がかかることがあります")
    yonmokugame = g.game(AI1.AI(),depth)
    go_forward(message)

@respond_to(r"^\s*yonmoku\s*easy$")
def start_game_easy(message ,depth = 3):
    global yonmokugame
    if yonmokugame !=None:
        message.reply("現在のゲームを中断して新しいゲームを開始します")
    yonmokugame = g.game(AI2.AI(),depth)
    go_forward(message)
    

@respond_to(r"^\s*yonmoku\s*set\s*([ABCDEabcde12345]{2})\s*$")    
def go_forward(message, pos=None):   
    global yonmokugame

    if yonmokugame == None:
        message.reply("四目並べゲームは開始されていません。もし開始する場合は\n```@(bot名)yonmoku```\nと打ってみてください。")
        return 0
    else: 
        # pos(str)->pos(int)
        if pos == None:
            pos = 0
        else:
            plist = list(pos)
            for i in range(2):
                if plist[i] =="1":
                    plist[i] = "0"
                elif plist[i] =="2":
                    plist[i] = "5"
                elif plist[i] =="3":
                    plist[i] = "10"
                elif plist[i] =="4":
                    plist[i] = "15"
                elif plist[i] =="5":
                    plist[i] = "20"
                else:
                    plist[i] = plist[i].replace("A", "0")
                    plist[i] = plist[i].replace("a", "0")
                    plist[i] = plist[i].replace("B", "1")
                    plist[i] = plist[i].replace("b", "1")
                    plist[i] = plist[i].replace("C", "2")
                    plist[i] = plist[i].replace("c", "2")
                    plist[i] = plist[i].replace("D", "3")
                    plist[i] = plist[i].replace("d", "3")
                    plist[i] = plist[i].replace("E", "4")
                    plist[i] = plist[i].replace("e", "4")
            pos = int(plist[0])+int(plist[1])
        # 範囲外なら入力し直し
        if pos < 0 or pos > 24:
            message.reply("入力が不正です。以下を参考に入力してください。\n")
        # 既に置かれていたらやりなおし
        elif yonmokugame.board[pos] != 0:
            message.reply("既に駒が置かれているところを選択しています。選び直してください。")
            return 0
        else:
            message.reply("Comが考えています。これには時間がかかることがあります。")
            (result, board_list) = yonmokugame.run(pos)
            for board in board_list:
                message.reply(board)
            if result != 0:
                yonmokugame = None
                # 勝ち
                if result == 1:
                    message.reply("あなたの勝ちです。おめでとうございます！")
                    return 0
                # 負け    
                if result == -1:
                    message.reply("ああ、残念！あなたの負けです。")
                    return 0
                # 引き分け
                if result == 2:
                    message.reply("引き分けです。")
                    return 0
            else:
                mark={-1:":red_circle:", 0:":white_small_square:", 1:":black_circle:"}
                message.reply(f"あなたの駒は{mark[yonmokugame.playerfirst]}です。どこに打ちますか？\n")
        message.reply("指定例 \n`!set A1` `!set 3c`\n`@(bot名)yonmoku set a1` `@(bot名)yonmoku set 3C`")
        

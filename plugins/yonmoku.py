from .sub_yonmoku import game_yonmoku as g
from .sub_yonmoku import monta as AI1
from .sub_yonmoku import atnom as AI2
from slackbot.bot import respond_to
from slackbot.bot import listen_to

yonmokugame = None

@respond_to(r"^\s*yonmoku$")
def start_game(message ,depth = 3):
    global yonmokugame
    if yonmokugame !=None:
        message.reply("現在のゲームを中断して新しいゲームを開始します")
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
                message.reply("どこに打ちますか？\n")
        message.reply("指定例 \n`!set A1` `!set 3c`\n`@(bot名)yonmoku set a1` `@(bot名)yonmoku set 3C`")
        

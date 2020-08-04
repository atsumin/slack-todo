from .sub_yonmoku import game_yonmoku as g
from .sub_yonmoku import com
from slackbot.bot import respond_to
from slackbot.bot import listen_to

yonmokugame = None

@respond_to(r"^yonmoku$")
def start_game(message):
    global yonmokugame
    if yonmokugame !=None:
        message.reply("現在のゲームを中断して新しいゲームを開始します")
    yonmokugame = g.game()
    yonmokugame.com = com.computer()
    go_forward(message)
    

@respond_to(r"^\s*yonmoku\s+set\s+([ABCDEabcde12345]{2})")    
def go_forward(message, pos=-1):   
    global yonmokugame
    (result, board_list) = yonmokugame.run(pos)
    for board in board_list:
        message.reply(board)
    if result != 0:
        yonmokugame = None
        # 勝ち
        if result == 1:
            message.reply("あなたの勝ちです。おめでとうございます！")
        # 負け    
        if result == -1:
            message.reply("ああ、残念！あなたの負けです。")
        # 引き分け
        if result == 2:
            message.reply("引き分けです。")
    else:
        message.reply("どこに打ちますか？\n指定例 \n```!set A1```\n```!set 3c```")
        

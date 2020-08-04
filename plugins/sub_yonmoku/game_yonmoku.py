import random
from copy import copy

class game:
    def __init__(self):
        # 使用するcom
        self.com = None

        # player先手？
        self.playerfirst = random.randint(0,1)
        
        # 何手目？
        self.step = 0
        # 5*5の盤面
        self.board = [0]*25

        # ゲーム状況 
        # 0:進行中　1:勝ち　-1:負け　2:引き分け
        self.status = 0
        
        
    def run(self, player_pos=-1):
        # 盤面の変化を記録
        self.board_list = []
        # 開始直後だと変化が特殊なので場合分け
        if self.step == 0:
            self.board_list.append(self.board_to_str())
            if self.playerfirst != 1:
                self.turn_com()
                self.judge()
        else:
            # Playerの指定した手を打つ
            self.board[player_pos] = (-1)**self.step
            
            # 手数を追加
            self.step += 1
            self.board_list.append(self.board_to_str())
            self.judge()
            # 勝利判定に引っかからなかった場合に続行
            if not self.status == 0:
                self.turn_com()
                self.judge()
        return (self.status, self.board_list)
    
    def turn_com(self):
        self.com.board = copy(self.board)
        pos = self.com.set_pos()
        self.board[pos] = (-1)**self.step
        self.step += 1
        self.board_list.append(self.board_to_str())
                


    def board_to_str(self):
        mark={-1:":white_circle:", 0:":red_circle:", 1:":black_circle:"}
        str_board = ""
        str_board += "現在の盤面\n      `A`  `B`  `C`  `D`  `E`\n"
        for i in range(5):
            str_board += f"{i+1} "
            for j in range(5):
                str_board += f"{mark[self.board[5*i+j]]}"
            str_board+="\n"
        return str_board

    def judge(self):
        finished = False

        # 一応決着がついたかを戻り値でも返すことにする
        return finished
        

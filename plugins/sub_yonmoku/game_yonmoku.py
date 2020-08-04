import random
from copy import copy

class game:
    def __init__(self):
        # 使用するcom
        self.com = None

        # player先手？1/-1
        self.playerfirst = random.randint(0,1)*2-1
        
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
            self.step += 1
            self.board_list.append(self.board_to_str())
            if self.playerfirst != 1:
                self.turn_com()
                self.judge()
        else:
            # Playerの指定した手を打つ
            self.place(player_pos)
            
            # 手数を追加
            self.step += 1
            self.board_list.append(self.board_to_str())
            self.judge()
            # 勝利判定に引っかからなかった場合に続行
            if self.status == 0:
                self.turn_com()
                self.judge()
        return (self.status, self.board_list)
    
    def turn_com(self):
        self.com.board = copy(self.board)
        pos = self.com.set_pos()
        self.place(pos)
        self.step += 1
        self.board_list.append(self.board_to_str())
                
    def place(self,pos):
        self.board[pos] = (-1)**(self.step-1)

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
        # 縦、横、斜めについて４つ揃っているか判定
        places = [
            (5, [i for i in range(10)]),
            (1, [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]),
            (6, [0, 1, 5, 6]),
            (4, [3, 4, 8, 9]),
        ]
        for itv, place in places:
            for i in place:
                k = sum(self.board[i: i + 3 * itv + 1: itv])
                if k == 4:
                    self.status = 1*self.playerfirst
                    return True
                if k == -4:
                    self.status = -1*self.playerfirst
                    return True
            if self.step == 26:
                self.status = 2
                return True
        # 一応決着がついたかを戻り値でも返すことにする
        return False
        

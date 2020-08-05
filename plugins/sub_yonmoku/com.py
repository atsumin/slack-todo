import random


def judge(board):
    # 縦、横、斜めについて４つ揃っているか判定
    places = [
        (5, [i for i in range(10)]),
        (1, [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]),
        (6, [0, 1, 5, 6]),
        (4, [3, 4, 8, 9]),
    ]
    for itv, place in places:
        for i in place:
            k = sum(board[i: i + 3 * itv + 1: itv])
            if k == 4:
                return 1
            if k == -4:
                return -1
    return 0
    



class computer():
    def __init__(self, AI, playerfirst, depth):
        self.depth = depth
        self.playerfirst = playerfirst
        self.AI = AI

    def set_pos(self):
        return 0

    def max_search(self, board, space, d = 0):
        if d == 0:
            if self.playerfirst == 1:
                board = list(map(lambda i: i * -1, board))
        
        status = judge(board)
        if status != 0:
            return (-1, self.AI.evaluate(board, status, space))

        if d < self.depth:
            shuffled = list(range(25))
            random.shuffle(shuffled)
            best_pos = -1
            best_value = -1000
            for i in shuffled:
                if board[i] == 0:
                    board[i] = (-1)**d
                    min_value = self.min_search(board, space - 1, d = d + 1)[1]
                    board[i] = 0
                    if best_value <= min_value:
                        best_pos = i
                        best_value = min_value
        else:
            return (-1, self.AI.evaluate(board, 0, space))

        return (best_pos, best_value)
    
    def min_search(self, board, space, d = 0):
        status = judge(board)
        if status != 0:
            return (-1, self.AI.evaluate(board, status, space))

        if d < self.depth:
            shuffled = list(range(25))
            random.shuffle(shuffled)
            best_pos = -1
            best_value = 1000
            for i in shuffled:
                if board[i] == 0:
                    board[i] = (-1)**d
                    max_value = self.max_search(board, space - 1, d = d + 1)[1]
                    board[i] = 0
                    if best_value >= max_value:
                        best_pos = i
                        best_value = max_value
        else:
            return (-1, self.AI.evaluate(board, 0, space))

        return (best_pos, best_value)
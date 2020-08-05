import numpy as np
import random
from copy import copy


def safejudge(board):
    # 縦一列 board[0, 5, 10, 15]
    num = 0
    for i in range(10):
        if max(board[i:i+16:5]) <= 0:
            num += abs(sum(board[i:i+16:5]))
    # 横一列 board[0, 1, 2, 3]
    for i in [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]:
        if max(board[i:i+4]) <= 0:
            num += abs(sum(board[i:i+4]))

    # 斜め一列 board[0, 6, 12, 18]
    for i in [0, 1, 5, 6]:
        if max(board[i:i+19:6]) <= 0:
            num += abs(sum(board[i:i+19:6]))

    # 斜め一列 board[3, 7, 11, 15]
    for i in [3, 4, 8, 9]:
        if max(board[i:i+13:4]) <= 0:
            num += abs(sum(board[i:i+13:4]))

    return num


def judge(board):
    dict = {}
    # 縦一列 board[0, 5, 10, 15]
    for i in range(10):
        if sum(board[i:i+16:5]) == -3:
            dict[i+5*board[i:i+16:5].index(0)] = 1
    # 横一列 board[0, 1, 2, 3]
    for i in [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]:
        if sum(board[i:i+4]) == -3:
            dict[i+board[i:i+4].index(0)] = 1

    # 斜め一列 board[0, 6, 12, 18]
    for i in [0, 1, 5, 6]:
        if sum(board[i:i+19:6]) == -3:
            dict[i+6*board[i:i+19:6].index(0)] = 1

    # 斜め一列 board[3, 7, 11, 15]
    for i in [3, 4, 8, 9]:
        if sum(board[i:i+13:4]) == -3:
            dict[i+4*board[i:i+13:4].index(0)] = 1

    return dict


def evaluation(board, space):
    dlist = [{}, {}]
    value = 0
    # 先手目線の盤面の評価
    dlist[1] = judge(board)
    value += safejudge(board)
    # 盤面の正負反転
    for i in range(25):
        board[i] *= -1
    # 後手目線の盤面の評価
    dlist[0] = judge(board)
    value -= safejudge(board)

    union = {}
    for i in range(2):
        for key in dlist[i].keys():
            union[key] = 1
    # print(dlist[0])
    # print(dlist[1])
    if len(dlist[1]) == space:
        return 800
    if len(dlist[0]) == space:
        return -800
    if len(union) == space:
        if len(dlist[0]) > len(dlist[1])+1:
            value -= 40
        elif len(dlist[1]) > len(dlist[0])+1:
            value += 40

    value += 10*len(dlist[1])-11*len(dlist[0])

    return value


class AI():

    def evaluate(self, board, judge, space):
        if judge == 1:  # 自分の勝ち
            return -900 - space
        if judge == -1:  # 自分の負け
            return 900 + space
        point = 0
        point = evaluation(copy(board), space)
        return point
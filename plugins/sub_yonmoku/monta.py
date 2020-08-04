import random

import numpy as np
from numba import njit


@njit(cache=True)
def judge(bd, bd_abs):
    dicts = [
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
        np.zeros(25),
    ]
    # 縦一列　横一列　右下へ斜め　左下へ斜め
    places = [
        (5, [i for i in range(10)]),
        (1, [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]),
        (6, [0, 1, 5, 6]),
        (4, [3, 4, 8, 9]),
    ]
    for itv, place in places:
        for i in place:
            k = np.sum(bd[i: i + 3 * itv + 1: itv])
            if k == 0:
                continue
            line = k
            if k < 0:
                line = -k + 4
            if np.sum(bd_abs[i: i + 3 * itv + 1: itv]) == abs(k):
                for l in [i, i + itv, i + 2 * itv, i + 3 * itv]:
                    if bd[l] == 0:
                        # dicts[line].setdefault(l, 0)
                        dicts[line][l] += 1
                        # print(f"place:{l}    line:{line}")
    return dicts



def evaluation(bd, space):
    bd_abs = np.abs(bd)
    value = 0
    chance = judge(bd, bd_abs)
    if np.sum(chance[7] > 0) >= 1:
        return -800
    if np.sum(chance[3] > 0) >= 2:
        return 800

    sums = [np.sum(chance[i]) // (4 - (i % 4)) for i in range(8)]

    if sums[3] == 1:
        if sums[2] != 0:
            if max(chance[2]) >= 2:
                return 700

    if sums[6] >= 2:
        return -700
    if sums[6] == 1:
        for key in range(25):
            if chance[6][key] == 0:
                continue
            if chance[5][key] >= 2:
                value += -30
        value -= 5
    if sums[2] != 0:
        if sums[2] - max(chance[2]) >= 2:
            value += 30
        if max(chance[2]) >= 2:
            value += 30

    if sums[5] >= 1:
        if max(chance[5]) >= 4:
            value -= 20
    value += sums[1]
    value += sums[2]
    if sums[2] >= 2:
        if sums[2] >= 3:
            value += sums[2]
        value += sums[2]

    value += sums[3]
    value -= sums[5]
    # print(chance[0])
    # print(chance[1])
    # print(chance[2])
    # print(chance[3])
    # print(chance[4])
    # print(chance[5])
    # print(chance[6])
    # print(chance[7])
    if space == 21 or space == 23:
        value += bd[12] * 11
    if space == 20 or space == 22:
        value += bd[1] * 2
        value += bd[3] * 2
        value += bd[5] * 2
        value += bd[9] * 2
        value += bd[15] * 2
        value += bd[19] * 2
        value += bd[21] * 2
        value += bd[23] * 2
    return value


class AI():
    def evaluate(self, board, judge, space):
        if judge == 1:  # 自分の勝ち
            return 900 + space
        if judge == -1:  # 自分の負け
            return -900 - space
        point = 0
        board = np.array(board, dtype=np.int32)
        point = evaluation(board, space)
        return point


# EOF

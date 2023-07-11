# -*- coding: utf-8 -*-
"""
@Time ： 2023-07-11 20:14
@Auth ： XinpengLu
@File ：Prisoners' Dilemma.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import numpy as np


def find_nash_equilibrium(matrix1, matrix2):
    # 找到每个玩家的最佳响应策略(划线法)，这里argmin表示找囚禁时间短的策略
    row_best_responses = np.argmax(matrix1, axis=1)
    col_best_responses = np.argmax(matrix2, axis=0)

    nash_equilibria = []

    # 迭代索引和元素值
    for i, row_resp in enumerate(row_best_responses):
        # 遍历玩家1的最佳响应策略，检查对应的玩家2策略是否也是最佳响应
        if col_best_responses[row_resp] == i:
            nash_equilibria.append((i, row_resp))

    print("博弈的纳什均衡为:", nash_equilibria)
    # 改成任意维度的矩阵，输出最终的收益值
    if len(nash_equilibria) > 0:
        for eq in nash_equilibria:
            print("玩家1的策略:", eq[0])
            print("玩家2的策略:", eq[1])
            payoff = payoff_matrix1[eq[0]][eq[1]] + payoff_matrix2[eq[0]][eq[1]]
            print("博弈的收益为:", payoff)
    else:
        print("不存在纯策略纳什均衡!")


# 定义收益矩阵
payoff_matrix1 = np.array([[6, 0],
                           [12, 1]])
payoff_matrix2 = np.array([[6, 12],
                           [0, 1]])

# 求解纳什均衡
if __name__ == "__main__":
    find_nash_equilibrium(payoff_matrix1, payoff_matrix2)

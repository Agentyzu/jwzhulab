# -*- coding: utf-8 -*-
"""
@Time ： 2023-07-13 21:20
@Auth ： Huailing Ma
@File ：Subset_enumeration_algorithm.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import numpy as np
import nashpy as nash
import time

# 子集枚举算法
def Subset_enumeration_algorithm(payoff_matrix):
    equilibria = payoff_matrix.support_enumeration()

    # 遍历所有纳什均衡
    for eq in equilibria:
        player1, player2 = eq[0], eq[1]
        print("Player 1:", player1)
        print("Player 2:", player2)

    return

# 定义收益矩阵
payoff_matrix1 = np.array([[3, 1],
                           [0, 3],
                           [2, 1]])
payoff_matrix2 = np.array([[3, 5],
                           [4, 2],
                           [3, 3]])

payoff_matrix = nash.Game(payoff_matrix1,
                          payoff_matrix2)



if __name__ == "__main__":
    # 记录开始时间
    time_start = time.time()

    Subset_enumeration_algorithm(payoff_matrix)

    # 记录结束时间
    time_end = time.time()
    # 计算的时间差为程序的执行时间，单位为秒/s
    time_sum = time_end - time_start
    print("运行时间是: {:9.9}s".format(time_sum))
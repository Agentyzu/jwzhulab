# -*- coding: utf-8 -*-
"""
@Time ： 2023-07-13 21:20
@Auth ： Huailing Ma
@File ：Lemke-Howson.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import nashpy as nash
import numpy as np
import time

def LH(payoff_matrix1, payoff_matrix2):
    # 只寻找一条路径，找到nash就停止
    e = payoff_matrix.lemke_howson(initial_dropped_label=0)
    print("一条路径下的nash:")
    print(e)
    print()

    # 寻找不同路径下的纳什均衡（可能不同路径最终走到的均衡是一样的）
    equilibria = payoff_matrix.lemke_howson_enumeration()
    print("不同路径下的nash:")
    # 遍历所有纳什均衡
    for eq in equilibria:
        player1, player2 = eq[0], eq[1]
        print("Player 1:", player1)
        print("Player 2:", player2)
        print()


# 定义收益矩阵
payoff_matrix1 = np.array([[3, 1],
                           [0, 3],
                           [2, 1]])
payoff_matrix2 = np.array([[3, 5],
                           [4, 2],
                           [3, 3]])

payoff_matrix = nash.Game(payoff_matrix1,
                          payoff_matrix2)

# lemke-howson算法求解纳什均衡
if __name__ == "__main__":
    # 记录开始时间
    time_start = time.time()

    LH(payoff_matrix1, payoff_matrix2)

    # 记录结束时间
    time_end = time.time()
    # 计算的时间差为程序的执行时间，单位为秒/s
    time_sum = time_end - time_start
    print("运行时间是: {:9.9}s".format(time_sum))




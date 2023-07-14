# -*- coding: utf-8 -*-
"""
@Time ： 2023-07-13 21:20
@Auth ： Huailing Ma
@File ：Automatically_generated_Subset_enumeration_algorithm.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import random
import nashpy
import numpy as np
import time
import argparse


# Num1是玩家1的策略数，Num2是玩家2的策略数，根据Num1和Num2生成一个Num1 * Num2的支付矩阵样例
# Input输入支付矩阵
def GetPayMatrix(Num1, Num2: int) -> list:
    global payoff_matrix1
    global payoff_matrix2
    _A = []
    _B = []

    print("输入样例:")
    for i in range(Num1):
        for j in range(Num2 - 1):
            print(random.randrange(0, 5), ',', random.randrange(0, 5), end=' ; ')
        print(random.randrange(0, 5), ',', random.randrange(0, 5))

    print("请输入支付矩阵:")
    print(' ' * 13, end='')
    for i in range(1, Num2 + 1):
        print("Strategy%s ; " % i, end='')
    print('')

    for i in range(1, Num1 + 1):
        pay = input("Strategy%s : " % i).split(';')
        tmpA = []
        tmpB = []
        for j in range(Num2):
            a, b = map(str.strip, pay[j].split(","))
            tmpA.append(float(a))
            tmpB.append(float(b))
        _A.append(tmpA)
        _B.append(tmpB)

    payoff_matrix1 = np.array(_A)
    payoff_matrix2 = np.array(_B)
    payoff_matrix = nashpy.Game(payoff_matrix1, payoff_matrix2)

    return payoff_matrix

# 子集枚举算法
def Subset_enumeration_algorithm(payoff_matrix):

    equilibria = payoff_matrix.support_enumeration()

    # 遍历所有纳什均衡
    for eq in equilibria:
        player1, player2 = eq[0], eq[1]
        print("Player 1:", player1)
        print("Player 2:", player2)
        print()

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='玩家1和玩家2的策略数')
    parser.add_argument('--Num1', type=int, help='玩家1的策略数', default=3)
    parser.add_argument('--Num2', type=int, help='玩家2的策略数', default=2)
    args = parser.parse_args()

    Num1 = args.Num1
    Num2 = args.Num2

    payoff_matrix = GetPayMatrix(Num1, Num2)

    print("Player 1的收益矩阵:\n", payoff_matrix1)
    print("Player 2的收益矩阵:\n", payoff_matrix2)

    # 记录开始时间
    time_start = time.time()

    Subset_enumeration_algorithm(payoff_matrix)

    # 记录结束时间
    time_end = time.time()
    # 计算的时间差为程序的执行时间，单位为秒/s
    time_sum = time_end - time_start
    print("运行时间是: {:9.9}s".format(time_sum))



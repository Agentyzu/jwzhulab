# -*- coding: utf-8 -*-
"""
@Time ： 2023-07-11 20:14
@Auth ： XinpengLu
@File ：Game_Tree.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 逆向归纳法求解动态博弈


def backward_induction(node):
    if 'payoff' in node:
        # 如果节点是叶子节点，则返回该节点的收益
        return node['payoff']
    
    player = node['player']
    if player == 'A':
        # 如果当前轮到玩家A行动，则选择收益最大的子节点
        best_payoff = None
        for action, child_node in node.items():
            if action == 'player':
                continue
            # 递归
            payoff = backward_induction(child_node)
            # 找收益最大的策略
            if best_payoff is None or payoff[1] > best_payoff[1]:
                best_payoff = payoff
        return best_payoff
    
    else:
        # 如果当前轮到玩家B行动，则选择收益最大的子节点
        best_payoff = None
        for action, child_node in node.items():
            if action == 'player':
                continue
            # 递归
            payoff = backward_induction(child_node)
            # 找收益最大的策略
            if best_payoff is None or payoff[0] > best_payoff[0]:
                best_payoff = payoff
        return best_payoff

# 构建博弈树:可以修改lawsuit后的payoff的值,比如将(2,0)改为(-10,-10)


game_tree = {
    'player': 'B',
    'no_borrow': {'payoff': (2, 0)},
    'borrow': {
        'player': 'A',
        'split': {'payoff': (3, 3)},
        'no_split': {
            'player': 'B',
            'lawsuit': {'payoff': (2, 0)},
            'not_lawsuit': {'payoff': (0, 6)}
            }
    }
}

if __name__ == "__main__":
    # 逆向归纳法（改的更规范，包含main函数，把树展示出来）
    optimal_payoff = backward_induction(game_tree)
    print("子博弈完美纳什均衡为:", optimal_payoff)

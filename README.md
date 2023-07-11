# Prisoner's Dilemma 1.0

## Introduction

This code can solve a two-person medium pure strategy Nash equilibrium where the function find_nash_equilibrium defines the function to solve the equilibrium. A classic example is the **Prisoner's dilemma**.

The *input* is the payoff matrix of the two players, and the *output* is all the Nash equilibrium solutions of the two players, the total payoff and the strategy adopted by the two players at this equilibrium point.

## Test

```
INPUT:
payoff_matrix1 = np.array([[6, 0],
                           [12, 1]])
payoff_matrix2 = np.array([[6, 12],
                           [0, 1]])
```

```
OUTPUT:
博弈的纳什均衡为: [(0, 0)]
玩家1的策略: 0
玩家2的策略: 0
博弈的收益为: 12
```



# Game_Tree 1.0

## Introduction

This code can solve the sub-game perfect Nash equilibrium in dynamic games and solve the equilibrium solution by backward induction. 

The *input* is the **game tree** of the dynamic game (the extended representation of the game), which contains the strategy and profit value of each player; The *output* is the solution of the perfect Nash equilibrium of the sub-game of the dynamic game.



## Example

An investor *A* is short of ￥20,000  when investing in a project worth ￥60,000, while *B* has ￥20,000 of idle funds to invest at this time. *A* hopes that *B* will lend him ￥20,000, and **promises** to split the money with *B* after making money at the end of the year. Should B lend the money to *A*?



## Test

```
INPUT1:
game_tree = {
    'player': 'B',
    'no_borrow': {'payoff': (2, 0)},
    'borrow': {
        'player': 'A',
        'split': {'payoff': (3, 3)},
        'no_split': {
            'player': 'B',
            'lawsuit': {'payoff': (-10, -10)},
            'not_lawsuit': {'payoff': (0, 6)}
            }
    }
}
```

```
OUTPUT1:
子博弈完美纳什均衡为: (2, 0)
```

```
INPUT2:
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
```

```
OUTPUT2:
子博弈完美纳什均衡为: (3, 3)
```
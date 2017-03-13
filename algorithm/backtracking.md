回溯法是暴力搜寻法中的一种。

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。

回溯法 = 穷举  + 剪枝

**基本思想**

在包含问题的所有解的解空间树中，按照**深度优先搜索的策略**，从根结点出发深度探索解空间树。当探索到某一结点时，要先判断该结点是否包含问题的解，如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。（其实回溯法就是对隐式图的深度优先搜索算法）。

**解题一般步骤**

1).确定问题的解空间 ：针对所给问题，定义问题的解空间； 

 子集树问题：装载问题、符号三角形问题、0-1背包问题、最大团问题
排列树问题：批处理作业调度、n后问题、旅行售货员问题、圆排列问题、电路板排列问题
其他：图的m着色问题

2).确定易于搜索的解空间结构：

找出适当的剪枝函数，约束函数和限界函数。

3).以深度优先的方式搜索解空间，并且在搜索过程中用剪枝函数避免无效的搜索。

递归回溯

迭代回溯

4).利用限界函数避免移动到不可能产生解的子空间



回溯的问题有三种：

1. find a path to success 有没有解
2. find all paths to success 求所有解
   1. 求所有解的个数
   2. 求所有解的具体信息
3. find the best path to success



**经典案例**

应用回溯法有：

- 1）装载问题
- 2）批处理作业调度
- 3）符号三角形问题
- 4）n后问题


- 5）0-1背包问题
- 6）最大团问题
- 7）图的m着色问题
- 8）旅行售货员问题
- 9）圆排列问题
- 10）电路板排列问题
- 11）连续邮资问题



#### n皇后问题

n×n格的棋盘上放置彼此不受攻击的n个皇后。按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。n后问题等价于在n×n格的棋盘上放置n个皇后，**任何2个皇后不放在同一行或同一列或同一斜线上**。求不同的解的个数。

当n=4时的分析过程：

![](pic/n_queen.jpg)

```python
# 递归版本
def nQueens(n, x=0, *solution):
    if x == n:
        yield solution
    else:
        for y in range(n):
            if all(y != j and abs(x - i) != abs(y - j) for i, j in solution):
                yield from nQueens(n, x + 1, *solution, (x, y))


# 迭代版本
def nQueensIter(n):
    solution = []
    j = 0
    while solution or j < n:
        i = len(solution)
        while j < n and not all(y != j and abs(x - i) != abs(y - j) 
                for x, y in enumerate(solution)):
            j += 1

        if j < n:
            solution.append(j)
            if i == n - 1:
                yield tuple(enumerate(solution))
                j = solution.pop() + 1
            else:
                j = 0
        else:
            j = solution.pop() + 1

if __name__ == '__main__':
    def showSolution(solutions, n):
        for i, s in enumerate(solutions, 1):
            print("%s:\n" % i + "=" * 20)
            for x in range(n):
                for y in range(n):
                    print('Q ' if s[x][1] == y else '_ ', end='')
                print()
            print()

    N = 8
    showSolution(nQueens(N), N)
    showSolution(nQueensIter(N), N)
```


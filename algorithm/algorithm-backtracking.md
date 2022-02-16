## 回溯法

回溯法是暴力搜寻法中的一种。

回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。

回溯法 = 穷举  + 剪枝



**解题套路**：

```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```


回溯的问题有三种：

1. find a path to success 有没有解
2. find all paths to success 求所有解
	1. 求所有解的个数
	2. 求所有解的具体信息
3. find the best path to success

**经典案例**

应用回溯法有：

* 装载问题
* 批处理作业调度
* 符号三角形问题
* **n皇后问题**
* **数独问题**
* 0-1背包问题
* 最大团问题
* 图的m着色问题
* 旅行售货员问题
* 全排列问题
* 电路板排列问题
* 连续邮资问题



#### 全排列问题

```python

"""
实现全排列：
inputs：
	nums: numbers need to be ordered
	
"""

res = []

def permute(nums, path):
    print(path)
    if len(path) == len(nums):
        res.append(tuple(path))
        return
   
    for i, n in enumerate(nums):
        if n in path:
            continue
        path.append(n)
        permute(nums, path)
        path.pop()


permute([1,2,3], [])

print("res: ", res)

```


#### n皇后问题
n×n格的棋盘上放置彼此不受攻击的n个皇后。按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。n后问题等价于在n×n格的棋盘上放置n个皇后，**任何2个皇后不放在同一行或同一列或同一斜线上**。求不同的解的个数。



```python

class nQueens(object):
  def __init__(self, n):
    self.n = n
    self.grid = [[0 for _ in range(n)] for _ in range(n)]
    self.solutions = []

  def is_finish(self, grid):
    _sum = [sum(line) for line in grid]
    _sum = sum(_sum)
    return True if _sum == self.n else False
 	
  def is_valid(self, grid, row, col):
    
    for i in range(row):
      f1 = grid[i][col] == 1
      f2 = grid[i][col - (row-i)] == 1 if col - (row-i) >= 0 else False
      f3 = grid[i][col + (row-i)] == 1 if col + (row-i) < self.n else False
      if f1 or f2 or f3:
        return False
    else:
        return True
    
  def backtrack(self, grid, row):
    if self.is_finish(grid):
      _grid = [[c for c in row] for row in grid]
      self.solutions.append(_grid)
      return

    for i in range(row, self.n):
      for j in range(self.n):
        if self.is_valid(grid, i, j):
          # 做选择
          grid[i][j] = 1
          # 递归
          self.backtrack(grid, i+1)
          # 撤销选择
          grid[i][j] = 0
    
  def run(self):
    self.backtrack(self.grid, 0)
    for i, s in enumerate(self.solutions):
        print(f'{i}:')
        for l in s:
            print(l)
    

nQueens(8).run()
```



#### 数独问题



```python
class Sudoku(object):
  def __init__(self, board):
    self.board = board
    self.N = len(board)
    self.options = [[i, j] for i in range(self.N) for j in range(self.N) 
                    if self.board[i][j] == 0]
    self.solutions = []
    
  def is_valid(self, board, row, col, num):
    # check if there is a same number in the same row
    for i in range(self.N):
        if self.board[row][i] == num:
            return False
    # check if there is a same number in the same column
    for i in range(self.N):
        if self.board[i][col] == num:
            return False
    # check if there is a same number in the same small square
    base_row, base_col = row//3, col//3
    for m in range(self.N):
        i, j = m//3, m%3
        if self.board[3*base_row+i][3*base_col+j] == num:
            return False
    return True
    
    
  def backtrack(self, board, ind):
    if ind == len(self.options):
      _board = [[c for c in row] for row in board]
      self.solutions.append(_board)
      return 
    
    i, j = self.options[ind]
    for num in range(1, 10, 1):
      if self.is_valid(board, i, j, num):
        board[i][j] = num
        self.backtrack(board, ind+1)
        board[i][j] = 0



    # print(self.empty)
          
  def run(self):
    self.backtrack(self.board, 0)
    for i, s in enumerate(self.solutions):
        print(f'{i}:')
        for l in s:
            print(l)
            

b = \
[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
Sudoku(b).run()
```


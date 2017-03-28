**一、基本概念：**

     所谓贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的仅是在某种意义上的局部最优解。

     贪心算法没有固定的算法框架，算法设计的关键是贪心策略的选择。必须注意的是，贪心算法不是对所有问题都能得到整体最优解，选择的贪心策略必须具备无后效性，即某个状态以后的过程不会影响以前的状态，只与当前状态有关。

    所以对所采用的贪心策略一定要仔细分析其**是否满足无后效性**。

**二、贪心算法的基本思路：**

    1.建立数学模型来描述问题。

    2.把求解的问题分成若干个子问题。

    3.对每一子问题求解，得到子问题的局部最优解。

    4.把子问题的解局部最优解合成原来解问题的一个解。

**三、贪心算法适用的问题**

**贪心策略适用的前提是：局部最优策略能导致产生全局最优解。**

**实际上，贪心算法适用的情况很少。一般，对一个问题分析是否适用于贪心算法，可以先选择该问题下的几个实际数据进行分析，就可做出判断。**



**四、贪心算法的实现框架**

    从问题的某一初始解出发；

    while （能朝给定总目标前进一步）

    { 

          利用可行的决策，求出可行解的一个解元素；

    }

    由所有解元素组合成问题的一个可行解；

  

**五、贪心策略的选择**

     因为用贪心算法只能通过解局部最优解的策略来达到全局最优解，因此，一定要注意判断问题是否适合采用贪心算法策略，找到的解是否一定是问题的最优解。



**六、典型例题**

* 均分纸牌
* 导弹拦截
* 合并果子
* 独木桥
* 最小生成树



例一：

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Note:**
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

**Example 1:**

```
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

```

**Example 2:**

```
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
```

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content = 0
        ind = 0
        for i in range(len(g)):
            while ind < len(s):
                if g[i] <= s[ind]:
                    content += 1
                    ind += 1
                    break
                ind += 1
            else:
                break
        return content
```


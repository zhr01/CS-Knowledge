# sort()函数多属性排序

### 函数说明

sort函数是list类的一个方法，说明如下：

sort(...)
L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1

其中，包含三个参数cmp，key，reverse：cmp用于指定排序的大小比较算法；key用于制定排序的维度和优先级别；reverse说明是否是逆序排列（True表示从大到小）

### 实例

让元祖按照第一维度降序，第二维度升序降序：

```python
students.sort(key=lambda l:(l[0],l[1]),reverse=True)
```

让一组数据降序，一组升序排列：

```python
def mycmp(a,b):
    if a[0]>b[0]:
        return 1
    if a[0]<b[0]:
        return -1
    if a[1]<b[1]:
        return 1
    if a[1]>b[1]:
        return -1
    return 0
if __name__=="__main__":
    #students.sort(key=lambda l:(l[0],l[1]),reverse=True)
    students.sort(cmp=mycmp)
```



Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers `(h, k)`, where `h` is the height of the person and `k` is the number of people in front of this person who have a height greater than or equal to `h`. Write an algorithm to reconstruct the queue.

**Note:**
The number of people is less than 1,100.

**Example**

```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

tag: Greedy

```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def mycmp(a, b):
            if a[0] > b[0]:
                return 1
            if a[0] < b[0]:
                return -1
            if a[1] < b[1]:
                return 1
            if a[1] > b[1]:
                return -1
            return 0

        people.sort(cmp=mycmp)
        people.reverse()
        res = []
        for person in people:
            res.insert(person[1], person)
        return res

s = Solution()
print s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
```


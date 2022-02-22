### Queue - 队列

FIFO -- First In First Out

```python
class Queue:
    """模拟队列"""
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def enqueue(self, item):
        self.items.insert(0,item)
 
    def dequeue(self):
        return self.items.pop()
 
    def size(self):
        return len(self.items)
```



### Stack - 栈

栈是⼀种 LIFO(Last In First Out) 的数据结构，常⽤⽅法有添加元素，取栈顶元素，弹出栈顶元素，判断栈
是否为空。

Python实现：

```python
stack = []
len(stack) # size of stack

# more efficient stack
import collections
stack = collections.deque()
```

**Methods:**

- `len(stack) != 0` - 判断`stack`是否weikong
- `stack[-1]` - 取栈顶元素，不移除
- `pop()` - 移除栈顶元素并返回该元素
- `append(item)` - 向栈顶添加元素

### Heap - 堆

⼀般情况下，堆通常指的是⼆叉堆。

**二叉堆（Binary Heap）**：二叉堆是完全二元树或者是近似完全二元树，它分为两种：最大堆和最小堆。

**特点**

1. 以数组表⽰，但是以完全⼆叉树的⽅式理解。
2. 唯⼀能够同时最优地利⽤空间和时间的⽅法——最坏情况下也能保证使⽤ 2N log N 次⽐较和恒定的额
   外空间。
3. 如果根节点在数组中的位置是1，第n个位置的子节点分别在2n和 2n+1，父节点在n//2。



![](pic/binary_heap.jpg)

以⼤根堆为例，堆的常⽤操作如下。

1. 最⼤堆调整（Max_Heapify）：插入-上浮，删除-下沉

2. 创建最⼤堆（Build_Max_Heap）：把一个无序的完全二叉树调整为二叉堆，本质上就是让所有非叶子节点依次下沉

3. 堆排序（HeapSort）：移除位在第⼀个数据的根节点，并做最⼤堆调整的递归运算

   

```python
class MaxHeap:
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []
            
    def _sink(self, array, i):
        # move node down the tree
        left, right = 2 * i + 1, 2 * i + 2
        max_index = i
        if left < len(array) and array[left] > array[max_index]:
            max_index = left
        if right < len(array) and array[right] > array[max_index]:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)

    def _swim(self, array, i):
        # move node up the tree
        if i == 0:
            return
        father = (i - 1) / 2
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)

    def _max_heapify(self, array):
        # 从最后一个非叶子节点开始，让所有非叶子节点依次下沉
        for i in xrange(len(array) / 2, -1, -1):
            self._sink(array, i)
        return array
		
    # 二叉堆的节点插入，插入位置是完全二叉树的最后一个位置
    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)
		
    # 删除的是处于堆顶的节点
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sink(self.heap, 0)
        return item

```



### Map - 哈希表

dict（Map）是python的一个基本数据结构。

```python
# map 在 python 中是一个keyword
hash_map = {} # or dict()
hash_map['shaun'] = 98
hash_map['wei'] = 99
exist = 'wei' in hash_map  # check existence
point = hash_map['shaun']  # get value by key
point = hash_map.pop('shaun') # remove by key, return value
keys = hash_map.keys()  # return key list
# iterate dictionary(map)
for key, value in hash_map.items():
    # do something with k, v
    pass
```


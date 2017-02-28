## Binary Search

⼆分搜索是⼀种在有序数组中寻找⽬标值的经典⽅法，也就是说使⽤前提是『有序数组』。⾮常简单的题中『有序』特征⾮常明显，但更多时候可能需要我们⾃⼰去构造『有序数组』。

### 迭代法

```python
def binary_search(alist, des):
    low, high = 0, len(alist)-1
    while low <= high:
        middle = low + (high-low)>>1
        if des == alist[middle]:
            return middle
        elif des < alist[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

a = [1,3,5,8,14,19,24,28,30,34,37]
print(binary_search(a, 3))
```



### 递归法

```python
def binary_search(alist, low, high, des):
    if low <= high:
        middle = low + (high-low)>>1
        if des == alist[mid]:
            return mid
        elif des < alist[mid]:
            return binary_search(alist, low, mid-1, des)
        elif des > alist[mid]:
            return binary_search(alist, mid+1, high, des)
    else:
        return -1

a = [1,3,5,8,14,19,24,28,30,34,37]
print(binary_search(a, 0, len(a), 3))
```


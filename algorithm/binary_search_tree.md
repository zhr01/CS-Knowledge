# Binary search Tree(BST)

一颗**二叉查找树(BST)**是一颗二叉树，其中每个节点都含有一个可进行比较的键及相应的值，且每个节点的键都**大于等于左子树中的任意节点的键**，而**小于右子树中的任意节点的键**。
$$
root.left.val \leq root.val < root.right.val
$$
**使用中序遍历可得到有序数组**，这是二叉查找树的又一个重要特征。

### 插入

```python
# 递归
def insert_node(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insert_node(root.left, node)
    else:
        root.right = insert_node(root.right, node)
    
    return root

# 迭代
def insert_node(root, node):
    if not root:
        return node
    init = root
    while root:
        if root.val >= node.val:
            if root.left:
                root = root.left
            else:
                root.left = node
                break
        else:
            if root.right:
                root = root.right
            else:
                root.right = node
                break
    return init
```






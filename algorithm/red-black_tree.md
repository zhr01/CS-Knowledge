# 动态查找树——红黑树

红黑树，一种二叉查找树，但在每个结点上增加一个存储位表示结点的颜色，可以是Red或Black。作为一棵二叉查找树，满足二叉查找树的一般性质。通过对任何一条从根到叶子的路径上各个结点着色方式的限制，红黑树确保没有一条路径会比其他路径长出俩倍，因而是接近平衡的。

**红黑树的5个性质：**

1. 每个结点要么是红的要么是黑的。  
2. 根结点是黑的。  
3. 每个叶结点（叶结点即指树尾端NIL指针或NULL结点）都是黑的。  
4. 如果一个结点是红的，那么它的两个儿子都是黑的。  
5.  对于任意结点而言，其到叶结点树尾端NIL指针的每条路径都包含相同数目的黑结点。 

![](pic/red-black.png)

"叶结点" 或"NULL结点"，如上图所示，它不包含数据而只充当树在此结束的指示，这些节点在绘图中经常被省略。

### 红黑树的插入与插入修复

红黑树的插入相当于在二叉查找树插入的基础上，为了重新恢复平衡，继续做了插入修复操作。

```python
RB-INSERT(T, z)  
y ← nil  
x ← T.root  
while x ≠ T.nil  
    do y ← x  
    if z.key < x.key  
        then x ← x.left  
    else x ← x.right  
z.p ← y  
if y == nil[T]  
    then T.root ← z  
else if z.key < y.key  
    then y.left ← z  
else y.right ← z  
z.left ← T.nil  
z.right ← T.nil  
z.color ← RED  
RB-INSERT-FIXUP(T, z)  	
```

但当遇到下述3种情况时又该如何调整呢？

● 插入修复情况1：如果当前结点的父结点是红色且祖父结点的另一个子结点（叔叔结点）是红色

● 插入修复情况2：当前节点的父节点是红色,叔叔节点是黑色，当前节点是其父节点的右子

● 插入修复情况3：当前节点的父节点是红色,叔叔节点是黑色，当前节点是其父节点的左子

```python
RB-INSERT-FIXUP(T, z)  
while z.p.color == RED  
    do if z.p == z.p.p.left  
        then y ← z.p.p.right  
        if y.color == RED  
            then z.p.color ← BLACK               ▹ Case 1  
            y.color ← BLACK                    ▹ Case 1  
            z.p.p.color ← RED                    ▹ Case 1  
            z ← z.p.p                            ▹ Case 1  
        else if z == z.p.right  
            then z ← z.p                          ▹ Case 2  
            LEFT-ROTATE(T, z)                   ▹ Case 2  
        z.p.color ← BLACK                        ▹ Case 3  
        z.p.p.color ← RED                         ▹ Case 3  
        RIGHT-ROTATE(T, z.p.p)                  ▹ Case 3  
    else (same as then clause with "right" and "left" exchanged)  
T.root.color ← BLACK  
```

### 红黑树的删除









### Python实现

```python
# coding=utf-8
# 红黑树Python实现

# 颜色常量
RED = 0
BLACK = 1


def left_rotate(tree, node):
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    if not node.p:
        tree.root = node_right
    elif node == node.p.left:
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:
        tree.root = node_left
    elif node == node.p.left:
        node.p.left = node_left
    elif node == node.p.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node


def transplant(tree, node_u, node_v):
    """
    用 v 替换 u
    :param tree: 树的根节点
    :param node_u: 将被替换的节点
    :param node_v: 替换后的节点
    :return: None
    """
    if not node_u.p:
        tree.root = node_v
    elif node_u == node_u.p.left:
        node_u.p.left = node_v
    elif node_u == node_u.p.right:
        node_u.p.right = node_v
    # 加一下为空的判断
    if node_v:
        node_v.p = node_u.p


def tree_maximum(node):
    """
    找到以 node 节点为根节点的树的最大值节点 并返回
    :param node: 以该节点为根节点的树
    :return: 最大值节点
    """
    temp_node = node
    while temp_node.right:
        temp_node = temp_node.right
    return temp_node


def tree_minimum(node):
    """
    找到以 node 节点为根节点的树的最小值节点 并返回
    :param node: 以该节点为根节点的树
    :return: 最小值节点
    """
    temp_node = node
    while temp_node.left:
        temp_node = temp_node.left
    return temp_node


def preorder_tree_walk(node):
    if node:
        print (node.value, node.color)
        preorder_tree_walk(node.left)
        preorder_tree_walk(node.right)


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = RED


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def insert(self, node):
        # 找到最接近的节点
        temp_root = self.root
        temp_node = None
        while temp_root:
            temp_node = temp_root
            if node.value == temp_node.value:
                return False
            elif node.value > temp_node.value:
                temp_root = temp_root.right
            else:
                temp_root = temp_root.left
        # 在相应位置插入节点
        if not temp_node:
            self.root = node
            node.color = BLACK
        elif node.value < temp_node.value:
            temp_node.left = node
            node.p = temp_node
        else:
            temp_node.right = node
            node.p = temp_node
        # 调整树
        self.insert_fixup(node)

    def insert_fixup(self, node):
        if node.value == self.root.value:
            return
        # 为什么是这个终止条件？
        # 因为如果不是这个终止条件那就不需要调整
        while node.p and node.p.color == RED:
            # 只要进入循环则必有祖父节点 否则父节点为根节点 根节点颜色为黑色 不会进入循环
            if node.p == node.p.p.left:
                node_uncle = node.p.p.right
                # 1. 没有叔叔节点 若此节点为父节点的右子 则先左旋再右旋 否则直接右旋
                # 2. 有叔叔节点 叔叔节点颜色为黑色
                # 3. 有叔叔节点 叔叔节点颜色为红色 父节点颜色置黑 叔叔节点颜色置黑 祖父节点颜色置红 continue
                # 注: 1 2 情况可以合为一起讨论 父节点为祖父节点右子情况相同 只需要改指针指向即可
                if node_uncle and node_uncle.color == RED:
                    node.p.color = BLACK
                    node_uncle.color = BLACK
                    node.p.p.color = RED
                    node = node.p.p
                    continue
                elif node == node.p.right:
                    left_rotate(self, node.p)
                    node = node.left
                node.p.color = BLACK
                node.p.p.color = RED
                right_rotate(self, node.p.p)
                return
            elif node.p == node.p.p.right:
                node_uncle = node.p.p.left
                if node_uncle and node_uncle.color == RED:
                    node.p.color = BLACK
                    node_uncle.color = BLACK
                    node.p.p.color = RED
                    node = node.p.p
                    continue
                elif node == node.p.left:
                    right_rotate(self, node)
                    node = node.right
                node.p.color = BLACK
                node.p.p.color = RED
                left_rotate(self, node.p.p)
                return
        # 最后记得把根节点的颜色改为黑色 保证红黑树特性
        self.root.color = BLACK

    def delete(self, node):
        # 找到以该节点为根节点的右子树的最小节点
        node_color = node.color
        if not node.left:
            temp_node = node.right
            transplant(self, node, node.right)
        elif not node.right:
            temp_node = node.left
            transplant(self, node, node.left)
        else:
            # 最麻烦的一种情况 既有左子 又有右子 找到右子中最小的做替换 类似于二分查找树的删除
            node_min = tree_minimum(node.right)
            node_color = node_min.color
            temp_node = node_min.right
            if node_min.p != node:
                transplant(self, node_min, node_min.right)
                node_min.right = node.right
                node_min.right.p = node_min
            transplant(self, node, node_min)
            node_min.left = node.left
            node_min.left.p = node_min
            node_min.color = node.color
        # 当删除的节点的颜色为黑色时 需要调整红黑树
        if node_color == BLACK:
            self.delete_fixup(temp_node)

    def delete_fixup(self, node):
        # 实现过程还需要理解 比如为什么要删除 为什么是那几种情况
        while node != self.root and node.color == BLACK:
            if node == node.p.left:
                node_brother = node.p.right
                if node_brother.color == RED:
                    node_brother.color = BLACK
                    node.p.color = RED
                    left_rotate(self, node.p)
                    node_brother = node.p.right
                if (not node_brother.left or node_brother.left.color == BLACK) and \
                        (not node_brother.right or node_brother.right.color == BLACK):
                    node_brother.color = RED
                    node = node.p
                else:
                    if not node_brother.right or node_brother.right.color == BLACK:
                        node_brother.color = RED
                        node_brother.left.color = BLACK
                        right_rotate(self, node_brother)
                        node_brother = node.p.right
                    node_brother.color = node.p.color
                    node.p.color = BLACK
                    node_brother.right.color = BLACK
                    left_rotate(self, node.p)
                node = self.root
                break
            else:
                node_brother = node.p.left
                if node_brother.color == RED:
                    node_brother.color = BLACK
                    node.p.color = RED
                    left_rotate(self, node.p)
                    node_brother = node.p.right
                if (not node_brother.left or node_brother.left.color == BLACK) and \
                        (not node_brother.right or node_brother.right.color == BLACK):
                    node_brother.color = RED
                    node = node.p
                else:
                    if not node_brother.left or node_brother.left.color == BLACK:
                        node_brother.color = RED
                        node_brother.right.color = BLACK
                        left_rotate(self, node_brother)
                        node_brother = node.p.left
                    node_brother.color = node.p.color
                    node.p.color = BLACK
                    node_brother.left.color = BLACK
                    right_rotate(self, node.p)
                node = self.root
                break
        node.color = BLACK


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()
    for number in number_list:
        node = RedBlackTreeNode(number)
        tree.insert(node)
        del node
    preorder_tree_walk(tree.root)
    tree.delete(tree.root)
    preorder_tree_walk(tree.root)

if __name__ == '__main__':
    main()
```


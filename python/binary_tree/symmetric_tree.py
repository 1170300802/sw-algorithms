#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: symmetric_tree.py

@desc: 判断对称树

@hint: 比较对称位置，递归和非递归。也可以根据前面二叉树反转，来判断两棵树是不是一样。
"""
from binary_tree import BinaryTree


# 递归
def symmetric_tree(root):
    if root is None:
        return True
    return is_symmetric_tree(root.left_child, root.right_child)


def is_symmetric_tree(left_child, right_child):
    if left_child is None or right_child is None:  # 有节点为空时判断
        return left_child == right_child
    return left_child.data == right_child.data and is_symmetric_tree(left_child.left_child, right_child.right_child) \
           and is_symmetric_tree(left_child.right_child, right_child.left_child)

#非递归：参考前序遍历的思路，将需要对比的节点入栈比较。需要注意的是:都为空的情况
def symmetric_tree_two(root):
    if root is None:
        return True
    node_list = []
    node_list.append(root.left_child)
    node_list.append(root.right_child)
    while len(node_list) != 0:
        node_one = node_list.pop()
        node_two = node_list.pop()
        if node_one == node_two is None:
            continue
        if node_one is None or node_two is None:
            return False
        if node_one.data != node_two.data:
            return False
        node_list.append(node_one.left_child)
        node_list.append(node_two.right_child)
        node_list.append(node_one.right_child)
        node_list.append(node_two.left_child)
    return True

if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_symmetric_tree()
    result = symmetric_tree_two(tree.root)
    print(result)

#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: sum_of_left_leaves.py

@desc: 二叉树左叶子节点的和

@hint: 递归和非递归解法， 其中非递归解法可使用层次遍历的方法，如果是做左叶子节点，则计入和。
"""

from binary_tree import BinaryTree


# 最简单的方法，一次全部输出
def sum_of_left_leaves_one(root):
    if root is None:
        return 0
    node_list = []
    sum = 0
    node_list.append(root)
    while len(node_list) != 0:
        temp_node = node_list.pop(0)
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
            #判断是不是叶子
            if temp_node.left_child.left_child is None and temp_node.left_child.right_child is None:
                sum += temp_node.left_child.data
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
    return sum

# 递归解法
def sum_of_left_leaves_two(root):
    if root is None:
        return 0
    ls = sum_of_left_leaves_two(root.left_child)
    rs = sum_of_left_leaves_two(root.right_child)
    #判断是不是左叶子节点
    if root.left_child is not None and root.left_child.left_child is None and root.left_child.right_child is None:
        ls += root.left_child.data
    return ls + rs




if __name__ == '__main__':
    tree = BinaryTree()
    result = sum_of_left_leaves_two(tree.root)
    print(result)

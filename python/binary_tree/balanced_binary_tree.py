#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: balanced_binary_tree.py

@desc: 判断平衡二叉树：一棵空树或它的任意节点的左右两个子树的高度差的绝对值均不超过1。

@hint:  多种方法判断
"""
from binary_tree import BinaryTree

def maximum_depth_of_binary_tree(root):
    if root is None:
        return 0
    return max(maximum_depth_of_binary_tree(root.left_child), maximum_depth_of_binary_tree(root.right_child)) + 1

#递归解法：前面求的树的最大高度。用于这个函数，计算任一节点的两个子树的高度差，即可判断。
def balanced_binary_tree(root):
    if root is None:
        return True
    left_d = maximum_depth_of_binary_tree(root.left_child)
    right_d = maximum_depth_of_binary_tree(root.right_child)
    # if abs(left_d - right_d) > 1:
    #     return False
    return abs(left_d - right_d) < 2 and balanced_binary_tree(root.left_child) and balanced_binary_tree(root.right_child)
#上面方法计算时，每个节点的计算都是重复的，因此在求得左右子树高度时，计算父节点的高度就不用重复计算了。



# 计算高度的同时， 用一个全局变量来保存是否是平衡二叉树,这种方法比较好理解。
def balanced_binary_tree_four(root):
    if root is None:
        return
    getDepth(root)
    return result


def getDepth(root):
    if root is None:
        return 0
    global result
    left_d = getDepth(root.left_child)
    right_d = getDepth(root.right_child)
    if abs(left_d - right_d) > 1:
        result = False
    return max(left_d, right_d) + 1


if __name__ == '__main__':
    tree = BinaryTree()
    # result = balanced_binary_tree_three(tree.root)
    # print(result)
    # tree.create_symmetric_tree()
    # result = balanced_binary_tree_three(tree.root)
    # print(result)
    result = True
    result = balanced_binary_tree_four(tree.root)
    print(result)
    result = True
    tree.create_symmetric_tree()
    result = balanced_binary_tree_four(tree.root)
    print(result)



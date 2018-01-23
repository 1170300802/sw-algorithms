#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_tree.py

@desc: 二叉树的构造

@hint: 对左右子树分别插入
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_tree():
    node_list = []
    for i in range(10):
        node_list.append(Node(i))
    node_list[0].left_child = node_list[1]
    node_list[0].right_child = node_list[2]
    node_list[1].left_child = node_list[3]
    node_list[2].left_child = node_list[4]
    node_list[2].right_child = node_list[5]
    node_list[3].right_child = node_list[7]
    node_list[4].right_child = node_list[9]
    node_list[5].left_child = node_list[6]
    node_list[7].left_child = node_list[8]

    return node_list[0]  #return tree root node


def create_symmetric_tree():
    node_list = [Node(0), Node(1), Node(1), Node(2), Node(2), Node(3), Node(3), Node(4), Node(4), Node(5), Node(5)]
    node_list[0].left_child = node_list[1]
    node_list[0].right_child = node_list[2]
    node_list[1].left_child = node_list[3]
    node_list[1].right_child = node_list[5]
    node_list[2].left_child = node_list[6]
    node_list[2].right_child = node_list[4]
    node_list[5].right_child = node_list[7]
    node_list[6].left_child = node_list[8]
    node_list[7].left_child = node_list[9]
    node_list[8].right_child = node_list[10]

    return node_list[0]  #return tree root node


class BinaryTree:
    def __init__(self):
        # self.treeNode = Node()
        self.root = create_tree()

    def create_symmetric_tree(self):
        self.root = create_symmetric_tree()



if __name__ == '__main__':
    tree = BinaryTree()
    print(tree.root.data)







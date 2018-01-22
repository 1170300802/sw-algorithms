#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: post_order_traversal_tree.py

@desc:  二叉树的后序遍历， 左--右--根

@hint:  递归和非递归
"""
from binary_tree import BinaryTree


def post_order_traversal_tree(root):
    if root is None:
        return
    post_order_traversal_tree(root.left_child)
    post_order_traversal_tree(root.right_child)
    print(root.data, end="   ")


# 非递归遍历
# 思路: 对于任一节点将其入栈。若左右节点都已经访问过，可以访问该节点并出栈。否则将其右子树入栈，左子树入栈，保证左子树在右子树之前访问。
def post_order_traversal_tree_two(root):
    if root is None:
        return
    node_list = []
    node_list.append(root)
    node_set = set()
    node_set.add(None)
    while len(node_list) != 0:
        temp_node = node_list[-1]
        if temp_node.left_child in node_set and temp_node.right_child in node_set:
            print(temp_node.data, end="   ")
            node_list.pop()
            node_set.add(temp_node)
        else:
            if temp_node.right_child is not None:
                node_list.append(temp_node.right_child)
            if temp_node.left_child is not None:
                node_list.append(temp_node.left_child)
    print()

# 对于任一结点P，将其入栈，然后沿其左子树一直往下搜索，直到搜索到没有左孩子的结点，此时该结点出现在栈顶，但是此时不能将其出栈并访问，因此其右孩子还为被访问。
# 所以接下来按照相同的规则对其右子树进行相同的处理，当访问完其右孩子时，该结点又出现在栈顶，此时可以将其出栈并访问。这样就保证了正确的访问顺序。
# 可以看出，在这个过程中，每个结点都两次出现在栈顶，只有在第二次出现在栈顶时，才能访问它。因此需要多设置一个变量标识该结点是否是第一次出现在栈顶。
def post_order_traversal_tree_three(root):
    if root is None:
        return
    node_list = []
    node_set = set()
    node_set.add(None)
    temp_node = root
    while len(node_list) != 0 or temp_node is not None:
        while temp_node is not None:
            node_list.append(temp_node)
            temp_node = temp_node.left_child

        if len(node_list) != 0:
            temp_node = node_list[-1]
            if temp_node not in node_set :  #第一次出现在栈顶，对右子树做相同操作。
                node_set.add(temp_node)
                temp_node = temp_node.right_child
            else:
                print(temp_node.data, end="   ")
                node_list.pop()
                temp_node = None   #最后注意temp_node 出栈后，置为空，防止再次入栈。
    print()


# 另一种方法：
#根节点入栈。根节点出栈并打印。左子树入栈，右子树入栈。重复上述操作。将打印结果反转即是后序遍历的结果。
def post_order_traversal_tree_four(root):
    if root is None:
        return
    node_list = []
    result = []
    node_list.append(root)
    while len(node_list) != 0:
        temp_node = node_list.pop()
        result.append(temp_node.data)
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
    for i in reversed(result):
        print(i, end="   ")
    print()

if __name__ == '__main__':
    tree = BinaryTree()
    # post_order_traversal_tree(tree.root)
    # print()
    post_order_traversal_tree_two(tree.root)
    post_order_traversal_tree_four(tree.root)


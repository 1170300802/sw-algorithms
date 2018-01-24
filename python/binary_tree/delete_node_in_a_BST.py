#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: delete_node_in_a_BST.py

@desc: 删除二叉查找树的节点

@hint:  递归和非递归
"""
from binary_tree import BinaryTree
from binary_tree_level_order_traversal import binary_tree_level_order_traversal_two


def delete_node_in_a_BST(root, key):
    if root is None:
        return None
    if root.left_child is None and root.right_child is None and root.data == key:
        return None
    root = remove_node(root, root,  key)
    return root

def remove_node(node, parent_node,  key):
    if node is None:
        return None
    if node.data > key:  #值在左边
        remove_node(node.left_child, node,  key)
    elif node.data < key:
        remove_node(node.right_child, node, key)
    else:  # find it
        if node.left_child is None and node.right_child is None:  # no children
            if parent_node.left_child == node:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        elif node.left_child is not None and node.right_child is not None:  # two children
            temp_node = node.right_child
            parent_node = node
            while temp_node.left_child is not None:
                parent_node = temp_node
                temp_node = temp_node.left_child
            temp_data = node.data
            node.data = temp_node.data
            temp_node.data = temp_data
            remove_node(temp_node, parent_node, key)  # remove no child node
        else:
            if parent_node == node:
                node = parent_node.right_child if parent_node.left_child is None else parent_node.left_child
            elif node.left_child is None:
                if parent_node.left_child == node:
                    parent_node.left_child = node.right_child
                else:
                    parent_node.right_child = node.right_child
            else:
                if parent_node.left_child == node:
                    parent_node.left_child = node.left_child
                else:
                    parent_node.right_child = node.left_child
    return node

#递归：非递归方法中，因为要保存父节点的信息，因此会加多情况的判断
def delete_node_in_a_BST_two(root, key):
    if root is None:
        return None
    if root.data == key:
        if root.left_child is None:
            return root.right_child
        if root.right_child is None:
            return root.left_child
        root.data = find_replace(root, root.left_child, True) # 找替换节点：左边最大，右边最小
    elif root.data > key:
        root.left_child = delete_node_in_a_BST_two(root.left_child, key)
    else:
        root.right_child = delete_node_in_a_BST_two(root.right_child, key)
    return root

def find_replace(parent_node, node, is_left):
    if node.right_child is None:
        if is_left is True:
            parent_node.left_child = node.left_child
        else:
            parent_node.right_child = node.left_child
        return node.data
    return find_replace(node, node.right_child, False)

if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    result = delete_node_in_a_BST_two(tree.root, 5)
    binary_tree_level_order_traversal_two(result)
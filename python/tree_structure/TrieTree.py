#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: TrieTree.py

@desc: 字典树，前缀树， 单词查找树和键树

@hint:
"""

class TrieNode:
    def __init__(self, c = 'a'):
        self.data = c
        self.is_word = False
        self.child = ['a'] * 26  # 最多26个子节点

class TrieTree:
    def __init__(self):
        self.root = TrieNode('0')


    def insert(self, word):
        temp_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if temp_node.child[index] is None:
                temp_node.child[index] = TrieNode(word[i])
            temp_node = temp_node.child[index]
        temp_node.is_word = True

    def search(self, word):
        temp_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if temp_node.child[index] is None:
                return False
            temp_node = temp_node.child[index]
        return temp_node.is_word

    def start_with(self, word):
        temp_node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if temp_node.child[index] is None:
                return False
            temp_node = temp_node.child[index]
        return True

if __name__ == '__main__':
    trie_tree = TrieTree()
    print(ord('a'))



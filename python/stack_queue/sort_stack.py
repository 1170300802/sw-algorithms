#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: sort_stack.py

@desc: 对栈排序

@hint:  top() 是最小的元素
"""

def sort_stack(stack):
    if len(stack) <= 1:
        return
    helper_stack = []
    pop = stack.pop()
    helper_stack.append(pop)
    while len(stack) != 0:
        if stack[-1] >= helper_stack[-1]:
            helper_stack.append(stack.pop())
        else:
            pop = stack.pop()
            while len(helper_stack) != 0 and helper_stack[-1] > pop:
                stack.append(helper_stack.pop())
            helper_stack.append(pop)
    while len(helper_stack) != 0:
        stack.append(helper_stack.pop())

if __name__ == '__main__':
    stack = []
    stack.append(1)
    stack.append(5)
    stack.append(4)
    stack.append(2)
    stack.append(3)
    print(stack)
    sort_stack(stack)
    print(stack)
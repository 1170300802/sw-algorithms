#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: intersection_of_two_linked_lists.py

@time: 2018/1/17 10:39

@desc:  两链表的交叉点

@hint: 也分为递归和非递归解法
"""

from singly_linked_list_implementation import LinkedList

def create_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    return ll


#普通解法：获取两个链表的长度差，长链表移动到与短链表相同的位置开始比较。
def intersection_of_two_linked_lists_one(node_one, node_two):

    temp_node_one = node_one
    temp_node_two = node_two
    one_length = 0
    two_length = 0
    while temp_node_one is not None:
        one_length += 1
        temp_node_one = temp_node_one.next
    while temp_node_two is not None:
        two_length += 1
        temp_node_two = temp_node_two.next

    if one_length > two_length:
        k = one_length - two_length
        temp_node_one = node_one
        while k > 0:
            temp_node_one = temp_node_one.next
            k -= 1
        temp_node_two = node_two
    else:
        k = two_length - one_length
        temp_node_two = node_two
        while k > 0:
            temp_node_two = temp_node_two.next
            k -= 1
        temp_node_one = node_one

    while temp_node_one is not None:
        if temp_node_one == temp_node_two:
            return temp_node_one.data
        temp_node_one = temp_node_one.next
        temp_node_two = temp_node_two.next
    return -1


#迭代解法：其实思想和上面解法是一样的。用两个节点分别代表两个链表的头节点。
#遍历两个链表，当短链表到达tail时，将长链表头节点赋值给它。此时两个节点之间的节点数就是两链表的长度差值。
#两节点一前一后，继续遍历。当前节点到达tail时，将短链表的头节点复制给它。
#此时后节点刚好是长链表减去k个节点的位置。遍历比较即可得出结果。
def intersection_of_two_linked_lists_two(node_one, node_two):
    if node_one is None or node_two is None:
        return -1
    temp_node_one = node_one
    temp_node_two = node_two
    while temp_node_one != temp_node_two:
        temp_node_one = temp_node_one.next if temp_node_one is not None else node_two
        temp_node_two = temp_node_two.next if temp_node_two is not None else node_one
    if temp_node_one is None:
        return -1
    return temp_node_one.data

# 环解法：遍历两个链表， 其中一个链表到达tail时，将后继节点设为另一链表的head。转换为单链表判断有环问题。
# 可用龟兔赛算法判断是否有环。有环则相交，环入口即为交点。(继续求环长度，带环链表的长度)
# 下面找出交点：快2慢1两节点遍历，相遇时慢节点在环内。用两节点表示头节点和相遇节点，单步向前遍历。相等时即为环入口点。

def intersection_of_two_linked_lists_three(node_one, node_two):
    if node_one is None or node_two is None:
        return -1
    temp_node_one = node_one
    temp_node_two = node_two
    while temp_node_one.next is not None:
        temp_node_one = temp_node_one.next
    temp_node_one.next = temp_node_two
    #判断链表是否是否有环：
    temp_node_fast = node_one
    temp_node_slow = node_one
    while temp_node_fast is not None and temp_node_fast.next is not None:
        temp_node_fast = temp_node_fast.next.next
        temp_node_slow = temp_node_slow.next
        if temp_node_slow == temp_node_fast:
            # 存在环
            meeting_node = temp_node_slow
            break
        if temp_node_fast is None:
            return -1

    #根据相遇节点，求出环的入口节点，即为交叉点
    temp_node_one = node_one
    temp_node_two = meeting_node
    while temp_node_two != temp_node_one:
        temp_node_one = temp_node_one.next
        temp_node_two = temp_node_two.next
    return temp_node_one.data

    #求的相遇点，遍历一遍即可知道环的长度。
    #求的入环点，从头节点遍历到入环点的长度加上环的长度，等于链表的长度


if __name__ == '__main__':
    ll = LinkedList()
    # ll.append(1)
    ll.append(2)
    # ll.append(3)

    l1 = LinkedList()
    l1.append(10)
    l1.append(11)
    # l1.append(12)
    l1.tail.next = ll.head
    l1.print_list_two()

    l2 = LinkedList()
    l2.append(4)
    l2.tail.next = ll.head
    l2.print_list_two()

    result = intersection_of_two_linked_lists_three(l1.head, l2.head)
    print(result)


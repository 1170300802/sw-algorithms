#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: anagram.py

@desc:  同字母异序词:排列与组合

@hint:
"""

def anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    temp = [0] * 26
    for i in range(len(word_one)):
        index = ord(word_one[i]) - ord('a')
        temp[index] += 1
        index = ord(word_two[i]) - ord('a')
        temp[index] -= 1
    for i in temp:
        if i != 0:
            return False
    return True


# 求给定数组的全组合 C(4,4) + C(4,3) + C(4,2) + C(4,1) + C(4, 0)
def all_comb(word, temp):
    back_track(0, word, temp)

def back_track(index, word, temp):
    if index == len(word):
        for i in range(len(temp)):
            if temp[i]:
                print(word[i], end="  ")
        print()
    else:
        temp[index] = True
        back_track(index + 1, word, temp)
        temp[index] = False
        back_track(index + 1, word, temp)

# 求给定数据的全组合  A(4, 4)
def all_comb_two(word):
    if len(word) == 0:
        return word
    else:
        temp = []
        for perm in all_comb_two(word[1:]):
            temp.append(word[0:1] + perm)
        temp.append(word[0:1])
        for perm in all_comb_two(word[1:]):
            temp.append(perm)
        return temp


# 求给定数据的全组合  A(4, 4)
def all_comb_two_yield(word):
    if len(word) == 0:
        yield word
    else:
        for perm in all_comb_two(word[1:]):
            yield (word[0:1] + perm)
        yield (word[0:1])
        for perm in all_comb_two(word[1:]):
            yield (perm)


# 求给定数据的全排列  C(4,4) + C(4,3) + C(4,2) + C(4,1) + C(4, 0)
def all_perms(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in all_perms(word[1:]):
            for i in range(len(word)):
                yield (perm[:i] + word[0:1] + perm[i:])


# 求给定数据的全排列  A(4, 4)
def all_perms_two(word):
    if len(word) <= 1:
        return word
    else:
        temp = []
        for perm in all_perms_two(word[1:]):
            for i in range(len(word)):
                temp.append(perm[:i] + word[0:1] + perm[i:])
        return temp


if __name__ == '__main__':
    a = "apple"
    b = "pleap"
    print(a in all_perms(b))
    print(anagram(a, b))
    # 1: 求出任一的全组合，判断另一个是否在其中

    # 2: 映射判断：两个单词出现的字母数量是一样的

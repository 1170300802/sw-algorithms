#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: quick_sort.py

@desc:  快速排序

@hint:
"""

import random


def quicksort(arr, left, right):
    #only if left < right , go on
    if left >=right:
        return 
    random_index = random.randint(left, right)
    #swap privot and first
    arr[left], arr[random_index] = arr[random_index], arr[left]
    pivot = arr[left]
    lt = left # arr[left+1...lt] < v
    gt = right + 1 # arr[gt...right] > v
    i = left + 1 # arr[lt+1...i] == v
    #when i = gt, stop
    while i < gt:
        if arr[i] < pivot:
            arr[i], arr[lt+1] = arr[lt+1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            gt -= 1
        else:
            i += 1
    #swap first(privot) to v
    arr[left], arr[lt] = arr[lt], arr[left]
    #iterator
    quicksort(arr, left, lt-1)
    quicksort(arr, gt, right)

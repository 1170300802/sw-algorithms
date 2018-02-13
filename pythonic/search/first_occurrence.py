#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: first_occurance.py

@desc: 二分查找首次出现

@hint:
"""


def first_occurrence():
    pass

#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_search.py

@desc: 二分查找

@hint:
"""

def first_occurrence(array, query):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) >> 1
        if mid == 0 and array[mid] == query:
            return mid
        if array[mid] == query and array[mid - 1] != query:
            return mid
        elif array[mid] < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
    print(array)
    print("-----SEARCH-----")
    query = 3
    print("found first: ", query, " in index:", first_occurrence(array, query))
    print("-----SEARCH-----")
    query = 5
    print("found first: ", query, " in index:", first_occurrence(array, query))
    print("-----SEARCH-----")
    query = 7
    print("found first: ", query, " in index:", first_occurrence(array, query))
    print("-----SEARCH-----")
    query = 1
    print("found first: ", query, " in index:", first_occurrence(array, query))
    print("-----SEARCH-----")
    query = -1
    print("found first: ", query, " in index:", first_occurrence(array, query))
    print("-----SEARCH-----")
    query = 9
    print("found first: ", query, " in index:", first_occurrence(array, query))



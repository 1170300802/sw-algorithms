#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: python.py

@desc: 给定一个数组和一个值，求数组中三个数的和与目标值最近的值。返回这3个数的和

@hint: 类似于求目标值为0, 从第一个数开始遍历到倒数第3个。每次3个数的和与之比较
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if s < target:
                    l += 1
                else:
                    r -= 1
                if abs(s - target) < abs(result - target):
                    result = s
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    result = Solution().threeSumClosest(nums, target)
    print(result)


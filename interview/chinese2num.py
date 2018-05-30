#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: chinese2num.py

@desc:

@hint:
"""


# 0--9 的字典表示
MARK_NUM = {
    '零': 0,
    '一': 1,
    '二': 2,
    '三': 3,
    '四': 4,
    '五': 5,
    '六': 6,
    '七': 7,
    '八': 8,
    '九': 9
}

# 进制单位
MARK_UNIT = {
    '十': 10,
    '百': 1e2,
    '千': 1e3,
    '万': 1e4,
    '亿': 1e8,
}

def str2num(str):
    result = 0
    cur_unit = 1
    for i in reversed(str):
        if i in MARK_NUM.keys():
            result += (MARK_NUM[i] * cur_unit)
            # print(cur_unit)
        else:
            if i == '万' or i == '亿':
                cur_unit = MARK_UNIT[i]
                continue
            if MARK_UNIT["亿"] <= cur_unit:
                cur_unit = MARK_UNIT[i] * MARK_UNIT["亿"]
                continue
            if MARK_UNIT["万"] <= cur_unit < 1000 * MARK_UNIT["万"]:
                # 万单位已经出现
                cur_unit = MARK_UNIT[i] * MARK_UNIT["万"]
                continue
            cur_unit = MARK_UNIT[i]
    # 以十结尾的特殊情况
    if str[0] == "十":
        result += 1 * cur_unit
    return result


if __name__ == '__main__':
    str_list = ["五十八", "一百二十三万四千五百六十七", '三千二百一十万零二百一十五', '一亿零九十万零七十六', "十八万"]
    for i in str_list:
        result = str2num(i)
        print(i, "--> %i" % result)
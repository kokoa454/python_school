# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:34:43 2025

@author: qqnq7
"""
def nth(lst, n):
    dt = lst.copy()

    for i in range(len(dt)):
        for j in range(i + 1, len(dt)):
            if dt[i] < dt[j]:
                dt[i], dt[j] = dt[j], dt[i]

    return dt[n - 1]

def nthWithoutCopy(lst, n):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst[n - 1]

# copy()を使用しないと、もともとのリスト内の順序が変更されてしまう。(console参照)
# そのため、一度実引数のリストをコピーして、もともとのリストに影響を与えないほうが同ソートのような使い方には好ましいと考えた。
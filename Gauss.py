#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/18
# @file Gauss.py

"""
--------test-input-1-------
4
0.4096 0.1234 0.3678 0.2943
0.2246 0.3872 0.4015 0.1129
0.3645 0.1920 0.3781 0.0643
0.1784 0.4002 0.2786 0.3927
1.1951 1.1262 0.9989 1.2499
---------------------------

-------test-input-2:-------
4
136.01 90.860 0       0
90.860 98.810 -67.590 0
0     -67.590 132.01 46.260
0      0      46.260 177.17
226.87 122.08 110.68 223.43
---------------------------

-------test-input-3:-------
4
1      0.5    0.3333 0.25
0.5    0.3333 0.25   0.2
0.3333 0.25   0.2    0.1667
0.25   0.2    0.1667 0.1429
2.0833 1.2833 0.95   0.7596
---------------------------

-------test-input-4:-------
4
10     7      8      7
7      5      6      5
8      6      10     9
7      5      9      10
32     23     33     31
---------------------------
"""

from numpy import *
import sys

print("---------高斯消元法---------")

n = int(input("input:\nn,a[i,j],b[i]\n"))

a = zeros((n + 1, n + 1))
for i in range(n):
    row = input().split()
    for j in range(n):
        a[i + 1][j + 1] = float(row[j])

b = [0.0] * (n + 1)
row = input().split()
for i in range(n):
    b[i + 1] = float(row[i])

for k in range(1, n):
    max_a = fabs(a[n, k])
    p = n
    for j in range(k, n):
        # 寻找待操作的行p
        if a[j, k] > max_a:
            max_a = a[j, k]
            p = j
    if max_a == 0:
        print("singular!")
        sys.exit()

    if p != k:
        # 交换p,k两行
        a[[p, k], :] = a[[k, p], :]
        b[p], b[k] = b[k], b[p]

    # 计算
    for i in range(k + 1, n + 1):
        m = a[i, k] / a[k, k]
        for j in range(k, n + 1):
            a[i, j] = a[i, j] - a[k, j] * m
        b[i] = b[i] - b[k] * m

if a[n, n] == 0:
    print("singular!")
    sys.exit()

# 求解x
x = [0.0] * (n + 1)
x[n] = b[n] / a[n, n]
for k in range(n - 1, 0, -1):
    sum = 0
    for j in range(k + 1, n + 1):
        sum += a[k, j] * x[j]
    x[k] = (b[k] - sum) / a[k, k]

# 输出x
for i in range(1, n + 1):
    print(x[i])

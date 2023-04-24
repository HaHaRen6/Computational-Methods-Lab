#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/21
# @file Lagrange.py

"""
-------question1-------
testInput1:

1.0/(x**2+1.0)
5
5
0.75
1.75
2.75
3.75
4.75

1.0/(x**2+1.0)
10
5
0.75
1.75
2.75
3.75
4.75

1.0/(x**2+1.0)
20
5
0.75
1.75
2.75
3.75
4.75


testInput2:

e**x
5
5
0.75
1.75
2.75
3.75
4.75
------------------------


"""

from math import *
from sympy import *

print("----------拉格朗日插值法----------")

t = Symbol('x')
FX = sympify(input())
n = int(input())  # n等分
a = [[0.0] * 2 for i in range(n + 1)]

h = 10.0 / n
for k in range(n + 1):
    a[k][0] = -5.0 + k * h
    a[k][1] = float(FX.subs(t, a[k][0]))

m = int(input())  # 输入插值点个数
for i in range(m):
    x = float(input())
    y = 0.0
    k = 0
    while k <= n:
        l = 1.0
        for j in range(n + 1):
            if j != k:
                l = l * (x - a[j][0]) / (a[k][0] - a[j][0])
        y = y + l * a[k][1]
        k += 1
    print("x:", x, " 近似值:", y, " 真值:", float(FX.subs(t, x)))

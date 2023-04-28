#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/21
# @file Lagrange.py

"""
-------question1-------
testInput1-1:

1.0/(x**2+1.0)
1
5
-5 5
5
0.75
1.75
2.75
3.75
4.75

testInput1-2:

1.0/(x**2+1.0)
1
10
-5 5
5
0.75
1.75
2.75
3.75
4.75

testInput1-3:

1.0/(x**2+1.0)
1
20
-5 5
5
0.75
1.75
2.75
3.75
4.75

testInput2-1:

exp(x)
1
5
-1 1
4
-0.95
-0.05
0.05
0.95

testInput2-2:

exp(x)
1
10
-1 1
4
-0.95
-0.05
0.05
0.95

testInput2-3:

exp(x)
1
20
-1 1
4
-0.95
-0.05
0.05
0.95

-----------------------

-------question2-------
testInput1-1:

1.0/(x**2+1.0)
1
5
-1 1
4
-0.95
-0.05
0.05
0.95

testInput1-2:

1.0/(x**2+1.0)
1
10
-1 1
4
-0.95
-0.05
0.05
0.95

testInput1-3:

1.0/(x**2+1.0)
1
20
-1 1
4
-0.95
-0.05
0.05
0.95

testInput2-1:

exp(x)
1
5
-5 5
4
-4.75
-0.25
0.25
4.75

testInput2-2:

exp(x)
1
10
-5 5
4
-4.75
-0.25
0.25
4.75

testInput2-3:

exp(x)
1
20
-5 5
4
-4.75
-0.25
0.25
4.75

-----------------------

-------question4-------
testInput1:

x**0.5
2
3
1 4 9
4
5
50
115
185

testInput2:

x**0.5
2
3
36 49 64
4
5
50
115
185

testInput3:

x**0.5
2
3
100 121 144
4
5
50
115
185

testInput4:

x**0.5
2
3
169 196 225
4
5
50
115
185

-----------------------
"""

from math import *
from sympy import *

print("----------拉格朗日插值法----------")

t = Symbol('x')
FX = sympify(input("输入f(x)表达式\n"))

print("选择数据点的输入方式")
print("1. 区间n等分（自动生成）")
print("2. 手动输入")
choice = int(input())
if choice == 1:
    n = int(input("n="))  # n等分
    aa, bb = input("区间\n").split(" ")
    aa = float(aa)
    bb = float(bb)
    a = [[0.0] * 2 for i in range(n + 1)]
    h = (bb - aa) / n
    print("\n自动生成数据点")
    print("x\t\t f(x)")
    for k in range(n + 1):
        a[k][0] = aa + k * h
        a[k][1] = float(FX.subs(t, a[k][0]))
    for k in range(n + 1):
        print(format(a[k][0], '.6f'), '\t', format(a[k][1], '.6f'))
elif choice == 2:
    n = int(input("输入个数:"))
    n = n - 1
    a = [[0.0] * 2 for i in range(n + 1)]
    print("输入节点x值")
    inputx = input().split(" ")
    for k in range(n + 1):
        a[k][0] = int(inputx[k])
        a[k][1] = float(FX.subs(t, a[k][0]))
    print("\n数据点")
    print("x\t\t f(x)")
    for k in range(n + 1):
        print(format(a[k][0], '.6f'), '\t', format(a[k][1], '.6f'))

print("\n求解")
m = int(input("插值点个数:")) 
print("插值点")
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
    print(
        "x:", format(x, '.6f'),
        "\t近似值:", format(y, '.8f'),
        "\t真值:", format(float(FX.subs(t, x)), '.8f'),
    )

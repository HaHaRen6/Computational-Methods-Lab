#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/14
# @file Newton.py

"""
test-input-1:
cos(x)-x,0.785398163,1e-6,1e-4,10

test-input-2:
exp(-x)-sin(x),0.6,1e-6,1e-4,10

test-input-3:
x-exp(-x),0.5,1e-6,1e-4,10

test-input-4: x**2-2*x*exp(-x)+exp(-2*x),0.5,1e-6,1e-4,20
"""

from math import *
from sympy import *
import sys

print("-----------牛顿迭代法-----------")

x = Symbol('x')

FX, x0, e1, e2, N = input("input:\nfunction,x0,epsilon1,epsilon2,N\n").split(",")
FX = sympify(FX)
x0 = float(x0)
e1 = float(e1)
e2 = float(e2)
N = int(N)

n = 1
while n <= N:
    F = float(FX.subs(x, x0))
    DF = float(diff(FX, x, 1).subs(x, x0))
    if fabs(F) < e1:
        print(x0)
        sys.exit()
    if fabs(DF) < e2:
        print("failed")
        sys.exit()
    x0 = x0 - F / DF
    Tol = fabs(F / DF)
    if Tol < e1:
        print(x0)
        sys.exit()
    n = n + 1
print("failed")

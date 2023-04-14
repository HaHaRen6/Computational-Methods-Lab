#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/14
# @file Newton-2.2.py
# test input: 0.5 1e-6 1e-4 20

import math
import sys

x, e1, e2, N = map(float, input("input:\nalpha epsilon1 epsilon2 N\n").split())
n = 1

while n <= N:
    F = math.pow(x, 2) - 2 * x * math.pow(math.e, -x) + math.pow(math.e, -2 * x)
    DF = 2 * x - 2 * math.pow(math.e, -x) + 2 * x * math.pow(math.e, -x) - 2 * math.pow(math.e, -2 * x)
    if math.fabs(F) < e1:
        print(x)
        sys.exit()
    if math.fabs(DF) < e2:
        print("failed")
        sys.exit()
    x = x - F / DF
    Tol = math.fabs(F / DF)
    if Tol < e1:
        print(x)
        sys.exit()
    n = n + 1
print("failed")

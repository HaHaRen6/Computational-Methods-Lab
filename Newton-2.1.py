#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author hhr
# @date 2023/4/14
# @file Newton-2.1.py
# test input: 0.5 1e-6 1e-4 10

import math
import sys

x, e1, e2, N = map(float, input("input:\nalpha epsilon1 epsilon2 N\n").split())
n = 1

while n <= N:
    F = x - math.pow(math.e, -x)
    DF = 1 + math.pow(math.e, -x)
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

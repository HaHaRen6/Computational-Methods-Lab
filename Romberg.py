"""
0 1 1e-6 x**2*exp(x)

1 3 1e-6 exp(x)*sin(x)

0 1 1e-6 4/(x**2+1)

0 1 1e-6 1/(x+1)
"""

from sympy import *
from math import *
import sys

x = Symbol("x")
a, b, e, f = input("input:\na,b,epsilon,f\n").split(" ")
a = float(a)
b = float(b)
e = float(e)
f = sympify(f)
# print(float(f.subs(x,1)))

n = 10

t = [[[] for i in range(n)] for i in range(n)]
h = b - a
t[0][0] = h * (f.subs(x, a) + f.subs(x, b)) / 2

for i in range(1, n):
    ii = 2 ** (i - 1)
    sum = 0
    for k in range(1, ii + 1):
        sum += f.subs(x, a + (k - 0.5) * h)
    t[0][i] = t[0][i - 1] / 2 + h / 2 * sum

    for m in range(1, i + 1):
        k = i - m
        t[m][k] = (4**m * t[m - 1][k + 1] - t[m - 1][k]) / (4**m - 1)

    if fabs(t[i][0] - t[i - 1][0]) < e:
        for j in range(i + 1):
            for k in range(i - j + 1):
                print(format(t[j][k], '.8f'), end="\t")
            print()
        print("近似值：", format(t[i][0], '.8f'))
        sys.exit()

    h = h / 2

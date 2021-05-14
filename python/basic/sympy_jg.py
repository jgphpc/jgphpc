#!/usr/bin/env python
# coding: utf-8

# test python sympy OR use /Applications/CSCS/xcas/usr/bin/icas
from __future__ import division
from sympy import *


def symbols_jg():
    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h', cls=Function)
    init_printing()
    x/3+x**2


def expand_jg():
    x, y = symbols('x y')
    expr = x + 2*y
    print(expand(expr*x**2))


def solve_jg():
    x = symbols('x')
    expr = x * x + 2*x - 3
    print(solve(expr))
    # infinity
    # solve(3*(x+1)-2*(x+3)<x-3*x)


def factor_jg():
    x = symbols('x')
    expr = (-2*x**3+8*x-12)/(x*x+2*x-3)
    print(f'{expr} ---factor--- {factor(expr)}')


def simplify_jg():
    a, b = symbols('a b')
    serie_huit_1 = (((a+b)/(a-b) + (a-b)/(a+b))/(((a+b)/(a-b) - (a-b)/(a+b))))
    serie_huit_2 = (2*a*b/(a**2+b**2))
    serie_huit_3 = (((a)/(a-b) - (b)/(a+b))/(((a)/(a+b) + (b)/(a-b))))
    serie_huit = serie_huit_1 * serie_huit_2 * serie_huit_3
    print(simplify(serie_huit))

def cuberoot_jg():
    from sympy.codegen.cfunctions import Cbrt
    # help(Cbrt)
    a, b = symbols('a b')
    g1 = cbrt(a*a*b)
    print(g1)
    # better in notebook


def add_jg(a, b):
    return (a+6*a*b-a*b*b)


if __name__ == "__main__":
    # better in a notebook
    # init_printing(use_unicode=True)
    # expand_jg()
    # solve_jg()
    # factor_jg()
    # simplify_jg()
    cuberoot_jg()
    # res = add_jg(4,-6); print(res)

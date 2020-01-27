#!/usr/bin/env python
# coding: utf-8

from sympy import *
# init_printing(use_unicode=True)
x, y = symbols('x y')
expr = x + 2*y
print(expand(expr*x**2))


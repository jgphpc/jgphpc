#!/bin/env python3
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# {{{
# x = np.arange(0, 10)
# y = np.exp(-x/3.0)
# f = interpolate.interp1d(x, y)
# xnew = np.arange(0, 9, 0.1)
# ynew = f(xnew)   # use interpolation function returned by `interp1d`
# plt.plot(x, y, 'o', xnew, ynew, '-')
# plt.show()
# }}}

np = [5025, 10203, 20081, 45225, 90824, 180917]
nx = [40, 57, 80, 120, 170, 240]
f = interpolate.interp1d(np, nx)
nx2 = f(np)
print(f'np={np}\nnx={nx}\nnx2={nx2}')
for mpi in [1, 2, 4, 12, 24]:
    np2 = mpi * np[0]
    print(mpi, np2, int(f([np2])))

# {{{
# nx = [2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 47,
#       50, 52, 55, 57, 60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87]
# np = [
#     11, 79, 154, 316, 455, 707, 908, 1257, 1517, 1965, 2294, 2828, 3222, 3845,
#     4305, 5025, 5535, 6362, 6946, 7860, 8502, 9506, 10203, 11289, 12073, 13274,
#     14109, 15380, 16286, 17672, 18619, 20081, 21120, 22706, 23783]
# f = interpolate.interp1d(nx, np)
# np2 = f(nx)
# print(f'np={np}\ninterp={np2}\n{np-np2}')
# }}}



# plt.plot(nx, np, 'o', nx, np2, '-')
# plt.show()

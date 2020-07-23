#!/Applications/CSCS/miniconda3/bin/python

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x=[0.65, 1.25, 2.25, 2.7, 3.7, 4.8]
y=[0.1, 0.2, 0.6, 1, 3, 10]

f_linear = interp1d(x, y, kind='linear')
f_nearest = interp1d(x, y, kind='nearest')
f_zero = interp1d(x, y, kind='zero')
f_slinear = interp1d(x, y, kind='slinear')
f_quadratic = interp1d(x, y, kind='quadratic')
f_cubic = interp1d(x, y, kind='cubic')
f_previous = interp1d(x, y, kind='previous')
f_next = interp1d(x, y, kind='next')

xx=[2.1, 2.6, 3.04]
print("linear", f_linear(xx))
print("nearest", f_nearest(xx))
print("zero", f_zero(xx))
print("slinear", f_slinear(xx))
print("quadratic", f_quadratic(xx))
print("cubic", f_cubic(xx))
print("previous", f_previous(xx))
print("next", f_next(xx))

# plt.plot(x, y, 'o', x, f1(x), '-', x, f2(x), '--', x, f3(x), ':')
# plt.show()

# xx=[2.1, 2.6, 3.04]
# xx,f1(xx)
# xx,f2(xx)
# xx,f3(xx)

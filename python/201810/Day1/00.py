#!/usr/bin/env python3

# /usr/bin/time -p ./00.py ## real 11.34
# srun -n1 python -m scorep ./00.py

import numpy

# uncomment the following line for line-by-line profiling with kernprof
@profile 
def dot(a, b):
    """Multiply the matrix a with the matrix b."""
    c = numpy.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                 c[i, j] += a[i, k] * b[k, j]
    return c


# -------------------------
if __name__ == "__main__":
    n = 128
    a = numpy.random.random((n, n))
    b = numpy.random.random((n, n))
    dot(a,b)
    #jupyter: t1_dot = %timeit -o dot(a,b)
    #t1_dot

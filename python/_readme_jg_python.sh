#!/bin/sh

# {{{ math
# sympy:
isympy
from sympy import Symbol, cos
x = Symbol('x')
e = 1/cos(x)
print e.series(x, 0, 10)
# }}}

# {{{ langs
http://www.swig.org/exec.html
https://pythran.readthedocs.io/en/latest/
https://gitlab.com/scemama/irpf90
https://pythran.readthedocs.io/en/latest/
https://github.com/inducer/pycuda
# }}}

# {{{ mpi
https://bitbucket.org/mpi4py/mpi4py
https://bitbucket.org/mpi4py/mpi4py-fft
https://github.com/hpcugent/mympingpong
https://github.com/rainwoodman/python-mpi-bcast
# }}}

# {{{ tools
https://github.com/NERSC/itt-python
# }}}

# {{{ interactive
https://jupyter.nersc.gov/hub/login
https://jupyter.cscs.ch/
https://d3js.org/
# }}}

# {{{ www,sql,moodle,gui
https://pypi.org/project/Flask/
https://ponyorm.com
https://github.com/moodle/moodle
https://glot.io = an open source pastebin with runnable snippets and API.
https://pypi.org/project/PyQt5/
# }}}

#!/usr/bin/env python3
# coding: utf-8

import json
import sys
import re
import numpy as np
from jg import *
import matplotlib
# import matplotlib_terminal                                                      
import matplotlib.pyplot as plt

dims = ['xsmall', 'small', 'medium', 'large']
prg_models = ['SphExa_MPI_Check',
              'SphExa_MPI_OpenMP_Cuda_Check',
              'SphExa_MPI_OpenMP_Target_Check']
prg_envs = ['PrgEnv-gnu', 'PrgEnv-intel', 'PrgEnv-cray', 'PrgEnv-pgi']
# mpi_tasks = [1, 6, 24]  # jenkins restricted to 1 cnode  
# steps_dict = {1: 0, 6: 1, 24: 2, 672: 10}
# cubeside_dict = {1: 30, 6: 30, 24: 100, 672: 300}
cubeside_d = {1: 'xsmall', 6: 'small', 12: 'medium', 672: 'large'}
# -------------------------------
mpi_tasks = [1, 6, 12]
cubeside_dict = {1: 30, 6: 30, 12: 30}
steps_dict = {1: 0, 6: 0, 12: 0}
# -------------------------------

rows = {}
rows = init_dict(dims, prg_models, prg_envs)
# print(rows)
# print('elapsed=', rows['small']['MPI_OpenMP_Target']['gnu']['elapsed'])
# sys.exit(0)

# f = open('./eff_in.json')
f = open('./eff.json')
d = json.load(f)
f.close()

# {{{ prints
# cubeside_d[24]
# print(d, type(d), d.keys())
# print(type(d['runs']), len(d['runs']),
#       d['runs'][0].keys())  # ['perfvars']
# print(d['runs'][0]['testcases'][0].keys(), 
#       type(d['runs'][0]['testcases'][0]['perfvars']))
# for ii in range(len(d['runs'][0]['testcases'])):
#     print(d['runs'][0]['testcases'][ii]['name'])
# print(len(d['runs'][0]['testcases'][0]['perfvars']))
# print(d['runs'][0]['testcases'][0]['perfvars'][0:2])
# print(d['runs'][0]['testcases'][0]['perfvars'][0].keys())
# print(d['runs'][0]['testcases'][0]['perfvars'][0]['name'])
# print(d['runs'][0]['testcases'][0]['perfvars'][0]['value'])
# print(type(d['runs'][0]['testcases'][0]['perfvars'][0]))
# print(d['runs'][0]['testcases'][0]['perfvars'][0].items())

## Elapsed 0.8913 s
## _Elapsed 2 s
## mpi_ranks 1
## cubeside 30
## steps 0
## FindNeighbors 0.1224 s
## MomentumEnergyIAD 0.4107 s
## %MomentumEnergyIAD 46.08 %
## %FindNeighbors 13.73 %
## Total Neighbors 6190320.0
## Avg neighbor count per particle 229.0
## Total energy 20811200000.0 erg
## Internal energy 1000000.0 erg
# }}}

rows = update_dict(d, rows, cubeside_d)

# {{{ rows_labels
dim_first_key = next(iter(rows))  # should be 'xsmall'
prg_model_first_key = next(iter(rows[dim_first_key]))  # should be 'MPI'

rows_labels = list(rows[dim_first_key][prg_model_first_key].keys())
# -> ['gnu', 'intel', 'cray', 'pgi']
### rows_labels = list(rows.keys())
print('rows_labels=', rows_labels)
# sys.exit(0)
# }}}

# {{{ columns_labels
columns_labels = list(rows[dim_first_key].keys())
# -> ['MPI', 'MPI_OpenMP_Cuda', 'MPI_OpenMP_Target']
print('columns_labels=', columns_labels)
# }}}

# {{{ shape data for plot:
dim_to_plot = 'xsmall'
for dim_to_plot in dims:
    myplt_data = shape_data(rows, dim_to_plot, dim_first_key, prg_model_first_key)
    print('myplt_data=', myplt_data)
    plot_data(myplt_data, rows_labels, columns_labels, dim_to_plot)
# }}}

# debug --> exec(open("./reframe_json_sandbox.py").read())

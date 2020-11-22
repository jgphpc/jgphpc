#!/usr/bin/env python3
# coding: utf-8

# import pandas as pd 
# df = pd.read_json('./lammps.json')
import json
f = open('./eff_in.json')
d = json.load(f)
f.close()




cubeside_d = {1: 'xsmall', 6: 'small', 24: 'medium', 672: 'large'}
# cubeside_d[24]
print(d)
type(d)
d.keys()
type(d['runs'])
len(d['runs'])
d['runs'][0].keys() # ['perfvars']
d['runs'][0]['testcases'][0].keys()
type(d['runs'][0]['testcases'][0]['perfvars'])


for ii in range(len(d['runs'][0]['testcases'])):
    print(d['runs'][0]['testcases'][ii]['name'])




len(d['runs'][0]['testcases'][0]['perfvars'])




d['runs'][0]['testcases'][0]['perfvars'][0:2]




d['runs'][0]['testcases'][0]['perfvars'][0].keys()




d['runs'][0]['testcases'][0]['perfvars'][0]['name']




d['runs'][0]['testcases'][0]['perfvars'][0]['value']




type(d['runs'][0]['testcases'][0]['perfvars'][0])




d['runs'][0]['testcases'][0]['perfvars'][0].items()


# # create dict:
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


row = {}
for ii in range(len(d['runs'][0]['testcases'])):
    dd = d['runs'][0]['testcases'][ii]
    print(d['runs'][0]['testcases'][ii]['name'], dd['name'])




row = {}
for ii in range(len(d['runs'][0]['testcases'])):
    dd = d['runs'][0]['testcases'][ii]
    prgenv_ = dd['environment']
    prgmodel_ = dd['name']
    ll = len(dd['perfvars'])
    #print(prgenv_, prgmodel_)
    for lll in range(ll):
        name_ = dd['perfvars'][lll]['name']
        #value_ = d['runs'][0]['testcases'][0]['perfvars'][lll]['value']
        #unit_ = d['runs'][0]['testcases'][0]['perfvars'][lll]['unit']    
        if name_ == 'Elapsed':
            #elapsed_ = d['runs'][0]['testcases'][0]['perfvars'][lll]['value']
            elapsed_ = dd['perfvars'][lll]['value']
        if name_ == 'mpi_ranks':
            mpi_ = dd['perfvars'][lll]['value']
        if name_ == 'cubeside':
            cubeside_ = dd['perfvars'][lll]['value']
        if name_ == 'steps':
            steps_ = dd['perfvars'][lll]['value']
            avg_elapsed_ = elapsed_ / ( steps_ + 1 )
        if name_ == 'Total Neighbors':
            total_neighb_ = dd['perfvars'][lll]['value']
        if name_ == 'Avg neighbor count per particle':
            avg_neighb_ = dd['perfvars'][lll]['value']
        if name_ == 'Total energy':
            total_energy = dd['perfvars'][lll]['value']
        if name_ == 'Internal energy':
            int_energy = dd['perfvars'][lll]['value']
            title_ = cubeside_d[mpi_] + '-' +                      prgmodel_.split('_')[1] + '-' +                      prgenv_.replace('PrgEnv-', '')
        #row[title_] = [total_neighb_, avg_neighb_, total_energy, int_energy]
            row[title_] = [avg_elapsed_]
            print(title_,
                  elapsed_,
                  total_neighb_, avg_neighb_,
                  total_energy, int_energy)




row




rows_labels = list(row.keys())
rows_labels




import numpy as np
list_of_lists = [row[k] for k in row.keys()]
myplt_data = np.array(list_of_lists)
print('myplt_data=', myplt_data)




d['runs'][0]['testcases'][0]['perfvars'][lll]




d['runs'][0]['testcases'][0]['environment']


# # PLOT



from jg import *




import numpy as np
import matplotlib
# import matplotlib_terminal                                                      
import matplotlib.pyplot as plt
import sys




#columns_labels = ['Total Neighbors', 'Avg neighbor per particle',
#                  'Total energy', 'Internal energy']
#columns_labels = ['Elapsed']
columns_labels = ['xsmall']
columns_labels = ['xsmall', 'small']
myplt_data= [[ 0.8846, 0.8846],
 [ 0.5223, 0.8846],
 [10.031, 11 ]]




fig, ax = plt.subplots()
# im, cbar = heatmap(myplt_data, short_rows_labels, columns_labels, ax=ax,
im, cbar = heatmap(myplt_data, rows_labels, columns_labels, ax=ax,
                   cmap="YlGn", cbarlabel="Average Execution Time (s/iteration)")
                   # cmap="YlGn", cbarlabel="Metrics [count|erg]")
texts = annotate_heatmap(im, valfmt="{x:.1f} s")
fig.tight_layout()
plt.show()
#ok plt.savefig('heatmap_matplot_sqpatch.png')
plt.close()









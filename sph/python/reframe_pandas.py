#!/usr/bin/env python3
# coding: utf-8

# >>> for i in range(len(d)): print(i, d[i]['name'])
# 0 Elapsed
# 1 _Elapsed
# 2 domain_distribute
# 3 mpi_synchronizeHalos
# 4 BuildTree
# 5 FindNeighbors
# 6 Density
# 7 EquationOfState
# 8 IAD
# 9 MomentumEnergyIAD
# 10 Timestep
# 11 UpdateQuantities
# 12 EnergyConservation
# 13 SmoothingLength
# 14 %MomentumEnergyIAD
# 15 %Timestep
# 16 %mpi_synchronizeHalos
# 17 %FindNeighbors
# 18 %IAD

import json
import pandas as pd


# jsonfile = 'strong.json'
# jsonfile = '128mpi.json'
jsonfile = '/tmp/POSTPROC/cce_weak.json'
f = open(jsonfile) ;d = json.load(f) ;f.close()
dd = d['runs'][0]['testcases']

mpiL = [] ;ompL = [] ;sideL = [] ;stepL = [] ;commitL = [] ;peL = []
elapsedL = [] ;unitL = []
aL = [];bL = [];cL = [];dL = [];eL = [];fL = [];gL = [];hL = [];iL = []
jL = [];kL = [];lL = [];mL = [];nL = [];oL = []
for job in range(len(dd)):
    name = dd[job]['name'].split('_')
    pe = dd[job]['environment']
    mpiL.append(int(name[2].replace('mpi', '')))
    ompL.append(int(name[3].replace('omp', '')))
    sideL.append(int(name[5].replace('n', '')))
    stepL.append(int(name[6].replace('steps', '')))
    commitL.append(name[7])
    peL.append(pe)
    # {'name': '_Elapsed', 'reference': 0, 'thres_lower': None, 'thres_upper': None, 'unit': 's', 'value': 8}
    for metric in range(len(dd[job]['perfvars'])):
        if dd[job]['perfvars'][metric]['name'] == 'Elapsed': elapsedL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'domain_distribute': aL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'mpi_synchronizeHalos': bL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'BuildTree': cL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'FindNeighbors': dL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'Density': eL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'EquationOfState': fL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'IAD': gL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'MomentumEnergyIAD': hL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'Timestep': iL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'UpdateQuantities': jL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'EnergyConservation': kL.append(dd[job]['perfvars'][metric]['value'])
        if dd[job]['perfvars'][metric]['name'] == 'SmoothingLength': lL.append(dd[job]['perfvars'][metric]['value'])
        # unitL.append(dd[job]['perfvars'][metric]['unit'])

df_dict = {'mpi': mpiL, 'openmp': ompL, 'cubeside': sideL, 'steps': stepL,
           'gitcommit': commitL, 'pe': peL, 'elapsed': elapsedL,
           'domain_distribute': aL, 'mpi_synchronizeHalos': bL, 'BuildTree': cL,
           'FindNeighbors': dL, 'Density': eL, 'EquationOfState': fL,
           'IAD': gL, 'MomentumEnergyIAD': hL, 'Timestep': iL, 'UpdateQuantities': jL,
           'EnergyConservation': kL, 'SmoothingLength': lL,
           }  # , 'unit': unitL}
# print(mpiL, ompL, sideL, stepL, peL)

df = pd.DataFrame(
    df_dict,
    columns = ['mpi', 'openmp', 'cubeside', 'steps', 'gitcommit', 'pe', 'elapsed',
           'domain_distribute', 'mpi_synchronizeHalos', 'BuildTree',
           'FindNeighbors', 'Density', 'EquationOfState',
           'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities',
           'EnergyConservation', 'SmoothingLength',
    ])
# print(df)
print(df[['mpi', 'openmp', 'cubeside', 'steps', 'gitcommit', 'pe', 'elapsed']])

# plot: https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot
# %matplotlib inline
import matplotlib.pyplot as plt
# df[['pe', 'mpi', 'elapsed']]
# df['pe'].isin(['PrgEnv-gnu'])

# a_prgenv[['pe', 'cubeside', 'mpi', 'elapsed']]
# a_prgenv.loc[(tmp['cubeside'] == 50)]['elapsed']
ax = plt.gca()  # gca stands for 'get current axis'
plot_kind = 'line'
# {{{
# cubeside = 50
# tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]
# tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', label=f'cubeside={cubeside}', ax=ax)

# cubeside = 100
# tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]
# tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x', label=f'cubeside={cubeside}', ax=ax)
# 
# cubeside = 200
# tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]
# tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x', label=f'cubeside={cubeside}', ax=ax) #, logy=True, secondary_y=True)
# logy=True
# secondary_y=True
# kind='line', x='mpi', y='', color='green') # , ax=ax)
# }}}

tmpdf1 = df[df['pe'].isin(['PrgEnv-gnu'])]
for cubeside in (tmpdf1['cubeside'].unique()):
    tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]
    tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x',
                label=f'cubeside={cubeside} GNU/9', ax=ax) #, logy=True, secondary_y=True)

tmpdf1 = df[df['pe'].isin(['PrgEnv-cray'])]
for cubeside in (tmpdf1['cubeside'].unique()):
    tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]
    tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x',
                label=f'cubeside={cubeside} CCE/10', ax=ax) #, logy=True, secondary_y=True)

# plt.xticks(tmpdf2['mpi'], tmpdf2['mpi'])
ax.grid(True)
plt.title(f'Walltime (PrgEnv-gnu)')
ax.yaxis.set_label('Elapsed / s')
plt.savefig('eff.png')
#             pe  cubeside  mpi   elapsed
# 1   PrgEnv-gnu        50    1    2.7630
# 3   PrgEnv-gnu       100    1   22.0406

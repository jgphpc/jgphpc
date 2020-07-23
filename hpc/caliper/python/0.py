import pandas as pd
import json
# export PYTHONPATH=/Users/piccinal/Library/Python/3.7/lib/python/site-packages:$PYTHONPATH
import hatchet

# Collecting hatchet
##   Downloading https://files.pythonhosted.org/packages/33/d1/b1479a770f66d962f545c2101630ce1d5592d90cb4f083d38862e93d16d2/pydot-1.4.1-py2.py3-none-any.whl
##   Downloading https://files.pythonhosted.org/packages/64/c2/b80047c7ac2478f9501676c988a5411ed5572f35d1beff9cae07d321512c/PyYAML-5.3.1.tar.gz (269kB)
## Requirement already satisfied: matplotlib in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from hatchet) (3.1.0)
## Requirement already satisfied: numpy in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from hatchet) (1.16.3)
##   Downloading https://files.pythonhosted.org/packages/45/12/1e1ba99fb65df9f7f3724d3232feef35cc044d18604d57492d561e90219f/pandas-0.23.0.tar.gz (13.1MB)
## Requirement already satisfied: pyparsing>=2.1.4 in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from pydot->hatchet) (2.4.0)
## Requirement already satisfied: kiwisolver>=1.0.1 in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from matplotlib->hatchet) (1.1.0)
## Requirement already satisfied: cycler>=0.10 in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from matplotlib->hatchet) (0.10.0)
## Requirement already satisfied: python-dateutil>=2.1 in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from matplotlib->hatchet) (2.8.0)
## Requirement already satisfied: pytz>=2011k in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from pandas==0.23.0->hatchet) (2019.1)
## Requirement already satisfied: setuptools in /usr/local/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib->hatchet) (42.0.2)
## Requirement already satisfied: six in /Users/piccinal/Library/Python/3.7/lib/python/site-packages (from cycler>=0.10->matplotlib->hatchet) (1.12.0)

injg='/tmp/CALIPER/JSON/quicksilver_topdown_counters_ori.json'
injg='/tmp/CALIPER/JSON/df.records'

# OPEN:
myf = open(injg, 'r')

# JSON:
# d=myf.read()
# res_d = json.loads(d)

# PANDAS:
pd.set_option("display.max_columns",0)
pd.set_option("display.max_colwidth",0)
df = pd.concat(pd.read_json(injg, orient='split', lines=True, chunksize=1000))
df = pd.concat(pd.read_json(injg, orient='records', lines=True, chunksize=1000))
# df.columns
# [cali.caliper.version,
#  cali.event.begin,
#  cali.event.end,
#  cali.event.set,

#  event.begin#function,
#  event.end#function,
#  event.set#pthread.id,

#  function,

#  libpfm.counter.BR_MISP_RETIRED:ALL_BRANCHES,
#  libpfm.counter.CPU_CLK_UNHALTED:THREAD_P,
#  libpfm.counter.CYCLE_ACTIVITY:CYCLES_NO_EXECUTE,
#  libpfm.counter.CYCLE_ACTIVITY:STALLS_L1D_PENDING,
#  libpfm.counter.CYCLE_ACTIVITY:STALLS_L2_PENDING,
#  libpfm.counter.CYCLE_ACTIVITY:STALLS_LDM_PENDING,
#  libpfm.counter.IDQ:MS_UOPS,
#  libpfm.counter.IDQ_UOPS_NOT_DELIVERED:CORE,
#  libpfm.counter.INT_MISC:RECOVERY_CYCLES,
#  libpfm.counter.MACHINE_CLEARS:COUNT,
#  libpfm.counter.MEM_LOAD_UOPS_RETIRED:L3_HIT,
#  libpfm.counter.MEM_LOAD_UOPS_RETIRED:L3_MISS,
#  libpfm.counter.RESOURCE_STALLS:SB,
#  libpfm.counter.RS_EVENTS:EMPTY_CYCLES,
#  libpfm.counter.UOPS_EXECUTED:CORE_CYCLES_GE_1,
#  libpfm.counter.UOPS_EXECUTED:CORE_CYCLES_GE_2,
#  libpfm.counter.UOPS_EXECUTED:THREAD,
#  libpfm.counter.UOPS_ISSUED:ANY,
#  libpfm.counter.UOPS_RETIRED:RETIRE_SLOTS,

#  mpi.rank,
#  mpi.size,
#  time.inclusive.duration,
#  time.offset]
df2 = df.dropna(subset=['function'])
# df2.to_json(r'/tmp/CALIPER/JSON/df3', orient='records')
## df2.to_csv(r'df2', header=None, index=None, sep=' ', mode='a')
## help(pd.DataFrame.to_json)

# ----------------------
# {{{ df = pd.read_json(injg)

##    3 papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##    4 papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##    4 papi.INT_MISC:RECOVERY_CYCLES,
##    4 papi.UOPS_ISSUED:ANY,
##    4 papi.UOPS_RETIRED:RETIRE_SLOTS,

## Columns: [avg#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  avg#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  avg#papi.INT_MISC:RECOVERY_CYCLES,
##  avg#papi.UOPS_ISSUED:ANY,
##  avg#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  count,
# {{{
##  histogram.bin.0#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.0#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.0#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.0#papi.UOPS_ISSUED:ANY,
##  histogram.bin.0#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.1#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.1#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.1#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.1#papi.UOPS_ISSUED:ANY,
##  histogram.bin.1#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.2#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.2#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.2#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.2#papi.UOPS_ISSUED:ANY,
##  histogram.bin.2#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.3#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.3#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.3#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.3#papi.UOPS_ISSUED:ANY,
##  histogram.bin.3#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.4#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.4#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.4#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.4#papi.UOPS_ISSUED:ANY,
##  histogram.bin.4#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.5#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.5#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.5#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.5#papi.UOPS_ISSUED:ANY,
##  histogram.bin.5#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.6#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.6#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.6#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.6#papi.UOPS_ISSUED:ANY,
##  histogram.bin.6#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.7#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.7#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.7#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.7#papi.UOPS_ISSUED:ANY,
##  histogram.bin.7#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.8#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.8#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.8#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.8#papi.UOPS_ISSUED:ANY,
##  histogram.bin.8#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  histogram.bin.9#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  histogram.bin.9#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  histogram.bin.9#papi.INT_MISC:RECOVERY_CYCLES,
##  histogram.bin.9#papi.UOPS_ISSUED:ANY,
##  histogram.bin.9#papi.UOPS_RETIRED:RETIRE_SLOTS,
# }}} 
##  max#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  max#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  max#papi.INT_MISC:RECOVERY_CYCLES,
##  max#papi.UOPS_ISSUED:ANY,
##  max#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  min#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  min#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  min#papi.INT_MISC:RECOVERY_CYCLES,
##  min#papi.UOPS_ISSUED:ANY,
##  min#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  path,
##  sum#papi.CPU_CLK_THREAD_UNHALTED:THREAD_P,
##  sum#papi.IDQ_UOPS_NOT_DELIVERED:CORE,
##  sum#papi.INT_MISC:RECOVERY_CYCLES,
##  sum#papi.UOPS_ISSUED:ANY,
##  sum#papi.UOPS_RETIRED:RETIRE_SLOTS,
##  topdown.backend_bound,
##  topdown.bad_speculation,
##  topdown.frontend_bound,
##  topdown.retiring]
# ----------------------
# df.iloc[10:12]
# df.nlargest(5, 'topdown.backend_bound')[['path', 'topdown.backend_bound']]
# df.nlargest(5, 'topdown.bad_speculation')[['path', 'topdown.bad_speculation']]
# df.nlargest(5, 'topdown.frontend_bound')[['path', 'topdown.frontend_bound']]
# df.nlargest(5, 'topdown.retiring')[['path', 'topdown.retiring']]
# df.loc[df['path'] == 'main'][['path', 'topdown.backend_bound', 'topdown.bad_speculation', 'topdown.frontend_bound', 'topdown.retiring']]
#OK: 
dfm2 = dfm.nlargest(5, 'topdown.backend_bound')
#non dfm2[['path', 'topdown.backend_bound']]
dfm2[['path', 'topdown.backend_bound']][1:]
dfm2.to_csv('o.csv')

>>> dfm2['topdown.backend_bound'] # <class 'pandas.core.series.Series'>
70    0.847790
15    0.819395
>>> dfm[['path', 'topdown.backend_bound']][1:5]
                                path  topdown.backend_bound
1  main                               0.451878
2  main/getParameters/supplyDefaults  0.519329
3  main/printParameters               0.562137
4  main/printParameters/operator<<    0.555843
# }}}


# df2['function'] = df2['function'].transform(lambda l: tuple(l.split('/')))
# AttributeError: 'Series' object has no attribute 'split'
df2.head()
# df2['function'][1:4]
# 115    main/cycleTracking/SumTasks
# 117    main/cycleTracking         
# 119    main/cycleTracking   
aggregators = dict([ (c, 'sum') for c in filter(lambda col: 'libpfm' in col, df.columns)])
aggregators['time.inclusive.duration'] = 'max'
aggregators['cali.caliper.version'] = 'count'
type(aggregators)
aggregators
# dict: {}
# 'libpfm.counter.BR_MISP_RETIRED:ALL_BRANCHES':'sum'
# 'libpfm.counter.CPU_CLK_UNHALTED:THREAD_P':'sum'
# 'libpfm.counter.CYCLE_ACTIVITY:CYCLES_NO_EXECUTE':'sum'
# 'libpfm.counter.CYCLE_ACTIVITY:STALLS_L1D_PENDING':'sum'
# 'libpfm.counter.CYCLE_ACTIVITY:STALLS_L2_PENDING':'sum'
# 'libpfm.counter.CYCLE_ACTIVITY:STALLS_LDM_PENDING':'sum'
# 'libpfm.counter.IDQ:MS_UOPS':'sum'
# 'libpfm.counter.IDQ_UOPS_NOT_DELIVERED:CORE':'sum'
# 'libpfm.counter.INT_MISC:RECOVERY_CYCLES':'sum'
# 'libpfm.counter.MACHINE_CLEARS:COUNT':'sum'
# 'libpfm.counter.MEM_LOAD_UOPS_RETIRED:L3_HIT':'sum'
# 'libpfm.counter.MEM_LOAD_UOPS_RETIRED:L3_MISS':'sum'
# 'libpfm.counter.RESOURCE_STALLS:SB':'sum'
# 'libpfm.counter.RS_EVENTS:EMPTY_CYCLES':'sum'
# 'libpfm.counter.UOPS_EXECUTED:CORE_CYCLES_GE_1':'sum'
# 'libpfm.counter.UOPS_EXECUTED:CORE_CYCLES_GE_2':'sum'
# 'libpfm.counter.UOPS_EXECUTED:THREAD':'sum'
# 'libpfm.counter.UOPS_ISSUED:ANY':'sum'
# 'libpfm.counter.UOPS_RETIRED:RETIRE_SLOTS':'sum'
# 'time.inclusive.duration':'max'
# 'cali.caliper.version':'count'

# CLOSE:
myf.close()

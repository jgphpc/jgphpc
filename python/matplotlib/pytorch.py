#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#                             'dom:gpu' d['runs'][0]['testcases'][0]['system']
#       * num_tasks: 8        len(d['runs'][0]['testcases'][0]['nodelist'])
#       * elapsed: 20 s                                                0
#       * throughput_per_gpu: 201.8 images/s                           1
#       * throughput_per_job: 1614.0 images/s                          2 

#       * min_gpu_use: 69 %                                            3 
#       * avg_gpu_use: 70.0 %                                          4
#       * max_gpu_use: 70 %                                            5 

#       * min_gpu_mem: 62.0 %                                          6
#       * avg_gpu_mem: 62.0 %                                          7             
#       * max_gpu_mem: 62.0 % d['runs'][0]['testcases'][0]['perfvars'][8]['value']

# import json ;f = open('./eff.json') ;d = json.load(f) ;f.close() ;dd = d['runs'][0]['testcases']
import json
f = open('./eff.json')
d = json.load(f)
f.close()
# ref_testname = 'inception_v3'
ref_testname = 'resnet50'

min_mem = [] ;avg_mem = [] ;max_mem = []
min_compute = [] ;avg_compute = [] ;max_compute = []
gpu_elapsed = [] ;throughput_per_gpu = []
# {{{ read data
dd = d['runs'][0]['testcases']
for i in range(len(dd)):
    # if ((ref_testname in dd[i]['name']) and (dd[i]['result'] == 'success') and (batch_size < 256)):
    if ref_testname in dd[i]['name']:
        batch_size = int(dd[i]['name'].split("_")[-1])
        # if (dd[i]['result'] == 'success' and batch_size < 256):
        print(i, dd[i]['name'], batch_size)
        # Elapsed time:
        gpu_elapsed.append(dd[i]['perfvars'][0]['value'])
        # throughput_per_gpu:
        throughput_per_gpu.append(dd[i]['perfvars'][1]['value'])
        # throughput_per_gpu.append(dd[i]['perfvars'][2]['value'])
        # GPU compute:
        min_compute.append(dd[i]['perfvars'][3]['value'])
        avg_compute.append(dd[i]['perfvars'][4]['value'])
        max_compute.append(dd[i]['perfvars'][5]['value'])
        # GPU top memory:
        min_mem.append(dd[i]['perfvars'][6]['value'])
        avg_mem.append(dd[i]['perfvars'][7]['value'])
        max_mem.append(dd[i]['perfvars'][8]['value'])

# input()
# print(gpu_use_max, len(gpu_use_max))
# print(f"ind={ind}")
# }}}

width = 0.9 # 0.15  # the width of the bars
# {{{ PLOT: batch_size 8:96
fig, ax = plt.subplots()
outps = f'{ref_testname}_gpu_batchsize'
elapsed = {}
ydata = {}
usedata = {}
memdata = {}
job_size = []
for i in range(len(dd)):
    batch_size = int(dd[i]['name'].split("_")[-1])
    cn = len(dd[i]['nodelist'])
    if ((ref_testname in dd[i]['name'])): # and cn == 1):
    # if ((ref_testname in dd[i]['name']) and (dd[i]['result'] == 'success') and (batch_size < 256)):
        # print(ref_testname in dd[i]['name'], ref_testname, dd[i]['name'])
        # print(dd[i]['result'] == 'success', dd[i]['result'])
        # print(batch_size < 256, batch_size)
        # print(job_size, dd[i]['perfvars'][0]['value']) # = elapsed
        if not batch_size in ydata.keys():
            ydata[batch_size] = (dd[i]['perfvars'][1]['value'],)
            usedata[batch_size] = (dd[i]['perfvars'][5]['value'],)
            memdata[batch_size] = (dd[i]['perfvars'][8]['value'],)
            # elapsed[batch_size] = (dd[i]['perfvars'][1]['value'],)
        else:
            ydata[batch_size] += (dd[i]['perfvars'][1]['value'],)
            usedata[batch_size] += (dd[i]['perfvars'][5]['value'],)
            memdata[batch_size] += (dd[i]['perfvars'][8]['value'],)

        if not len(dd[i]['nodelist']) in job_size:
            job_size.append(len(dd[i]['nodelist']))
            sysname = dd[i]['system']
            testname = dd[i]['name']

print("ydata=", ydata, ydata.keys(), len(ydata), type(ydata[64]))
print("usedata=", usedata, usedata.keys(), len(usedata), type(usedata[64]))
print("max_compute=", max_compute, len(max_compute), type(max_compute))
print("memdata=", memdata, memdata.keys(), len(memdata), type(memdata[64]))
# print(elapsed, elapsed.keys(), len(elapsed), type(elapsed[64]))
# {64: (26, 18, 20), 128: (27, 28, 30)} dict_keys([64, 128]) 2 <class 'tuple'>
# input()

ind = np.arange(len(job_size))  # the x locations for the groups
# print(job_size, len(job_size))
# print(f"ind: {ind}")
# print(f"1: {ind - width/2}, {elapsed[64]}, {width/2}")
bsize =  8; rects = ax.bar(ind - 2*width/5, ydata[bsize], width/5, label=f'batch_size:{bsize}')
bsize = 16; rects = ax.bar(ind - 1*width/5, ydata[bsize], width/5, label=f'batch_size:{bsize}')
bsize = 32; rects = ax.bar(ind            , ydata[bsize], width/5, label=f'batch_size:{bsize}')
bsize = 64; rects = ax.bar(ind + 1*width/5, ydata[bsize], width/5, label=f'batch_size:{bsize}')
bsize = 96; rects = ax.bar(ind + 2*width/5, ydata[bsize], width/5, label=f'batch_size:{bsize}')
# rects2 = ax.bar(ind + width/2, ydata[96], width/2, label=f'Img/sec per GPU, batch_size:96')
## print(f"gpu_elapsed: {gpu_elapsed}")
# ind2 = np.arange(len(max_compute)/2)
ind2 = np.arange(0-2*width/5, 0+3*width/5, width/5)
rects = ax.plot(ind2, tuple(max_compute[0:int(len(max_compute)/2)]), 'bo-', label='gpu max use (%)')
rects = ax.plot(ind2, tuple(max_mem[0:int(len(max_mem)/2)]), 'b.-', label='gpu_memory max use (%)')
rects = ax.plot(ind2, tuple(gpu_elapsed[0:int(len(max_mem)/2)]), 'bx-', label='Walltime (s)')

ind2 = np.arange(1-2*width/5, 1+3*width/5, width/5)
rects = ax.plot(ind2, tuple(max_compute[int(len(max_compute)/2):]), 'bo-') # , label='gpu max use (%)')
rects = ax.plot(ind2, tuple(max_mem[int(len(max_mem)/2):]), 'b.-') # , label='gpu_memory max use (%)')
rects = ax.plot(ind2, tuple(gpu_elapsed[int(len(max_mem)/2):]), 'bx-') # , label='Walltime (s)')
# rects = ax.plot(ind - 2*width/5, memdata[bsize], 'bo-', label='gpu_max_memory use')
## rects3 = ax.plot(ind, tuple(gpu_elapsed[0::2]), 'bx-', label='elapsed, batch_size:64')
## rects4 = ax.plot(ind, tuple(gpu_elapsed[1::2]), 'rx-', label='elapsed, batch_size:128')

ax.set_ylabel('Img/sec per GPU')
ax.set_xlabel('GPU nodes')
ax.set_title(f'Elapsed time and Throughput\n({sysname}, {testname})')
ax.grid(True)
ax.set_xticks(ind)
ax.set_xticklabels(tuple(job_size))

# ax.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, ncol=3, fontsize=6)

second_ax = ax.secondary_yaxis('right')
# second_ax.set_ylim([0, 100])
second_ax.set_ylabel('GPU max use (%)')
fig.tight_layout()
# plt.show()
plt.draw()
plt.savefig(f'{outps}.png') ;print(f"done {outps}")
input()
# }}}

# {{{ PLOT: batch_size
# 12 PytorchHorovodTest_resnet50_1_64 64
# 13 PytorchHorovodTest_resnet50_1_128 128
#
# 16 PytorchHorovodTest_resnet50_2_64 64
# 17 PytorchHorovodTest_resnet50_2_128 128
#
# 20 PytorchHorovodTest_resnet50_8_64 64
# 21 PytorchHorovodTest_resnet50_8_128 128
fig, ax = plt.subplots()
outps = f'{ref_testname}_gpu_batchsize'
elapsed = {}
job_size = []
for i in range(len(dd)):
    batch_size = int(dd[i]['name'].split("_")[-1])
    if ((ref_testname in dd[i]['name']) and (dd[i]['result'] == 'success') and (batch_size < 256)):
        # print(ref_testname in dd[i]['name'], ref_testname, dd[i]['name'])
        # print(dd[i]['result'] == 'success', dd[i]['result'])
        # print(batch_size < 256, batch_size)
        # print(job_size, dd[i]['perfvars'][0]['value']) # = elapsed
        if not batch_size in elapsed.keys():
            elapsed[batch_size] = (dd[i]['perfvars'][1]['value'],)
        else:
            elapsed[batch_size] += (dd[i]['perfvars'][1]['value'],)

        if not len(dd[i]['nodelist']) in job_size:
            job_size.append(len(dd[i]['nodelist']))
            sysname = dd[i]['system']
            testname = dd[i]['name']

print(elapsed, elapsed.keys(), len(elapsed), type(elapsed[64]))
# {64: (26, 18, 20), 128: (27, 28, 30)} dict_keys([64, 128]) 2 <class 'tuple'>
# input()

ind = np.arange(len(elapsed)+1)  # the x locations for the groups
# print(f"ind: {ind}")
# print(f"1: {ind - width/2}, {elapsed[64]}, {width/2}")
rects1 = ax.bar(ind - width/2, elapsed[64], width/2, label=f'Img/sec per GPU, batch_size:64')
# print(f"2: {ind + width/2}, {elapsed[128]}, {width/2}")
rects2 = ax.bar(ind + width/2, elapsed[128], width/2, label=f'Img/sec per GPU, batch_size:128')

## print(f"gpu_elapsed: {gpu_elapsed}")
rects3 = ax.plot(ind, tuple(gpu_elapsed[0::2]), 'bx-', label='elapsed, batch_size:64')
rects4 = ax.plot(ind, tuple(gpu_elapsed[1::2]), 'rx-', label='elapsed, batch_size:128')
ax.set_xticks(ind)
## job_size = []
## for i in range(len(dd)):
##     batch_size = int(dd[i]['name'].split("_")[-1])
##     # print("i=", i, ref_testname in dd[i]['name'], ref_testname, dd[i]['name'])
##     # print(dd[i]['result'] == 'success', dd[i]['result'])
##     # print(batch_size < 256, batch_size)
##     # print(len(dd[i]['nodelist']))
##     if ((ref_testname in dd[i]['name']) and (dd[i]['result'] == 'success') and (batch_size < 256)):
##     # if ref_testname in dd[i]['name']:

ax.grid(True)
ax.set_ylabel('Elapsed time / s')
ax.set_xlabel('Compute nodes')
# ax.set_title(f'Elapsed time')
ax.set_title(f'Elapsed time and Throughput\n({sysname}, {testname})')
# ax.set_ylim([0, 100])
ax.set_xticklabels(tuple(job_size))

# ax.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, ncol=2)

second_ax = ax.secondary_yaxis('right')
second_ax.set_ylabel('Img/sec per GPU')
fig.tight_layout()
# plt.show()
plt.draw()
plt.savefig(f'{outps}.png') ;print(f"done {outps}")
input()
# }}}

# {{{ PLOT: gpu compute
fig, ax = plt.subplots()
gpu_use_min = tuple(min_compute) ;gpu_use_avg = tuple(avg_compute) ;gpu_use_max = tuple(max_compute)
outps = f'{ref_testname}_gpu_usage'
ind = np.arange(len(gpu_use_avg))  # the x locations for the groups
rects1 = ax.bar(ind - width/3, gpu_use_min, width/3, label='gpu_use_min')
rects2 = ax.bar(ind, gpu_use_avg, width/3, label='gpu_use_avg')
rects3 = ax.bar(ind + width/3, gpu_use_max, width/3, label='gpu_use_max')
ax.set_xticks(ind)
job_size = []
for i in range(len(dd)):
    # print(f"test={ref_testname} name={dd[i]['name']} i={i}")
    # if 'inception_v3' in dd[i]['name']:
    if ref_testname in dd[i]['name']:
        # print(f"i={i} found")
        job_size.append(len(dd[i]['nodelist']))
        sysname = dd[i]['system']
        testname = dd[i]['name']


ax.grid(True)
ax.set_ylabel('GPU usage / %')
ax.set_xlabel('Compute nodes')
ax.set_title(f'GPU usage\n({sysname}, {testname})')
# print(f"j={job_size}")
ax.set_ylim([0, 100])
## ax.set_xticklabels(tuple(job_size))
ax.legend()
fig.tight_layout()
# plt.show()    
plt.draw()
plt.savefig(f'{outps}.png') ;print(f"done {outps}")
# input()
# }}}

# {{{ PLOT: gpu memory
fig, ax = plt.subplots()
gpu_use_min = tuple(min_mem) ;gpu_use_avg = tuple(avg_mem) ;gpu_use_max = tuple(max_mem)
outps = f'{ref_testname}_gpu_memory'
ind = np.arange(len(gpu_use_avg))  # the x locations for the groups
rects1 = ax.bar(ind - width/3, gpu_use_min, width/3, label='gpu_use_min')
rects2 = ax.bar(ind, gpu_use_avg, width/3, label='gpu_use_avg')
rects3 = ax.bar(ind + width/3, gpu_use_max, width/3, label='gpu_use_max')
ax.set_xticks(ind)
job_size = []
for i in range(len(dd)):
    if ref_testname in dd[i]['name']:
        job_size.append(len(dd[i]['nodelist']))
        sysname = dd[i]['system']
        testname = dd[i]['name']

ax.grid(True)
ax.set_ylabel('GPU usage / %')
ax.set_xlabel('Compute nodes')
ax.set_title(f'High watermark GPU memory usage\n({sysname}, {testname})')
# print(f"j={job_size}")
ax.set_ylim([0, 100])
## ax.set_xticklabels(tuple(job_size))
ax.legend()
fig.tight_layout()
# plt.show()    
plt.draw()
plt.savefig(f'{outps}.png') ;print(f"done {outps}")
# }}}

# {{{ PLOT: elapsed
fig, ax = plt.subplots()
# gpu_use_min = tuple(min_mem) ;gpu_use_avg = tuple(avg_mem) ;gpu_use_max = tuple(max_mem)
outps = f'{ref_testname}_gpu_elapsed'
ind = np.arange(len(gpu_elapsed))  # the x locations for the groups
rects1 = ax.plot(ind, tuple(gpu_elapsed), 'bx-', label='elapsed')
rects2 = ax.bar(ind, tuple(throughput_per_gpu), width, label='Img/sec per GPU')
ax.set_xticks(ind)
job_size = []
for i in range(len(dd)):
    if ref_testname in dd[i]['name']:
        job_size.append(len(dd[i]['nodelist']))
        sysname = dd[i]['system']
        testname = dd[i]['name']

ax.grid(True)
ax.set_ylabel('Elapsed time / s')
ax.set_xlabel('Compute nodes')
ax.set_title(f'Elapsed time\n({sysname}, {testname})')
# ax.set_ylim([0, 100])
## ax.set_xticklabels(tuple(job_size))
ax.legend()
second_ax = ax.secondary_yaxis('right')
second_ax.set_ylabel('Img/sec per GPU')
fig.tight_layout()
# plt.show()
plt.draw()
plt.savefig(f'{outps}.png') ;print(f"done {outps}")
# }}}

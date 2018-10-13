#!/usr/bin/env python3

# Thanks goes to Peter Messmer at NVIDIA

# mll daint-gpu PyExtensions/3.6.1.1-CrayGNU-17.08

# https://github.com/eth-cscs/pyfr/issues/11
#     Gray are the compute nodes
#     Yellow the service nodes
#     Blue the nodes allocated in the run
#     Red the failed node

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import re
import sys

# 2018/06: row0=mc rows1-3=gpu, row3=8cabs only

# hostlist -e `sacct -j 1323038 -o nodelist -P |grep -m1 ^nid` > nids.daint

# first=c0-0c0s0n1 last=s7-3c2s15n3 / c(0-9)-(0-3)c(0-2)s(0-15)n(0-3)
#                                     cab     row chassis blade  cn
#                                  <= 10     *4  *3      *16    *4 = 7680 (delta=551)
# grep service xtprocadmin.daint     |wl     # =  117
# grep compute xtprocadmin.daint     |wl     # = 7129
# grep -v NODENAME xtprocadmin.daint |wl # = 7246

## 1 electrical group = 384cn

# ## --- cabinets:
#     741 c0
#     753 c1
#     737 c2
#     753 c3
#     745 c4
#     757 c5
#     759 c6
#     768 c7
#     564 c8
#     552 c9
# average = 712.9 cn / cabinet
# 
# ## --- rows:
#    1809 0
#    1880 1
#    1904 2
#    1536 3
# average = 1782.25 cn / row

#old daint-: 5320n=52services+5268cn
#old     566 c0
#old     570 c1
#old     564 c2
#old     576 c3
#old     564 c4
#old     576 c5
#old     566 c6
#old     576 c7
#old     378 c8
#old     384 c9
#old c6-0c0s1n3: cab0-9 row0-2 chassis0-2 slotblade0-15 cn0-3
#old                   <= 10*3*3*16*4 = 5760cn

#old santis: cab0-0 row0-0 chassis0-2 slotblade0-15 cn0-3
#old                   <= 1*1*3*16*4 = 192cn

cpuDx = 4
cpuDy = 4

slotDx = 4 * cpuDx + 2
slotDy = 1 * cpuDy + 2

cageDx =  1 * slotDx + 4
cageDy = 16 * slotDy + 2

cabinetDx = 4 * cageDx + 6
cabinetDy = 1 * cageDy + 6

# fileTopo = 'DaintTopo.txt'
#fileTopo = 'santistopo.txt'
fileTopo = 'xtprocadmin.daint'
fileNodes= 'nodes.txt'
#fileImage= 'image.png'

def parseTopo(filename, nodes):
  f = open(filename, 'r')
  f.readline()
  for line in f:
    words = line.split()
    nid = int(words[0])
    nodes[nid] = [words[0],words[2], words[3], words[4]]
  f.close()


def posToCoord(p):
  return re.findall(r'(\d+)', p)


def initNodeArray():
  # 
  nodeArray = np.zeros([4 * cabinetDx, 10 * cabinetDy, 3])
  #nodeArray = np.zeros([3 * cabinetDx, 10 * cabinetDy, 3])
  return nodeArray


def paintNode(nA, node, color):
  (x, y, g, s, n) = posToCoord(node)
  px = int(y) * cabinetDx + int(g) * cageDx + int(n) * cpuDx
  py = int(x) * cabinetDy + int(s) * slotDy
  #print(node, x, y, g, s, n)
  nA[px:px+cpuDx-1, py:py+cpuDy-1, :] = color


def paintTopo(nA, node):
  if node[2] == "compute":
       color = [0.5, 0.5, 0.5]
  elif node[2] == "service":
       color = [1, 1, 0]
  else:
       color = [1, 0, 0]

  paintNode(nA, node[1], color)
  #print(node, x, y, g, s, n, px, py) 


def paintNodeList(nA, nodes):
  #f = open('nodes.txt', 'r') 
  f = open(fileNodes, 'r')
  for line in f:
     n =  int(line.strip())
     nodeStr = nodes[n][1]
     color = [0, 1, 1]
     #print( n)
     print(nodes[n])
     paintNode(nA, nodeStr, color)

def paintFaultNodes(nA,  nodes, faultNodes):
  for i in faultNodes:
     n = int(i)
     nodeStr = nodes[n][1]
     color = [1, 0, 0]
     paintNode(nA, nodeStr, color)

#---
# python crayvis_pmessmer.py nodes.txt eff.png
# nodes.txt
# eff.png
# []
# ['10', 'c0-0c0s2n2', 'compute', 'up']
# ['0', '0', '0', '2', '2']

args = []
for i in sys.argv:
    args.append(i)
args.pop(0)
fileTopo = args.pop(0)
fileNodes = args.pop(0)
fileImage = args.pop(0)
print('in1=', fileTopo)
print('in2=', fileNodes)
print('out=', fileImage)
faultNodes = args
print('fault=',faultNodes)

nodes = dict()
#parseTopo('DaintTopo.txt', nodes)
parseTopo(fileTopo, nodes)
#print(nodes)
#ok print('cn[10]=', nodes[10])
#ok print('cn[10]=', posToCoord(nodes[10][1]))
nodeArray = initNodeArray()

for n in nodes:
  #print(nodes[n])
  paintTopo(nodeArray, nodes[n])

paintNodeList(nodeArray, nodes)

paintFaultNodes(nodeArray, nodes, faultNodes)


# bof:
#plt.figure()
#plt.imshow(nodeArray)
#plt.text(5, 95, "Don't use Jet!", color="white", fontsize=10)
##plt.show()
#plt.savefig('eff.png')
#quit()

#ok:
#img.imsave("out.png", nodeArray)
img.imsave(fileImage, nodeArray)

"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#for c, z in zip(['b', 'r', 'y', 'g', 'b'], [40000, 30000, 10000, 5000, 1000]):
for c, z in zip(['b', 'r', 'y', 'g', 'b'], [40,30,20,10,0]):
    #xs = np.arange(6)
    #ys = np.random.rand(6)
    xs = [1,2,3,4,5,6]  # pair, neigh, comm, output, modify, other
    ys = [6,5,4,3,2,1]  # tpair, tneigh, tcomm, toutput, tmodify, tother
# You can provide either a single color or an array. To demonstrate this,
# the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    #cs[0] = 'c'
    #ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
    #ax.bar(xs, ys, zs=z, zdir='y') #, color=cs, alpha=0.8)
    ax.bar(xs, ys, zs=z, zdir='y') #, color=cs, alpha=0.8)
    # left	The x coordinates of the left sides of the bars.
    # height	The height of the bars.
    # zs	Z coordinate of bars, if one value is specified they will all be placed at the same z.
    # zdir	Which direction to use as z

#ax.set_xlabel('Lammps section')
ax.set_ylabel('# of steps (*$10^3$)')
ax.set_zlabel('% of total time')

my_xticks = ['Pair','Neigh','Comm','Output','Modify','Other']
my_yticks = ['5','','10','','20','','30','','40']
ax.set_xticklabels(my_xticks, rotation=15)
ax.set_yticklabels(my_yticks)

plt.show()

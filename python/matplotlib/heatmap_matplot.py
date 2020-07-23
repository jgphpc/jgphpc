#!/usr/bin/env python3

# https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
# sphinx_gallery_thumbnail_number = 2


# {{{ plotjg:
#fig, ax = plt.subplots()
#im = ax.imshow(myplt_data)
## plt.show()
#
## Create colorbar
#cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
#cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
#
## We want to show all ticks...
#ax.set_xticks(np.arange(len(columns_labels)))
#ax.set_yticks(np.arange(len(rows_labels)))
## ... and label them with the respective list entries
#ax.set_xticklabels(columns_labels)
#short_rows_labels = [i for i in range(len(rows_labels))]
#ax.set_yticklabels(short_rows_labels)
## ax.set_yticklabels(rows_labels)
#
## Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")
#
## Loop over data dimensions and create text annotations.
#for i in range(len(rows_labels)):
#    for j in range(len(columns_labels)):
#        text = ax.text(j, i, myplt_data[i, j],
#                       ha="center", va="center", color="w")
#
#ax.set_title("Test Validation")
#fig.tight_layout()
## plt.show()
#plt.savefig('heat_matplot_sph.png')
# }}}

# sys.exit(0)

# {{{ old
#old for dim in mydata['mpi+omp'].keys():
#old     # dim = ['large', 'medium', 'small', 'xsmall']
#old     # exe = ['mpi+omp', 'mpi+omp+acc', 'mpi+omp+cuda', 'mpi+omp+target']
#old     for exe in mydata.keys():
#old         print(dim, exe, end=' ')
#old         try:
#old             print(mydata[exe][dim]['pe'], mydata[exe][dim]['tot_neighb'])
#old         except:
#old             print('x -1')
#old     print()
#old 
#old labels = list(mydata['mpi+omp'].keys())
#old # ['large', 'medium', 'small', 'xsmall']
#old exes = list(mydata.keys())
#old # ['mpi+omp', 'mpi+omp+acc', 'mpi+omp+cuda', 'mpi+omp+target']
#old tot_ngb = []
#old # mydata['mpi+omp']['large']['tot_neighb'],
#old # mydata['mpi+omp']['medium']['tot_neighb'],
#old # mydata['mpi+omp']['small']['tot_neighb'],
#old for exe in exes:
#old # for dim in labels:
#old     # print(dim)
#old     tmp = []
#old     for dim in labels:
#old         try:
#old             # print(mydata[exe][dim]['pe'], mydata[exe][dim]['tot_neighb'])            
#old             tmp.append(mydata[exe][dim]['tot_neighb'])
#old         except:
#old             # print('x -1')
#old             tmp.append(-1)
#old     tot_ngb.append(tmp)
#old     print(tot_ngb)
#old exe0 = tot_ngb[0]
#old exe1 = tot_ngb[1]
#old exe2 = tot_ngb[2]
#old exe3 = tot_ngb[3]
#old for i in range(len(tot_ngb)):
#old     print(i, tot_ngb[i], min(tot_ngb[i]), max(tot_ngb[i]), max(tot_ngb[i])-min(tot_ngb[i]))
# }}}

# {{{ plot
#vegetables = ["cucumber", "tomato", "lettuce"]
#farmers = ["Farmer Joe", "Upland Bros."]
#harvest = np.array([[0.8, 2.4],
#                    [2.4, 0.0],
#                    [1.1, 2.4],])

#vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
#              "potato", "wheat", "barley"]
#farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
# harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
#                     [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
#                     [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
#                     [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
#                     [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
#                     [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
#                     [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

##  fig, ax = plt.subplots()
##  im = ax.imshow(harvest)
##  
##  # We want to show all ticks...
##  ax.set_xticks(np.arange(len(farmers)))
##  ax.set_yticks(np.arange(len(vegetables)))
##  # ... and label them with the respective list entries
##  ax.set_xticklabels(farmers)
##  ax.set_yticklabels(vegetables)
##  
##  # Rotate the tick labels and set their alignment.
##  plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
##           rotation_mode="anchor")
##  
##  # Loop over data dimensions and create text annotations.
##  for i in range(len(vegetables)):
##      for j in range(len(farmers)):
##          text = ax.text(j, i, harvest[i, j],
##                         ha="center", va="center", color="w")
##  
##  ax.set_title("Harvest of local farmers (in tons/year)")
##  fig.tight_layout()
##  # plt.show()
##  plt.savefig('heat_matplot.png')
# }}}

# {{{ def heatmap
def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar
# }}}


# {{{ def annotate_heatmap
def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
# }}}

# {{{ main:
# read data into mydata dict:
mydata = {}
in1='/private/tmp/JG/PYTHON/0.in'
exec(open(in1).read())

columns_labels = ['Total Neighbors', 'Avg neighbor per particle',
                  'Total energy', 'Internal energy']
rows_labels = []
row = {}
for dim in ['xsmall']:
    for exe in ['mpi+omp', 'mpi+omp+target', 'mpi+omp+acc', 'mpi+omp+cuda']:
        for pe in ['PrgEnv-cray', 'PrgEnv-gnu', 'PrgEnv-intel', 'PrgEnv-pgi']:
            label = f'{dim}_{exe}_{pe}'
            try:
                row[label] = mydata[exe][dim][pe]
            except:
                row[label] = [-1, -1, -1, -1]

print(columns_labels)
rows_labels = list(row.keys())
short_rows_labels = [i for i in range(len(rows_labels))]
#ax.set_yticklabels(short_rows_labels)
print(rows_labels)
list_of_lists = [row[k] for k in row.keys()]
# harvest = np.array(list_of_lists)
myplt_data = np.array(list_of_lists)
print('myplt_data=', myplt_data)

fig, ax = plt.subplots()
# im, cbar = heatmap(myplt_data, short_rows_labels, columns_labels, ax=ax,
im, cbar = heatmap(myplt_data, rows_labels, columns_labels, ax=ax,
                   cmap="YlGn", cbarlabel="Metrics [count|erg]")
# texts = annotate_heatmap(im, valfmt="{x:.1f}")
fig.tight_layout()
# plt.show()
plt.savefig('heatmap_matplot_sqpatch.png')
# }}}

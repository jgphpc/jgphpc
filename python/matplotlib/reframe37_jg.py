#!/usr/bin/env python3
# coding: utf-8


import json
import numpy as np
import matplotlib.pyplot as plt
# import sys
# import re
from decimal import Decimal


def May2021_read_reframe_json_and_return_dict():
    # --- read data from reframe json report
    f = open('run-report_cuda.json')
    d = json.load(f)
    f.close()

    # --- construct dict for plotly:
    #     my_data['cn:np_per_c:func_name': func_seconds]
    my_data = {}
    for myjob in d['runs'][0]['testcases']:
        if myjob['result'] == 'success':
            job_stdout = myjob['job_stdout']
            for myfunc in range(0, 14):
                # 0 Elapsed              # 1 _Elapsed
                # 2 domain_sync          # 8 IAD
                # 3 updateTasks          # 9 MomentumEnergyIAD
                # 4 FindNeighbors        # 10 Timestep
                # 5 Density              # 11 UpdateQuantities
                # 6 EquationOfState      # 12 EnergyConservation
                # 7 mpi_synchronizeHalos # 13 UpdateSmoothingLength
                cn = job_stdout.split('_')[5]
                np_per_c = f"{Decimal(job_stdout.split('_')[6]):.1E}"
                func_name = myjob['perfvars'][myfunc]['name']
                my_key = f'{cn}:{np_per_c}:{func_name}'
                func_seconds = myjob['perfvars'][myfunc]['value']
                # print(my_key, func_seconds)
                my_data[my_key] = func_seconds

    return my_data


def May2021_create_xdata_for_plot(my_data):
    # get dict and format it for plotly x_data
    # https://plotly.com/python/horizontal-bar-charts/
    # -> Color Palette for Bar Chart
    my_func_idx = 0
    mylist = []
    x_data = []
    for kk in my_data.keys():
        cn = kk.split(':')[0]
        # np_per_c = kk.split(':')[1]
        # func_name = kk.split(':')[2]
        # 2:1.0E+6:UpdateSmoothingLength 0.2407
        if my_func_idx > 1 and cn == '1':
            mylist.append(my_data[kk])
        my_func_idx += 1
        if my_func_idx == 14:
            my_func_idx = 0
            x_data.append(mylist)
            mylist = []

    return x_data


def list2percentages(ll):
    # convert each element of the list to its % value
    # res_l = []
    # total = sum(ll)
    # print(ll)
    # for seconds in ll:
    #     print(seconds)
    #     ll[0] = round(seconds / total, 5)

    ll = np.true_divide(ll, sum(ll))
    # ll = np.true_divide(ll, ll.sum(axis=1, keepdims=True))
    return ll * 100


def May2021_plot_mydata_as_pctg_hbar(my_data):
    """
    copied from:
     https://matplotlib.org/stable/gallery/lines_bars_and_markers/
     horizontal_barchart_distribution.html
     #sphx-glr-gallery-lines-bars-and-markers-horizontal-barchart-distribution-py
    """

    category_names = ['domain_sync', 'updateTasks', 'FindNeighbors', 'Density',
                      'EquationOfState', 'mpi_synchronizeHalos', 'IAD',
                      'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities',
                      'EnergyConservation', 'UpdateSmoothingLength']

    results = {
        '$10^4$': my_data[0],
        '$10^5$': my_data[1],
        '$10^6$': my_data[2],
    }
    #  2 domain_sync
    #  3 updateTasks
    #  4 FindNeighbors
    #  5 Density
    #  6 EquationOfState
    #  7 mpi_synchronizeHalos
    #  8 IAD
    #  9 MomentumEnergyIAD
    # 10 Timestep
    # 11 UpdateQuantities
    # 12 EnergyConservation
    # 13 UpdateSmoothingLength

    def survey(results, category_names):
        """
        Parameters
        ----------
        results : dict
            A mapping from question labels to a list of answers per category.
            It is assumed all lists contain the same number of entries and that
            it matches the length of *category_names*.
        category_names : list of str
            The category labels.
        """
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names,
                                                 category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            rects = ax.barh(labels, widths, left=starts, height=0.5,
                            label=colname, color=color)
            r, g, b, _ = color
            # text_color = 'black'
            # {{{ jg ax.text -------------------------------------------------
            if min(widths) > 2:
                # fmtjg = f'{int(bar_label)}:%}'
                ax.bar_label(rects, label_type='center', color='black',
                             fmt='%d%%')
                # --- adding func_name to bar_label
                for rr in rects:
                    # print(rr, type(rr))
                    # Rectangle(xy=(0, -0.25), width=5.6, height=0.5, angle=0)
                    # Rectangle(xy=(0, 0.75), width=17.9, height=0.5, angle=0)
                    # ax.text(0+(10/2)-(1*10/2), -.25+0.5, category_names[0],
                    # ------> x
                    # | x0,y0   x1,y0  ...
                    # | x0,y1   x1,y1  ...
                    # | x0,y2   x1,y2  ...
                    # y
                    x_text = rr.xy[0]  # + rr.width / 4
                    y_text = rr.xy[1] + rr._height
                    ax.text(x_text, y_text, colname, rotation=-45)
                    # fontsize=8)

    #        text_color = '' if min(widths) < 2 else 'black'
    #        # text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
    #        ax.bar_label(rects, label_type='center', color=text_color)
            # }}} ------------------------------------------------------------
        # ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
        ax.legend(ncol=4, bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        return fig, ax

    survey(results, category_names)
    plt.show()


# ----------------------------------------------------------------------------
# elapsed timings (seconds, %) for each sph function call as a bar plot
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/
# horizontal_barchart_distribution.html
if __name__ == "__main__":
    my_data = May2021_read_reframe_json_and_return_dict()
    x_data = May2021_create_xdata_for_plot(my_data)
    print(x_data)

    # --- convert seconds (x_data) to % (x_data_percents):
    # --- not needed? (matplotlib does it)
    x_data_percents = []
    for ii in x_data:
        if ii:
            x_data_percents.append(np.round(list2percentages(ii), 1).tolist())
            # x_data_percents = list2percentages(ii)
            # print("#", np.round(x_data_percents, 2).tolist())

    print(x_data_percents)
    May2021_plot_mydata_as_pctg_hbar(x_data_percents)
    # for i in newl: print(i)
    # for i in x_data[2]: print(i)

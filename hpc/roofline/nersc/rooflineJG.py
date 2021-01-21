#!/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

font = {"size": 15}
plt.rc("font", **font)
colors = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
]
styles = [
    "o",
    "s",
    "v",
    "^",
    "D",
    ">",
    "<",
    "*",
    "h",
    "H",
    "+",
    "1",
    "2",
    "3",
    "4",
    "8",
    "p",
    "d",
    "|",
    "_",
    ".",
    ", ",
    "x",
]
markersize = 10
markerwidth = 2
maxchar = 25


def roofline(filename, FLOPS, AIHBM, AIL2=None, AIL1=None, LABELS=None,
        flag="HBM", peak_HBM = 828.0, peak_DP = 7.8):
    # memRoofs = [("L1", 54000.0), ("L2", 2996.77), ("HBM", 828.76)]
    # cmpRoofs = [("Tensor", 96.9), ("DP", 7.8)]
    if not FLOPS:
        print("FLOPS can not be empty!")
        return
    if max(FLOPS) == 0:
        print("FLOPS are all 0s!")
        return
    if (not AIHBM) and (not AIL2) and (not AIL1):
        print("AIHBM, AIL2 and AIL1 can not all be empty!")
        return
    if (
        (len(FLOPS) != len(AIHBM))
        or (len(FLOPS) != len(AIL2))
        or (len(FLOPS) != len(AIL1))
    ):
        print("FLOPS needs to have the same length as AI!")
        return
    if (flag != "HBM") and (flag != "L2") and (flag != "L1") and (flag != "all"):
        print("flag needs to be one of HBM, L2, L1, and all!")
        return
    LABELS = [x[:maxchar] for x in LABELS]

# sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_sustained	inst/cycle
# * sm__cycles_elapsed.avg.per_second	cycle/nsecond
# Peak SP FLOP/sec = inst/cycle  * cycle/nsecond  = inst/nanosecond
# 2*sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_sustained*sm__cycles_elapsed.avg.per_second
# ---
# sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained	inst/cycle
# * sm__cycles_elapsed.avg.per_second	cycle/nsecond
# Peak DP FLOP/sec = inst/cycle  * cycle/nsecond  = inst/nanosecond
# 2*sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained*sm__cycles_elapsed.avg.per_second
# ---
# tensor ?
# ---
# device__attribute_display_name	Tesla	V100-SXM2-32GB
# ---
# dram__bytes.sum.peak_sustained	Kbyte/cycle	1.02
# * dram__cycles_elapsed.avg.per_second	cycle/usecond	877.5
# = Kbyte/cycle * cycle/usecond = 895.05	Gbytes/sec

    memRoofs = [("L1", 54000.0), ("L2", 2996.77), ("HBM", peak_HBM)]
    cmpRoofs = [("Tensor", 96.9), ("DP", peak_DP)]
    # memRoofs = [("L1", 54000.0), ("L2", 2996.77), ("HBM", 828.76)]
    # cmpRoofs = [("Tensor", 96.9), ("DP", 7.8)]

    fig = plt.figure(1, figsize=(10.67, 6.6))
    plt.clf()
    ax = fig.gca()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Arithmetic Intensity [FLOPs/Byte]")
    ax.set_ylabel("Performance [GFLOP/sec]")
    nx = 10000
    xmin = -3
    # NAMD: xmax = 6
    # QE:
    xmax = 6
    # xmax = 3
    ymin = 1
    ymax = 200000
    ax.set_xlim(10 ** xmin, 10 ** xmax)
    ax.set_ylim(ymin, ymax)
    ixx = int(nx * 0.02)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    scomp_x_elbow = []
    scomp_ix_elbow = []
    smem_x_elbow = []
    smem_ix_elbow = []
    x = np.logspace(xmin, xmax, nx)
    for roof in cmpRoofs:
        for ix in range(1, nx):
            if (
                float(memRoofs[0][1] * x[ix]) >= roof[1] * 1024 and
                (memRoofs[0][1] * x[ix - 1]) < roof[1] * 1024
            ):
                scomp_x_elbow.append(x[ix - 1])
                scomp_ix_elbow.append(ix - 1)
                break

    for roof in memRoofs:
        for ix in range(1, nx):
            if (
                cmpRoofs[0][1] * 1024 <= roof[1] * x[ix] and
                cmpRoofs[0][1] * 1024 > roof[1] * x[ix - 1]
            ):
                smem_x_elbow.append(x[ix - 1])
                smem_ix_elbow.append(ix - 1)
                break

    for i in range(len(cmpRoofs)):
        roof = cmpRoofs[i][1] * 1024
        y = np.ones(len(x)) * roof
        ax.plot(x[scomp_ix_elbow[i] :], y[scomp_ix_elbow[i] :], c="k", ls="-", lw="2")

    for i in range(len(memRoofs)):
        roof = memRoofs[i][1]
        y = x * roof
        ax.plot(
            x[: smem_ix_elbow[i] + 1], y[: smem_ix_elbow[i] + 1], c="k", ls="-", lw="2"
        )

    for i in range(len(AIHBM)):
        if flag == "L1":
            ax.plot(
                float(AIL1[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[0],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )
        elif flag == "L2":
            ax.plot(
                float(AIL2[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[1],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )
        elif flag == "HBM":
            ax.plot(
                float(AIHBM[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[22],
                # marker=styles[2],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )
        elif flag == "all":
            ax.plot(
                float(AIL1[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[0],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )
            ax.plot(
                float(AIL2[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[1],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )
            ax.plot(
                float(AIHBM[i]),
                float(FLOPS[i]),
                c=colors[i % 10],
                marker=styles[2],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=LABELS[i] if LABELS else "unknown",
            )

    marker_handles = []
    if flag == "L1":
        marker_handles.append(
            ax.plot(
                [],
                [],
                c="k",
                marker=styles[0],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=memRoofs[0][0],
            )[0]
        )
    elif flag == "L2":
        marker_handles.append(
            ax.plot(
                [],
                [],
                c="k",
                marker=styles[1],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=memRoofs[1][0],
            )[0]
        )
    elif flag == "HBM":
        marker_handles.append(
            ax.plot(
                [],
                [],
                c="k",
                marker=styles[2],
                linestyle="None",
                ms=markersize,
                markerfacecolor="none",
                markeredgewidth=markerwidth,
                label=memRoofs[2][0],
            )[0]
        )
    elif flag == "all":
        for i in range(len(memRoofs)):
            marker_handles.append(
                ax.plot(
                    [],
                    [],
                    c="k",
                    marker=styles[i],
                    linestyle="None",
                    ms=markersize,
                    markerfacecolor="none",
                    markeredgewidth=markerwidth,
                    label=memRoofs[i][0],
                )[0]
            )

    for roof in cmpRoofs:
        ax.text(
            x[-ixx],
            roof[1] * 1024,
            roof[0] + ": " + "{0:.1f}".format(roof[1]) + " TFLOP/s",
            horizontalalignment="right",
            verticalalignment="bottom",
        )

    for roof in memRoofs:
        ang = np.arctan(
            np.log10(xlim[1] / xlim[0])
            / np.log10(ylim[1] / ylim[0])
            * fig.get_size_inches()[1]
            / fig.get_size_inches()[0]
        )
        if x[ixx] * roof[1] > ymin:
            ax.text(
                x[ixx],
                x[ixx] * roof[1] * (1 + 0.25 * np.sin(ang) ** 2),
                roof[0] + ": " + "{0:.1f}".format(float(roof[1])) + " GB/s",
                horizontalalignment="left",
                verticalalignment="bottom",
                rotation=180 / np.pi * ang,
            )
        else:
            ymin_ix_elbow = list()
            ymin_x_elbow = list()
            for ix in range(1, nx):
                if ymin <= roof[1] * x[ix] and ymin > roof[1] * x[ix - 1]:
                    ymin_x_elbow.append(x[ix - 1])
                    ymin_ix_elbow.append(ix - 1)
                    break
            ax.text(
                x[ixx + ymin_ix_elbow[0]],
                x[ixx + ymin_ix_elbow[0]] * roof[1] * (1 + 0.25 * np.sin(ang) ** 2),
                roof[0] + ": " + "{0:.1f}".format(float(roof[1])) + " GB/s",
                horizontalalignment="left",
                verticalalignment="bottom",
                rotation=180 / np.pi * ang,
            )

    # print(f'handles={marker_handles}')  # matplotlib.lines.Line2D
    leg1 = plt.legend(
        handles=marker_handles,
        loc="lower right",
        ncol=len(flag[0]) if "all" not in flag else 3,
        bbox_to_anchor=(1, 0),
    )
    ax.add_artist(leg1)
    patch_handles = list()
    for i in range(0, len(AIHBM)):
        if FLOPS[i] > 0:
            patch_handles.append(
                mpatches.Patch(
                    color=colors[i % 10], label=LABELS[i] if LABELS else "unknown"
                )
            )

    leg2 = plt.legend(
        handles=patch_handles, loc=4, ncol=1, bbox_to_anchor=(1, 0.1), scatterpoints=1
    )
    ax.text(
        xlim[0] * 1.1,
        ylim[1] / 1.1,
        "-".join([filename, flag]),
        horizontalalignment="left",
        verticalalignment="top",
    )
    ax.grid(True)
    # plt.title('-'.join([filename,flag]))
    plt.legend(bbox_to_anchor=(1,1), loc="upper left")  # on the right side
    plt.savefig("_".join([filename, flag]) + ".png", bbox_inches='tight')
    # plt.savefig('_'.join([filename,flag])+'.eps')
    # plt.show()

# if __name__ == "__main__":
#     tag = 'V100_KernelA'
#     FLOPS = [3315.528408831178, 3315.272547975705, 3315.465711192385, 3315.356360410653, 3315.307971170475, 3315.2866271370253, 3315.2945186014863, 3315.4486409586298, 3315.415089558547, 3314.6110609602265]
#     AI_HBM = [624.7476452687752, 613.9439869642424, 624.2895201176688, 465.9266986281462, 624.2806141360542, 625.1476636632309, 623.9845778311686, 624.5607794616116, 625.5851879022089, 624.5106526026543]
#     AI_L2 = [622.3443248822133, 612.131636038963, 623.0247559860268, 461.670109655668, 621.3452731947159, 622.7472543779011, 622.9935228142175, 622.9987533940958, 622.0107493662354, 621.4681310656867]
#     AI_L1 = [625.0, 625.0, 625.0, 625.0, 625.0, 625.0, 625.0, 625.0, 625.0, 625.0]
#     LABELS = ['kernA_0', 'kernA_1', 'kernA_2', 'kernA_3', 'kernA_4', 'kernA_5', 'kernA_6', 'kernA_7', 'kernA_8', 'kernA_9']
#     flag = 'HBM'
#     peak_HBM = 898.831296512
#     peak_DP = 6.63326208
#     roofline(tag, FLOPS, AI_HBM, AI_L2, AI_L1, LABELS, flag, peak_HBM, peak_DP)

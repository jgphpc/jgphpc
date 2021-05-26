#!/usr/bin/env python3

# From:
#  https://gitlab.com/NERSC/roofline-on-nvidia-gpus/-/blob/master/
#  custom-scripts/roofline.py
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

font = {"size": 15}
plt.rc("font", **font)
# {{{
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
# }}}
markersize = 10
markerwidth = 2
maxchar = 25


# {{{ read_csv_data
def read_csv_data(filename):
    files = [filename]
    for file in files:
        # print(file)
        tag, ext = os.path.splitext(os.path.basename(file))
        # tag='output', ext='.csv'
        # dfs[tag] = pd.DataFrame()
        with open(file, 'r') as f:
            cnt = 0
            while True:
                ln = f.readline()
                if not ln:
                    break
                cnt += 1
                if 'Host Name' in ln:
                    break
            df = pd.read_csv(file, skiprows=cnt-1)
            # dft = df.groupby(['Kernel Name', 'Metric Name']).sum()
            f.close()

    return df
# }}}


# {{{ get_roofline_kernel_name
def get_roofline_kernel_name(df):
    # 'density'
    return df['Kernel Name'][1].split("<")[0].split("::")[-1]
# }}}


# {{{ get_roofline_gpu_name
def get_roofline_gpu_name(df):
    # 'A100-PCIE-40GB'
    return df['device__attribute_display_name'][1]
# }}}


# {{{ get_roofline_executable_name
def get_roofline_executable_name(df):
    # 'mpi+omp+cuda'
    return df['Process Name'][1]
# }}}


# {{{ get_roofline_peaks
def get_roofline_peaks(df):
    # Double Precision Roofline
    PeakWork = []
    PeakTraffic = []
    # arithmetic_intensity = []
    for ii in range(1, len(df['ID'])):
        # Double Precision Roofline
        # DP PeakWork:
        mm = 'sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained'
        inst_per_cycle = float(df[mm][ii])
        res = 2 * inst_per_cycle
        # derived__sm__sass_thread_inst_executed_op_dfma_pred_on_x2.append(res)
        mm = 'sm__cycles_elapsed.avg.per_second'
        cycle_per_usecond = float(df[mm][ii])
        PeakWork.append(res * cycle_per_usecond)
        # PeakTraffic:
        mm = 'dram__bytes.sum.peak_sustained'
        kbyte_per_cycle = float(df[mm][ii])
        mm = 'dram__cycles_elapsed.avg.per_second'
        cycle_per_nsecond = float(df[mm][ii])
        PeakTraffic.append(kbyte_per_cycle * cycle_per_nsecond)

    return (float(np.min(PeakTraffic)), float(np.min(PeakWork) / 1e6))
#del
#del        # DP AchievedWork:
#del        mm_ = 'smsp__sass_thread_inst_executed_op_'
#del        mm = f'{mm_}dadd_pred_on.sum.per_cycle_elapsed'
#del        inst_per_cycle_dadd = float(df[mm][ii])
#del        mm = f'{mm_}dmul_pred_on.sum.per_cycle_elapsed'
#del        inst_per_cycle_dmul = float(df[mm][ii])
#del        mm = f'{mm_}dfma_pred_on.sum.per_cycle_elapsed'
#del        inst_per_cycle_dfma = 2 * float(df[mm][ii])
#del        # = derived__smsp__sass_thread_inst_executed_op_dfma_pred_on_x2
#del        # cycle_per_usecond = see above
#del        AchievedWork.append(
#del            (inst_per_cycle_dadd + inst_per_cycle_dmul + inst_per_cycle_dfma) *
#del            cycle_per_usecond
#del        )

#    peak_gflops = np.min(PeakWork) / 1e3  # 5 286 017.097216 =  MFLOP/s
#    peak_bw = np.min(PeakTraffic)   # 1.55469056 = TERA
#    kernel_gflops = np.divide(AchievedWork, 1e3)  # 104871.54267 = 104 GFLOP/s
#    # kernel_ai # 8.746599
#    arithmetic_intensity = list(np.divide(AchievedWork, AchievedTraffic_dram)
#                                / 1e3)
#    print(f'peak_tflops: {peak_mflops / 1e6}, peak_bw: {peak_bw} ')
#    print(f'kernel_gflops: {kernel_gflops}')
#    print(f'AchievedTraffic_dram: {AchievedTraffic_dram}')
#    print(f'arithmetic_intensity: {arithmetic_intensity}')
    # NOTE:
    # https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html
    # #metrics-structure
    # Counters using the term cycles in the name report the number of cycles in
    # the unit's clock domain. Unit-level cycle metrics include:
    #  - unit__cycles_elapsed : the number of cycles within a range,
    #    the cycles' DimUnits are specific to the unit's clock domain.
    #  - .sum: the sum of counter values across all unit instances.
    #  - .avg: the average counter value across all unit instances.
    #  - .per_second: the number of operations per user-specified frame cycle
# }}}


 # {{{ get_roofline_peak_perf
def get_roofline_peak_perf(df):
    # Double Precision Roofline
    PeakWork = []
    # arithmetic_intensity = []
    for ii in range(1, len(df['ID'])):
        # Double Precision Roofline
        # DP PeakWork:
        mm = 'sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained'
        inst_per_cycle = float(df[mm][ii])
        res = 2 * inst_per_cycle
        # derived__sm__sass_thread_inst_executed_op_dfma_pred_on_x2.append(res)
        mm = 'sm__cycles_elapsed.avg.per_second'
        cycle_per_usecond = float(df[mm][ii])
        PeakWork.append(res * cycle_per_usecond)

    return float(np.min(PeakWork) / 1e6)
# }}}


# {{{ get_roofline_peak_bw
def get_roofline_peak_bw(df):
    # Double Precision Roofline
    PeakTraffic = []
    # arithmetic_intensity = []
    for ii in range(1, len(df['ID'])):
        # Double Precision Roofline
        # PeakTraffic:
        mm = 'dram__bytes.sum.peak_sustained'
        kbyte_per_cycle = float(df[mm][ii])
        mm = 'dram__cycles_elapsed.avg.per_second'
        cycle_per_nsecond = float(df[mm][ii])
        PeakTraffic.append(kbyte_per_cycle * cycle_per_nsecond)

    return float(np.min(PeakTraffic) * 1e3)
# }}}


# {{{ get_roofline_kernel_flops
def get_roofline_kernel_flops(df):
    # Double Precision Roofline
    AchievedWork = []
    for ii in range(1, len(df['ID'])):
        # DP AchievedWork:
        mm_ = 'smsp__sass_thread_inst_executed_op_'
        mm = f'{mm_}dadd_pred_on.sum.per_cycle_elapsed'
        inst_per_cycle_dadd = float(df[mm][ii])
        mm = f'{mm_}dmul_pred_on.sum.per_cycle_elapsed'
        inst_per_cycle_dmul = float(df[mm][ii])
        mm = f'{mm_}dfma_pred_on.sum.per_cycle_elapsed'
        inst_per_cycle_dfma = 2 * float(df[mm][ii])
        # = derived__smsp__sass_thread_inst_executed_op_dfma_pred_on_x2
        mm = 'sm__cycles_elapsed.avg.per_second'
        cycle_per_usecond = float(df[mm][ii])
        AchievedWork.append(
            (inst_per_cycle_dadd + inst_per_cycle_dmul + inst_per_cycle_dfma) *
            cycle_per_usecond
        )

    return AchievedWork
# }}}


# {{{ get_roofline_kernel_arithmetic_intensity
def get_roofline_kernel_arithmetic_intensity(df, inAchievedWork):
    # Double Precision Roofline
    AchievedTraffic_dram = []
    for ii in range(1, len(df['ID'])):
        # AchievedTraffic:
        gbyte_per_second_dram = float(df['dram__bytes.sum.per_second'][ii])
        AchievedTraffic_dram.append(gbyte_per_second_dram)

    arithmetic_intensity = list(np.divide(inAchievedWork, AchievedTraffic_dram)
                                / 1e3)

    return arithmetic_intensity
# }}}


# plot here:
# {{{ roofline_ncu
def roofline_ncu(filename, FLOPS, AIHBM, AIL2=None, AIL1=None, LABELS=None,
                 flag="HBM", peak_HBM=828.0, peak_DP=7.8, my_title=''):
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
    ):
        print("FLOPS needs to have the same length as AI!")
        print(f'len(FLOPS): {len(FLOPS)} len(AIHBM): {len(AIHBM)}')
        return
    if (flag != "HBM") and (flag != "L2") and (flag != "L1") and \
       (flag != "all"):
        print("flag needs to be one of HBM, L2, L1, and all!")
        return
    LABELS = [x[:maxchar] for x in LABELS]

# {{{
# from roofline-on-nvidia-gpus.git/README.md (charlene because NVIDIA did not share)
# and ~/jgphpc.git/hpc/roofline/nersc/jg.ods
# ------------------------------------------
# sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_sustained	inst/cycle
# * sm__cycles_elapsed.avg.per_second	cycle/nsecond
# Peak SP FLOP/sec = inst/cycle  * cycle/nsecond  = inst/nanosecond
# 2 *sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_sustained *sm__cycles_elapsed.avg.per_second
# ---
# sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained	inst/cycle
# * sm__cycles_elapsed.avg.per_second	cycle/nsecond
# Peak DP FLOP/sec = inst/cycle  * cycle/nsecond  = inst/nanosecond
# 2 *sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained *sm__cycles_elapsed.avg.per_second
# ---
# tensor ?
# ---
# device__attribute_display_name	Tesla	V100-SXM2-32GB
# ---
# dram__bytes.sum.peak_sustained	Kbyte/cycle	1.02
# * dram__cycles_elapsed.avg.per_second	cycle/usecond	877.5
# = Kbyte/cycle * cycle/usecond = 895.05	Gbytes/sec
# ------------------------------------------
# from roofline-on-nvidia-gpus.git/README.md (charlene because NVIDIA did not share)
#   - `Time`:
#     + sm__cycles_elapsed.avg / sm__cycles_elapsed.avg.per_second
#   - `FLOPs`:
#     + `DP`: sm__sass_thread_inst_executed_op_dadd_pred_on.sum + 2 x sm__sass_thread_inst_executed_op_dfma_pred_on.sum + sm__sass_thread_inst_executed_op_dmul_pred_on.sum
#     + `SP`: sm__sass_thread_inst_executed_op_fadd_pred_on.sum + 2 x sm__sass_thread_inst_executed_op_ffma_pred_on.sum + sm__sass_thread_inst_executed_op_fmul_pred_on.sum
#     + `HP`: sm__sass_thread_inst_executed_op_hadd_pred_on.sum + 2 x sm__sass_thread_inst_executed_op_hfma_pred_on.sum + sm__sass_thread_inst_executed_op_hmul_pred_on.sum
#     + `Tensor Core`: 512 x sm__inst_executed_pipe_tensor.sum
#   - `Bytes`:
#     + `DRAM`: dram__bytes.sum
#     + `L2`: lts__t_bytes.sum
#     + `L1`: l1tex__t_bytes.sum
# ------------------------------------------
# > grep op_dfma_pred_on eff.csv
# "derived__sm__sass_thread_inst_executed_op_dfma_pred_on_x2"
# "derived__smsp__sass_thread_inst_executed_op_dfma_pred_on_x2"
# "sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained"
# "smsp__sass_thread_inst_executed_op_dfma_pred_on.sum.per_cycle_elapsed"
# }}}

    memRoofs = [("HBM", peak_HBM)]
    cmpRoofs = [("DP", peak_DP)]
    # memRoofs = [("L1", 54000.0), ("L2", 2996.77), ("HBM", peak_HBM)]
    # cmpRoofs = [("Tensor", 96.9), ("DP", peak_DP)]
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
    # QE: xmax = 6
    xmax = 2
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
        ax.plot(x[scomp_ix_elbow[i]:], y[scomp_ix_elbow[i]:], c="k", ls="-",
                lw="2")

    for i in range(len(memRoofs)):
        roof = memRoofs[i][1]
        y = x * roof
        ax.plot(
            x[:smem_ix_elbow[i] + 1], y[:smem_ix_elbow[i] + 1], c="k", ls="-",
            lw="2"
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
                label=memRoofs[0][0],
                # label=memRoofs[2][0],
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
                x[ixx + ymin_ix_elbow[0]] * roof[1] *
                (1 + 0.25 * np.sin(ang) ** 2),
                roof[0] + ": " + "{0:.1f}".format(float(roof[1])) + " GB/s",
                horizontalalignment="left",
                verticalalignment="bottom",
                rotation=180 / np.pi * ang,
            )

    # print(f'handles={marker_handles}')  # matplotlib.lines.Line2D
    # removing "HBM" from plot:
    # leg1 = plt.legend(
    #     handles=marker_handles,
    #     loc="lower right",
    #     ncol=len(flag[0]) if "all" not in flag else 3,
    #     bbox_to_anchor=(1, 0),
    # )
    # ax.add_artist(leg1)
    patch_handles = list()
    for i in range(0, len(AIHBM)):
        if FLOPS[i] > 0:
            patch_handles.append(
                mpatches.Patch(
                    color=colors[i % 10],
                    label=LABELS[i] if LABELS else "unknown"
                )
            )

    leg2 = plt.legend(
        handles=patch_handles, loc=4, ncol=1, bbox_to_anchor=(1, 0.1),
        scatterpoints=1
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
    ax.set_title(my_title, fontsize=10)

# The ratio of peak float (fp32) to double (fp64) performance on this device is
# 2:1. The kernel achieved  close to 0% of this device's fp32 peak performance
# and 2% of its fp64 peak performance.

    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")  # on the right side
    plt.savefig("_".join([filename, flag]) + ".png", bbox_inches='tight')
    # plt.savefig('_'.join([filename,flag])+'.eps')
    # plt.show()
# }}}


# {{{ roofline_utilization_message
def roofline_utilization_message():
    x = 0
    # from: nvidia-nsight-compute -> sections/SpeedOfLight_Roofline.py
#     peak_fp32 = 2 * action.metric_by_name("sm__sass_thread_inst_executed_op_ffma_pred_on.sum.peak_sustained").as_double()
#     peak_fp64 = 2 * action.metric_by_name("sm__sass_thread_inst_executed_op_dfma_pred_on.sum.peak_sustained").as_double()
#     achieved_fp32 = 0.0
#     achieved_fp32 += action.metric_by_name("smsp__sass_thread_inst_executed_op_fadd_pred_on.sum.per_cycle_elapsed").as_double()
#     achieved_fp32 += action.metric_by_name("smsp__sass_thread_inst_executed_op_fmul_pred_on.sum.per_cycle_elapsed").as_double()
#     achieved_fp32 += 2 * action.metric_by_name("smsp__sass_thread_inst_executed_op_ffma_pred_on.sum.per_cycle_elapsed").as_double()
#     achieved_fp64 = 0.0
#     achieved_fp64 += action.metric_by_name("smsp__sass_thread_inst_executed_op_dadd_pred_on.sum.per_cycle_elapsed").as_double()
#     achieved_fp64 += action.metric_by_name("smsp__sass_thread_inst_executed_op_dmul_pred_on.sum.per_cycle_elapsed").as_double()
#     achieved_fp64 += 2 * action.metric_by_name("smsp__sass_thread_inst_executed_op_dfma_pred_on.sum.per_cycle_elapsed").as_double()
#     ratio = peak_fp32 / peak_fp64
#     message = "The ratio of peak float (fp32) to double (fp64) performance on this device is {:.0f}:1.".format(ratio)
# 
#     high_utilization_threshold = 0.60
#     low_utilization_threshold = 0.15
# 
#     achieved_fp64_pct = achieved_fp64 / peak_fp64
#     fp64_prefix = "" if achieved_fp64_pct >= 0.01 or achieved_fp64_pct == 0.0 else " close to "
#     achieved_fp32_pct = achieved_fp32 / peak_fp32
#     fp32_prefix = "" if achieved_fp32_pct >= 0.01 or achieved_fp32_pct == 0.0 else " close to "
# 
#     message += " The kernel achieved {}{:.0f}% of this device's fp32 peak performance and {}{:.0f}% of its fp64 peak performance.".format(fp32_prefix, 100.0 * achieved_fp32_pct, fp64_prefix, 100.0 * achieved_fp64_pct)
# 
#     if achieved_fp32_pct < high_utilization_threshold and achieved_fp64_pct > low_utilization_threshold:
#         msg_type = NvRules.IFrontend.MsgType_MSG_WARNING
#         message += " If @section:ComputeWorkloadAnalysis:Compute Workload Analysis@ determines that this kernel is fp64 bound, consider using 32-bit precision floating point operations to improve its performance."
#     elif achieved_fp64_pct > high_utilization_threshold and achieved_fp32_pct > high_utilization_threshold:
#         msg_type = NvRules.IFrontend.MsgType_MSG_WARNING
#         message += " If @section:SpeedOfLight:Speed Of Light@ analysis determines that this kernel is compute bound, consider using integer arithmetic instead where applicable."
# }}}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # takes 1 filename as arg:
        sys.stderr.write("Usage: {} <csvfile>\n".format(sys.argv[0]))
        sys.exit(1)
    else:
        filename = sys.argv[1]

    df = read_csv_data(filename)
    # peak_HBM = 1554.69056  # peak_bw * 1e3
    # peak_DP = 5.2860170972159995    # peak_gflops / 1e3
    # peak_HBM, peak_DP = get_roofline_peaks(df)
    peak_HBM = get_roofline_peak_bw(df)
    peak_DP = get_roofline_peak_perf(df)
    #
    FLOPS = get_roofline_kernel_flops(df)
    kernel_gflops = list(np.divide(FLOPS, 1e3))  # 104871.54267 = 104 GFLOP/s
    AI_DRAM = get_roofline_kernel_arithmetic_intensity(df, FLOPS)
    tag = get_roofline_gpu_name(df)  # 'A100-PCIE-40GB'
    # print(len(FLOPS))
    # print(len(AI_DRAM))
    # AI_L2 = None
    # AI_L1 = None
    executable_name = get_roofline_executable_name(df)  # mpi+omp+cuda
    kernel_name = get_roofline_kernel_name(df)  # density
    LABELS = [f'{kernel_name}{k}' for k in range(len(FLOPS))]
    flag = 'HBM'
# ok    peak_HBM = 1554.69056 # peak_bw * 1e3
# ok    peak_DP = 5.2860170972159995    # peak_gflops / 1e3
# ok    FLOPS = [
# ok        104.87154267766653, 105.13625724534072, 98.84322933786025,
# ok        100.81500816343082, 107.95501561404049, 104.71735919960484,
# ok        109.64074566906089, 102.59391015755575, 101.15644876541225,
# ok        104.90504196640012]
# ok    AI_DRAM = [
# ok        11.989979496906915, 11.730078239231905, 11.928239974476555,
# ok        11.667277506248913, 11.880154956907743, 11.750491368479192,
# ok        11.897316748936084, 11.679195813175933, 11.919139393480235,
# ok        11.769784428796296]
    print("peak_HBM:", peak_HBM, type(peak_HBM))  # 1.554
    print("peak_DP:", peak_DP, type(peak_DP))  # 5286077.4
    print("FLOPS:", FLOPS, type(FLOPS))
    print("kernel_gflops:", kernel_gflops, type(kernel_gflops))
    print("AI_DRAM:", AI_DRAM, type(AI_DRAM))  # 11.9
    my_title = (
        f'GPU Speed Of Light Roofline Chart ({filename})\n'
        'High-level overview of the utilization for compute and memory '
        'resources of the GPU presented as a roofline chart\n'
        '10 instances of Cuda Kernel (at $90^{th}$ steps, '
        f'Perf$\\leqslant${int(np.max(FLOPS))} GFLOP/sec, '
        f'AI$\\leqslant${int(np.max(AI_DRAM))} FLOPS/Byte).'
    )
    # roofline_ncu(tag, FLOPS, AI_DRAM, LABELS=LABELS, flag=flag,
    roofline_ncu(tag, kernel_gflops, AI_DRAM, LABELS=LABELS, flag=flag,
                 peak_HBM=peak_HBM, peak_DP=peak_DP, my_title=my_title)

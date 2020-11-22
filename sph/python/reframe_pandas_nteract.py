{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# jsonfile = 'strong.json'\n",
        "# jsonfile = '128mpi.json'\n",
        "jsonfile = '/tmp/POSTPROC/cce_weak.json'\n",
        "f = open(jsonfile) ;d = json.load(f) ;f.close()\n",
        "dd = d['runs'][0]['testcases']"
      ],
      "outputs": [],
      "execution_count": 1,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T13:38:30.534Z",
          "iopub.execute_input": "2020-11-05T13:38:30.537Z",
          "shell.execute_reply": "2020-11-05T13:38:30.666Z",
          "iopub.status.idle": "2020-11-05T13:38:30.670Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "mpiL = [] ;ompL = [] ;sideL = [] ;stepL = [] ;commitL = [] ;peL = []\n",
        "elapsedL = [] ;unitL = []\n",
        "aL = [];bL = [];cL = [];dL = [];eL = [];fL = [];gL = [];hL = [];iL = []\n",
        "jL = [];kL = [];lL = [];mL = [];nL = [];oL = []\n",
        "for job in range(len(dd)):\n",
        "    name = dd[job]['name'].split('_')\n",
        "    pe = dd[job]['environment']\n",
        "    mpiL.append(int(name[2].replace('mpi', '')))\n",
        "    ompL.append(int(name[3].replace('omp', '')))\n",
        "    sideL.append(int(name[5].replace('n', '')))\n",
        "    stepL.append(int(name[6].replace('steps', '')))\n",
        "    commitL.append(name[7])\n",
        "    peL.append(pe)\n",
        "    # {'name': '_Elapsed', 'reference': 0, 'thres_lower': None, 'thres_upper': None, 'unit': 's', 'value': 8}\n",
        "    for metric in range(len(dd[job]['perfvars'])):\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'Elapsed': elapsedL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'domain_distribute': aL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'mpi_synchronizeHalos': bL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'BuildTree': cL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'FindNeighbors': dL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'Density': eL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'EquationOfState': fL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'IAD': gL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'MomentumEnergyIAD': hL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'Timestep': iL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'UpdateQuantities': jL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'EnergyConservation': kL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        if dd[job]['perfvars'][metric]['name'] == 'SmoothingLength': lL.append(dd[job]['perfvars'][metric]['value'])\n",
        "        # unitL.append(dd[job]['perfvars'][metric]['unit'])\n",
        "\n",
        "df_dict = {'mpi': mpiL, 'openmp': ompL, 'cubeside': sideL, 'steps': stepL,\n",
        "           'gitcommit': commitL, 'pe': peL, 'elapsed': elapsedL,\n",
        "           'domain_distribute': aL, 'mpi_synchronizeHalos': bL, 'BuildTree': cL,\n",
        "           'FindNeighbors': dL, 'Density': eL, 'EquationOfState': fL,\n",
        "           'IAD': gL, 'MomentumEnergyIAD': hL, 'Timestep': iL, 'UpdateQuantities': jL,\n",
        "           'EnergyConservation': kL, 'SmoothingLength': lL,\n",
        "           }  # , 'unit': unitL}\n",
        "# print(mpiL, ompL, sideL, stepL, peL)\n",
        "\n",
        "df = pd.DataFrame(\n",
        "    df_dict,\n",
        "    columns = ['mpi', 'openmp', 'cubeside', 'steps', 'gitcommit', 'pe', 'elapsed',\n",
        "           'domain_distribute', 'mpi_synchronizeHalos', 'BuildTree',\n",
        "           'FindNeighbors', 'Density', 'EquationOfState',\n",
        "           'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities',\n",
        "           'EnergyConservation', 'SmoothingLength',\n",
        "    ])"
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     mpi  openmp  cubeside  steps gitcommit           pe   elapsed\n",
            "0    128       1       425      1   f982fde  PrgEnv-cray   26.9721\n",
            "1    256       1       535      1   f982fde  PrgEnv-cray   26.8286\n",
            "2    512       1       674      1   f982fde  PrgEnv-cray   31.3122\n",
            "3   1024       1       850      1   f982fde  PrgEnv-cray   27.2097\n",
            "4   2048       1      1071      1   f982fde  PrgEnv-cray   44.8215\n",
            "5   4096       1      1349      1   f982fde  PrgEnv-cray   39.4858\n",
            "6   8192       1      1700      1   f982fde  PrgEnv-cray   62.4377\n",
            "7  16384       1      2142      1   f982fde  PrgEnv-cray   44.7967\n",
            "8  32768       1      2698      1   f982fde  PrgEnv-cray  162.8040\n"
          ]
        }
      ],
      "execution_count": 2,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T13:39:01.094Z",
          "iopub.execute_input": "2020-11-05T13:39:01.098Z",
          "iopub.status.idle": "2020-11-05T13:39:01.107Z",
          "shell.execute_reply": "2020-11-05T13:39:01.111Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# print(df)\n",
        "print(df[['pe', 'cubeside', 'mpi', 'elapsed', 'openmp', 'steps', 'MomentumEnergyIAD']])"
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            pe  cubeside    mpi   elapsed  openmp  steps  MomentumEnergyIAD\n",
            "0  PrgEnv-cray       425    128   26.9721       1      1             5.3977\n",
            "1  PrgEnv-cray       535    256   26.8286       1      1             5.5122\n",
            "2  PrgEnv-cray       674    512   31.3122       1      1             5.6364\n",
            "3  PrgEnv-cray       850   1024   27.2097       1      1             5.5877\n",
            "4  PrgEnv-cray      1071   2048   44.8215       1      1             5.2044\n",
            "5  PrgEnv-cray      1349   4096   39.4858       1      1             4.7544\n",
            "6  PrgEnv-cray      1700   8192   62.4377       1      1             5.4943\n",
            "7  PrgEnv-cray      2142  16384   44.7967       1      1             5.6284\n",
            "8  PrgEnv-cray      2698  32768  162.8040       1      1             5.0892\n"
          ]
        }
      ],
      "execution_count": 18,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:07:46.394Z",
          "iopub.execute_input": "2020-11-05T14:07:46.399Z",
          "iopub.status.idle": "2020-11-05T14:07:46.411Z",
          "shell.execute_reply": "2020-11-05T14:07:46.415Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# plot: https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot\n",
        "# %matplotlib inline\n",
        "import matplotlib.pyplot as plt"
      ],
      "outputs": [],
      "execution_count": 20,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:09:28.005Z",
          "iopub.execute_input": "2020-11-05T14:09:28.009Z",
          "iopub.status.idle": "2020-11-05T14:09:28.017Z",
          "shell.execute_reply": "2020-11-05T14:09:28.020Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf1 = df[df['pe'].isin(['PrgEnv-cray'])]\n",
        "tmpdf1"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 43,
          "data": {
            "text/plain": "     mpi  openmp  cubeside  steps gitcommit           pe   elapsed  \\\n0    128       1       425      1   f982fde  PrgEnv-cray   26.9721   \n1    256       1       535      1   f982fde  PrgEnv-cray   26.8286   \n2    512       1       674      1   f982fde  PrgEnv-cray   31.3122   \n3   1024       1       850      1   f982fde  PrgEnv-cray   27.2097   \n4   2048       1      1071      1   f982fde  PrgEnv-cray   44.8215   \n5   4096       1      1349      1   f982fde  PrgEnv-cray   39.4858   \n6   8192       1      1700      1   f982fde  PrgEnv-cray   62.4377   \n7  16384       1      2142      1   f982fde  PrgEnv-cray   44.7967   \n8  32768       1      2698      1   f982fde  PrgEnv-cray  162.8040   \n\n   domain_distribute  mpi_synchronizeHalos  BuildTree  FindNeighbors  Density  \\\n0             2.5859                2.1741     1.9037         4.0965   2.4026   \n1             2.8955                3.2091     2.0939         4.2277   2.4946   \n2             3.1797                4.1907     3.0970         4.2274   2.5317   \n3             3.0239                4.0796     1.2920         4.1799   2.5854   \n4             3.5569               13.8668     1.9449         4.3819   2.4535   \n5             4.1697               12.6808     2.5802         4.3712   2.5059   \n6             6.6821                3.3354     2.7411         5.3852   2.4364   \n7             7.2803                9.9729     3.3023         5.4277   2.5266   \n8            10.3754               90.0528     4.1116         5.4494   2.5907   \n\n   EquationOfState     IAD  MomentumEnergyIAD  Timestep  UpdateQuantities  \\\n0           0.0080  3.2074             5.3977    5.0018            0.1226   \n1           0.0081  3.2740             5.5122    2.9154            0.1223   \n2           0.0082  3.3898             5.6364    4.7180            0.1227   \n3           0.0082  3.3070             5.5877    2.5514            0.1226   \n4           0.0085  3.3188             5.2044    9.7925            0.1220   \n5           0.0082  3.3264             4.7544    4.6981            0.1209   \n6           0.0082  3.2735             5.4943   32.1920            0.1194   \n7           0.0082  3.3768             5.6284    6.5853            0.1242   \n8           0.0087  3.0592             5.0892   41.4034            0.1247   \n\n   EnergyConservation  SmoothingLength  \n0              0.0241           0.0348  \n1              0.0249           0.0352  \n2              0.1599           0.0358  \n3              0.4183           0.0358  \n4              0.1208           0.0348  \n5              0.1905           0.0350  \n6              0.7143           0.0350  \n7              0.5084           0.0349  \n8              0.2202           0.0364  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>mpi</th>\n      <th>openmp</th>\n      <th>cubeside</th>\n      <th>steps</th>\n      <th>gitcommit</th>\n      <th>pe</th>\n      <th>elapsed</th>\n      <th>domain_distribute</th>\n      <th>mpi_synchronizeHalos</th>\n      <th>BuildTree</th>\n      <th>FindNeighbors</th>\n      <th>Density</th>\n      <th>EquationOfState</th>\n      <th>IAD</th>\n      <th>MomentumEnergyIAD</th>\n      <th>Timestep</th>\n      <th>UpdateQuantities</th>\n      <th>EnergyConservation</th>\n      <th>SmoothingLength</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>128</td>\n      <td>1</td>\n      <td>425</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>26.9721</td>\n      <td>2.5859</td>\n      <td>2.1741</td>\n      <td>1.9037</td>\n      <td>4.0965</td>\n      <td>2.4026</td>\n      <td>0.0080</td>\n      <td>3.2074</td>\n      <td>5.3977</td>\n      <td>5.0018</td>\n      <td>0.1226</td>\n      <td>0.0241</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>256</td>\n      <td>1</td>\n      <td>535</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>26.8286</td>\n      <td>2.8955</td>\n      <td>3.2091</td>\n      <td>2.0939</td>\n      <td>4.2277</td>\n      <td>2.4946</td>\n      <td>0.0081</td>\n      <td>3.2740</td>\n      <td>5.5122</td>\n      <td>2.9154</td>\n      <td>0.1223</td>\n      <td>0.0249</td>\n      <td>0.0352</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>512</td>\n      <td>1</td>\n      <td>674</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>31.3122</td>\n      <td>3.1797</td>\n      <td>4.1907</td>\n      <td>3.0970</td>\n      <td>4.2274</td>\n      <td>2.5317</td>\n      <td>0.0082</td>\n      <td>3.3898</td>\n      <td>5.6364</td>\n      <td>4.7180</td>\n      <td>0.1227</td>\n      <td>0.1599</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1024</td>\n      <td>1</td>\n      <td>850</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>27.2097</td>\n      <td>3.0239</td>\n      <td>4.0796</td>\n      <td>1.2920</td>\n      <td>4.1799</td>\n      <td>2.5854</td>\n      <td>0.0082</td>\n      <td>3.3070</td>\n      <td>5.5877</td>\n      <td>2.5514</td>\n      <td>0.1226</td>\n      <td>0.4183</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2048</td>\n      <td>1</td>\n      <td>1071</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>44.8215</td>\n      <td>3.5569</td>\n      <td>13.8668</td>\n      <td>1.9449</td>\n      <td>4.3819</td>\n      <td>2.4535</td>\n      <td>0.0085</td>\n      <td>3.3188</td>\n      <td>5.2044</td>\n      <td>9.7925</td>\n      <td>0.1220</td>\n      <td>0.1208</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>4096</td>\n      <td>1</td>\n      <td>1349</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>39.4858</td>\n      <td>4.1697</td>\n      <td>12.6808</td>\n      <td>2.5802</td>\n      <td>4.3712</td>\n      <td>2.5059</td>\n      <td>0.0082</td>\n      <td>3.3264</td>\n      <td>4.7544</td>\n      <td>4.6981</td>\n      <td>0.1209</td>\n      <td>0.1905</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>8192</td>\n      <td>1</td>\n      <td>1700</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>62.4377</td>\n      <td>6.6821</td>\n      <td>3.3354</td>\n      <td>2.7411</td>\n      <td>5.3852</td>\n      <td>2.4364</td>\n      <td>0.0082</td>\n      <td>3.2735</td>\n      <td>5.4943</td>\n      <td>32.1920</td>\n      <td>0.1194</td>\n      <td>0.7143</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>16384</td>\n      <td>1</td>\n      <td>2142</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>44.7967</td>\n      <td>7.2803</td>\n      <td>9.9729</td>\n      <td>3.3023</td>\n      <td>5.4277</td>\n      <td>2.5266</td>\n      <td>0.0082</td>\n      <td>3.3768</td>\n      <td>5.6284</td>\n      <td>6.5853</td>\n      <td>0.1242</td>\n      <td>0.5084</td>\n      <td>0.0349</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>32768</td>\n      <td>1</td>\n      <td>2698</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>162.8040</td>\n      <td>10.3754</td>\n      <td>90.0528</td>\n      <td>4.1116</td>\n      <td>5.4494</td>\n      <td>2.5907</td>\n      <td>0.0087</td>\n      <td>3.0592</td>\n      <td>5.0892</td>\n      <td>41.4034</td>\n      <td>0.1247</td>\n      <td>0.2202</td>\n      <td>0.0364</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 43,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:20:32.749Z",
          "iopub.execute_input": "2020-11-05T14:20:32.755Z",
          "iopub.status.idle": "2020-11-05T14:20:32.769Z",
          "shell.execute_reply": "2020-11-05T14:20:32.776Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf2 = tmpdf1[['domain_distribute', 'mpi_synchronizeHalos',\t'BuildTree', 'FindNeighbors', 'Density', 'EquationOfState', 'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities', 'EnergyConservation', 'SmoothingLength']]\n",
        "tmpdf2"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 52,
          "data": {
            "text/plain": "   domain_distribute  mpi_synchronizeHalos  BuildTree  FindNeighbors  Density  \\\n0             2.5859                2.1741     1.9037         4.0965   2.4026   \n1             2.8955                3.2091     2.0939         4.2277   2.4946   \n2             3.1797                4.1907     3.0970         4.2274   2.5317   \n3             3.0239                4.0796     1.2920         4.1799   2.5854   \n4             3.5569               13.8668     1.9449         4.3819   2.4535   \n5             4.1697               12.6808     2.5802         4.3712   2.5059   \n6             6.6821                3.3354     2.7411         5.3852   2.4364   \n7             7.2803                9.9729     3.3023         5.4277   2.5266   \n8            10.3754               90.0528     4.1116         5.4494   2.5907   \n\n   EquationOfState     IAD  MomentumEnergyIAD  Timestep  UpdateQuantities  \\\n0           0.0080  3.2074             5.3977    5.0018            0.1226   \n1           0.0081  3.2740             5.5122    2.9154            0.1223   \n2           0.0082  3.3898             5.6364    4.7180            0.1227   \n3           0.0082  3.3070             5.5877    2.5514            0.1226   \n4           0.0085  3.3188             5.2044    9.7925            0.1220   \n5           0.0082  3.3264             4.7544    4.6981            0.1209   \n6           0.0082  3.2735             5.4943   32.1920            0.1194   \n7           0.0082  3.3768             5.6284    6.5853            0.1242   \n8           0.0087  3.0592             5.0892   41.4034            0.1247   \n\n   EnergyConservation  SmoothingLength  \n0              0.0241           0.0348  \n1              0.0249           0.0352  \n2              0.1599           0.0358  \n3              0.4183           0.0358  \n4              0.1208           0.0348  \n5              0.1905           0.0350  \n6              0.7143           0.0350  \n7              0.5084           0.0349  \n8              0.2202           0.0364  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>domain_distribute</th>\n      <th>mpi_synchronizeHalos</th>\n      <th>BuildTree</th>\n      <th>FindNeighbors</th>\n      <th>Density</th>\n      <th>EquationOfState</th>\n      <th>IAD</th>\n      <th>MomentumEnergyIAD</th>\n      <th>Timestep</th>\n      <th>UpdateQuantities</th>\n      <th>EnergyConservation</th>\n      <th>SmoothingLength</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2.5859</td>\n      <td>2.1741</td>\n      <td>1.9037</td>\n      <td>4.0965</td>\n      <td>2.4026</td>\n      <td>0.0080</td>\n      <td>3.2074</td>\n      <td>5.3977</td>\n      <td>5.0018</td>\n      <td>0.1226</td>\n      <td>0.0241</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2.8955</td>\n      <td>3.2091</td>\n      <td>2.0939</td>\n      <td>4.2277</td>\n      <td>2.4946</td>\n      <td>0.0081</td>\n      <td>3.2740</td>\n      <td>5.5122</td>\n      <td>2.9154</td>\n      <td>0.1223</td>\n      <td>0.0249</td>\n      <td>0.0352</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>3.1797</td>\n      <td>4.1907</td>\n      <td>3.0970</td>\n      <td>4.2274</td>\n      <td>2.5317</td>\n      <td>0.0082</td>\n      <td>3.3898</td>\n      <td>5.6364</td>\n      <td>4.7180</td>\n      <td>0.1227</td>\n      <td>0.1599</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3.0239</td>\n      <td>4.0796</td>\n      <td>1.2920</td>\n      <td>4.1799</td>\n      <td>2.5854</td>\n      <td>0.0082</td>\n      <td>3.3070</td>\n      <td>5.5877</td>\n      <td>2.5514</td>\n      <td>0.1226</td>\n      <td>0.4183</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>3.5569</td>\n      <td>13.8668</td>\n      <td>1.9449</td>\n      <td>4.3819</td>\n      <td>2.4535</td>\n      <td>0.0085</td>\n      <td>3.3188</td>\n      <td>5.2044</td>\n      <td>9.7925</td>\n      <td>0.1220</td>\n      <td>0.1208</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>4.1697</td>\n      <td>12.6808</td>\n      <td>2.5802</td>\n      <td>4.3712</td>\n      <td>2.5059</td>\n      <td>0.0082</td>\n      <td>3.3264</td>\n      <td>4.7544</td>\n      <td>4.6981</td>\n      <td>0.1209</td>\n      <td>0.1905</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>6.6821</td>\n      <td>3.3354</td>\n      <td>2.7411</td>\n      <td>5.3852</td>\n      <td>2.4364</td>\n      <td>0.0082</td>\n      <td>3.2735</td>\n      <td>5.4943</td>\n      <td>32.1920</td>\n      <td>0.1194</td>\n      <td>0.7143</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>7.2803</td>\n      <td>9.9729</td>\n      <td>3.3023</td>\n      <td>5.4277</td>\n      <td>2.5266</td>\n      <td>0.0082</td>\n      <td>3.3768</td>\n      <td>5.6284</td>\n      <td>6.5853</td>\n      <td>0.1242</td>\n      <td>0.5084</td>\n      <td>0.0349</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>10.3754</td>\n      <td>90.0528</td>\n      <td>4.1116</td>\n      <td>5.4494</td>\n      <td>2.5907</td>\n      <td>0.0087</td>\n      <td>3.0592</td>\n      <td>5.0892</td>\n      <td>41.4034</td>\n      <td>0.1247</td>\n      <td>0.2202</td>\n      <td>0.0364</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 52,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:27:11.477Z",
          "iopub.execute_input": "2020-11-05T14:27:11.480Z",
          "iopub.status.idle": "2020-11-05T14:27:11.488Z",
          "shell.execute_reply": "2020-11-05T14:27:11.492Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf3 = tmpdf1[['mpi', 'domain_distribute', 'mpi_synchronizeHalos',\t'BuildTree', 'FindNeighbors', 'Density', 'EquationOfState', 'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities', 'EnergyConservation', 'SmoothingLength']]\n",
        "tmpdf3"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 57,
          "data": {
            "text/plain": "     mpi  domain_distribute  mpi_synchronizeHalos  BuildTree  FindNeighbors  \\\n0    128             2.5859                2.1741     1.9037         4.0965   \n1    256             2.8955                3.2091     2.0939         4.2277   \n2    512             3.1797                4.1907     3.0970         4.2274   \n3   1024             3.0239                4.0796     1.2920         4.1799   \n4   2048             3.5569               13.8668     1.9449         4.3819   \n5   4096             4.1697               12.6808     2.5802         4.3712   \n6   8192             6.6821                3.3354     2.7411         5.3852   \n7  16384             7.2803                9.9729     3.3023         5.4277   \n8  32768            10.3754               90.0528     4.1116         5.4494   \n\n   Density  EquationOfState     IAD  MomentumEnergyIAD  Timestep  \\\n0   2.4026           0.0080  3.2074             5.3977    5.0018   \n1   2.4946           0.0081  3.2740             5.5122    2.9154   \n2   2.5317           0.0082  3.3898             5.6364    4.7180   \n3   2.5854           0.0082  3.3070             5.5877    2.5514   \n4   2.4535           0.0085  3.3188             5.2044    9.7925   \n5   2.5059           0.0082  3.3264             4.7544    4.6981   \n6   2.4364           0.0082  3.2735             5.4943   32.1920   \n7   2.5266           0.0082  3.3768             5.6284    6.5853   \n8   2.5907           0.0087  3.0592             5.0892   41.4034   \n\n   UpdateQuantities  EnergyConservation  SmoothingLength  \n0            0.1226              0.0241           0.0348  \n1            0.1223              0.0249           0.0352  \n2            0.1227              0.1599           0.0358  \n3            0.1226              0.4183           0.0358  \n4            0.1220              0.1208           0.0348  \n5            0.1209              0.1905           0.0350  \n6            0.1194              0.7143           0.0350  \n7            0.1242              0.5084           0.0349  \n8            0.1247              0.2202           0.0364  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>mpi</th>\n      <th>domain_distribute</th>\n      <th>mpi_synchronizeHalos</th>\n      <th>BuildTree</th>\n      <th>FindNeighbors</th>\n      <th>Density</th>\n      <th>EquationOfState</th>\n      <th>IAD</th>\n      <th>MomentumEnergyIAD</th>\n      <th>Timestep</th>\n      <th>UpdateQuantities</th>\n      <th>EnergyConservation</th>\n      <th>SmoothingLength</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>128</td>\n      <td>2.5859</td>\n      <td>2.1741</td>\n      <td>1.9037</td>\n      <td>4.0965</td>\n      <td>2.4026</td>\n      <td>0.0080</td>\n      <td>3.2074</td>\n      <td>5.3977</td>\n      <td>5.0018</td>\n      <td>0.1226</td>\n      <td>0.0241</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>256</td>\n      <td>2.8955</td>\n      <td>3.2091</td>\n      <td>2.0939</td>\n      <td>4.2277</td>\n      <td>2.4946</td>\n      <td>0.0081</td>\n      <td>3.2740</td>\n      <td>5.5122</td>\n      <td>2.9154</td>\n      <td>0.1223</td>\n      <td>0.0249</td>\n      <td>0.0352</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>512</td>\n      <td>3.1797</td>\n      <td>4.1907</td>\n      <td>3.0970</td>\n      <td>4.2274</td>\n      <td>2.5317</td>\n      <td>0.0082</td>\n      <td>3.3898</td>\n      <td>5.6364</td>\n      <td>4.7180</td>\n      <td>0.1227</td>\n      <td>0.1599</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1024</td>\n      <td>3.0239</td>\n      <td>4.0796</td>\n      <td>1.2920</td>\n      <td>4.1799</td>\n      <td>2.5854</td>\n      <td>0.0082</td>\n      <td>3.3070</td>\n      <td>5.5877</td>\n      <td>2.5514</td>\n      <td>0.1226</td>\n      <td>0.4183</td>\n      <td>0.0358</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2048</td>\n      <td>3.5569</td>\n      <td>13.8668</td>\n      <td>1.9449</td>\n      <td>4.3819</td>\n      <td>2.4535</td>\n      <td>0.0085</td>\n      <td>3.3188</td>\n      <td>5.2044</td>\n      <td>9.7925</td>\n      <td>0.1220</td>\n      <td>0.1208</td>\n      <td>0.0348</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>4096</td>\n      <td>4.1697</td>\n      <td>12.6808</td>\n      <td>2.5802</td>\n      <td>4.3712</td>\n      <td>2.5059</td>\n      <td>0.0082</td>\n      <td>3.3264</td>\n      <td>4.7544</td>\n      <td>4.6981</td>\n      <td>0.1209</td>\n      <td>0.1905</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>8192</td>\n      <td>6.6821</td>\n      <td>3.3354</td>\n      <td>2.7411</td>\n      <td>5.3852</td>\n      <td>2.4364</td>\n      <td>0.0082</td>\n      <td>3.2735</td>\n      <td>5.4943</td>\n      <td>32.1920</td>\n      <td>0.1194</td>\n      <td>0.7143</td>\n      <td>0.0350</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>16384</td>\n      <td>7.2803</td>\n      <td>9.9729</td>\n      <td>3.3023</td>\n      <td>5.4277</td>\n      <td>2.5266</td>\n      <td>0.0082</td>\n      <td>3.3768</td>\n      <td>5.6284</td>\n      <td>6.5853</td>\n      <td>0.1242</td>\n      <td>0.5084</td>\n      <td>0.0349</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>32768</td>\n      <td>10.3754</td>\n      <td>90.0528</td>\n      <td>4.1116</td>\n      <td>5.4494</td>\n      <td>2.5907</td>\n      <td>0.0087</td>\n      <td>3.0592</td>\n      <td>5.0892</td>\n      <td>41.4034</td>\n      <td>0.1247</td>\n      <td>0.2202</td>\n      <td>0.0364</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 57,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:44:02.614Z",
          "iopub.execute_input": "2020-11-05T14:44:02.618Z",
          "iopub.status.idle": "2020-11-05T14:44:02.629Z",
          "shell.execute_reply": "2020-11-05T14:44:02.632Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sph_l = ['domain_distribute', 'mpi_synchronizeHalos',\t'BuildTree', 'FindNeighbors', 'Density', 'EquationOfState', 'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities', 'EnergyConservation', 'SmoothingLength']\n",
        "# tmpdf2.plot.area(stacked=True).legend(loc='center left',bbox_to_anchor=(1.0, 0.5));\n",
        "\n",
        "plot_kind = 'area'\n",
        "pltt = tmpdf3.plot(kind=plot_kind, x='mpi', y=sph_l).legend(loc='center left',bbox_to_anchor=(1.0, 0.5))\n",
        "# pltt.xticks(tmpdf3['mpi'], tmpdf3['mpi']);\n",
        "\n"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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hC1btgTb2tqCTU1Npba2tuDPf/7z1oULFxZh92JZjuPwr//6r5NLpZIWCoXcX/7yl1tnzZpV3lt57zvvvLNtw4YNgUsvvbS5t7fXqK2tte+8887WGTNmlD/84Q83x+NxZ9WqVdHu7m7zhhtu2DG8iudo8Y5RHla++BAnuFu4tfJDuLN6kRI2bToF2wrS3LyKTRtPHdXn2XaQbKZhj3bDKBCPd2EGihi6g+tqlMpherqnYPsVF73zikSiKd/t4VsqoilM8+iwtA24FwYsB/FBsQgjuRfKe7gXkIKyZWKVQ5RKMVKpRlz3yH0lhRREZZAKGSYuw1TJKLOdJhxcnjHWMdtpYro7ntfT61nXuxwpLZriS3AciblpA8e3P0U2Op4t085nWsueKZgZPwVzxWyNWdslp2+A/10ssAJweTLFlX0p+nSdb9TV8KlUmqmWWvBJMTYplUra7Nmz5/a//9KXvtRx+eWX9wHU1dXZb7zxxrqbb765/uabb2685557tn31q18df/bZZ6d/97vftfb09OgLFy6cc8EFF6QB1q5dG1m9evXaxsZG5xvf+EZjVVWV09LSsvall14KnXbaaccCfOpTn+qbN2/e+FKptCMYDMrf/OY3dbfffvu2hx56KH788cePmMt85513Vr3++uvhdevWre3o6DAWLVo059xzz80CrFu3Lrxy5cotzc3N1oIFC2Y//PDDseOPP77wl7/8pXrLli1rNE2jv0T2P//zP0/64he/uOu8887Lbtq0KXDeeefN2LJly1qATZs2hVasWLE+FovJb33rWw133XVXzcKFC9u3bdtmdnV1mWeddVa+t7dXe+mll9abpskDDzwQv+aaayYuX768ZW/lvQGuvPLKyR//+McTn/3sZxP/9V//VXvllVdOeuSRR1oAdu3aZb788svrV65cGfrQhz40XSkP+8FffvavGKU051x5B0IbWmug9/EfkJFhJpntVIRa6OycRqJnCpOnrKR16wkcrhmtbYfJZMLDWiWGUaSiwo/6111cV6dUCtPVNXWIGd80CwOuj+ggi4VplhltPPdCZHdQ4jAlYbh7IRDIEwplqarahWmW0DQX29ZwnMPjXtgfTKkPKAf92/79mAyhDZLNwWWn1kuHluRUeyaWY/G3rj+TKq7B0BuYWbGARMph9vr7iRZ2sb1pCZpTZvb6kVMwf/IBjXQE/v4ph63jvCqYkyyL73QkOKFUZnkkwtaAydd7ejk66uYpFAfHvtwWH/vYx/oAFi1alH/wwQerAZ544omK5cuXV916663jwCsOtXnz5gDAmWeemW5sbHQAnnvuudjnP//5LoCTTz65OHPmzDx4hbje9a53Ze65557K+fPnFy3LEosWLSo89NBD8ZFkAHj66afjF198ca9hGEyaNMk+5ZRTss8880yksrLSnT9/fm7atGkWwLHHHptvaWkJLF26NBsMBt1LLrmkedmyZcl+d8Kzzz5bsWnTpoEfdb+AlQbw3ve+NxmLxSTAJz/5yb5zzjln5ve///32O++8s/r888/vA6/a6CWXXDK1tbU1JISQlmW96WD02muvRf/617+2AFx55ZW93/rWtyb2H7vggguSuq6zYMGCYiKROGQ/JW8b5aG9o5V3b7+ToLD50//rZtl1Dw4c6+ls44z889wbXsrzVcfwvsIutrScTEXFLjLpWixr+GB+uBHYdph0ek+lwjQLRKO9GGYZQ3dwXJ1SKULXrmk4zu7vhRnIey6PwS6QaBLDsPb55KHuhaGZC/vrXrAsA9t3L+TzR8a9MCCjhCgh4m6YuAxRISO+ghCiQoYJMVThKVImI4r0iAxtWg+OcNGkRkDqhGWQShlhsl3Hltx2Xun5M66bojZyMlHNxGlt5cRtf6EcqGDd7I+PmIJZNuA3fgrmhITkkqf9FMwo/H06w5d7k9hC8O811VyYzXFeXi34pHh7M6iUtbRtWwBIKbnvvvs2H3/88UNMq88880w0Eons1xLAV1xxRc+NN944bubMmcVPfOITPQDz588vPPDAA29aDXM4wWBwIKVJ13Vs2xamabJy5cp1Dz74YMV9991X/ZOf/KThhRde2Cil5NVXX10XiUT2SIOKRqMDsk+dOtWqqqqyV6xYEb7//vtrbrvttm0A1157bdPixYszDz/8cMuGDRsCS5cufUv+8/7+Ba9fDxVvG+Xh2f+7mb8XNn/TF7Gs+CR//P4nOf9f7wTgxQdu5v3CIVNjcuH4/+P1VecAkrr67WxpWUhMhjjWnoSBBggE/UOfQEivZeD9wPH+luHHwUXSJ3IktAwJkSEtCgc5lgosK4JlDVvVEIlp5v0BvISu2ziuQakYobNzOq67W6kIBPIDVopQOINtBYekOpaHrZg44F6IJqmq7vBcK1JgDbgX4kfcvWBKfYjFYLj1QB9kPXBxyYoiaQps07opaTYSiSF1gq5JjBBxGaZOxgf+ioOxXZsnEk+yK7sCocWZU/0BElmbiRv/RlV6C7vqT9yvFMxzX3GReCmYtY7Lf+9KcFahyIpQkKcjEb7YlySiFnxSvEM5++yz07fcckvjL3/5yzZN03j22WfD73rXuwrDzzvttNOyd999d/X555+feeWVV0IbN24cmHEtXbo0d/XVVwfWrl0bff3119cCnH/++Zmvf/3r4nvf+17dl7/85R6AFStWhPv6+vSzzjor89Of/rT+6quvTnR1dRkvvvhi7NZbb92+evXqEWeTqVRKy2az2iWXXJJ6z3vek502bdp8gDPOOCN90003Ndxwww27wMuSOP300/eQHeDDH/5w73e+851xmUxGP+WUUwoA6XRanzhxYhng9ttvr+s/d1/lvU888cTcz372s+p/+Zd/6b399ttrFi5cmB3pvEPJ20J5sK0y7+p6iOe0Y1kxfipWp875qT/w8E+/xNmX3siCzj/zpHY8LcVJhNoKZNINHDPtRVq3noiQgneX51MjY5TxBhYAObAHUnj7clDr7u3u9v59A51Jbi2a4/3dy9gkRIaEliWhpUmILH0ihxQHO1gILCuKlYoOa5cEAjlCoQSmWULXXd+yEKUjNXNgwO93L1RWdRAwS2iaxHE0L4ahFKFUjJPoOYLuBQkR/NgDN7yHmyE8zHpQwiIjCiREhh1aAls4CCkISIOwDBAnTKOswpQ67MccxnVdMnaOXeUEa/qexLI7iYfm0hiootDRwwmbfw9obJhxMeM6X6Sx+7Wh1wt48BTBPWdpxAvwmT+7A1Uw353L882eXsJS8v3qKk4uFPhy7yFxSSoUgJdaOdqpmm92zvCYh6VLl6Z+/OMf73VFvptvvrn9iiuumDx79uy5ruuKSZMmlR5//PE9CgN95Stf6b744oubp02bduy0adOK06dPL1ZXVw+kIn3wgx/sW716daS+vt4B0DSNBx98sOWqq66a9IMf/GBcMBiUEydOLP3whz/cfu6552afe+652Jw5c44VQshvfetbOyZPnmyvXr16RBmTyaS+bNmy6aVSSQDccMMN2wHuuOOO7ZdddtnkmTNnznUcR5xyyimZ008/vW2ke3ziE5/o+/rXvz7585//fHt/27XXXtt52WWXTf3ud7874Zxz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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 68,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:50:19.118Z",
          "iopub.execute_input": "2020-11-05T14:50:19.124Z",
          "iopub.status.idle": "2020-11-05T14:50:19.392Z",
          "shell.execute_reply": "2020-11-05T14:50:19.401Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "type(pltt)"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 69,
          "data": {
            "text/plain": "matplotlib.legend.Legend"
          },
          "metadata": {}
        }
      ],
      "execution_count": 69,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:50:55.290Z",
          "iopub.execute_input": "2020-11-05T14:50:55.294Z",
          "iopub.status.idle": "2020-11-05T14:50:55.305Z",
          "shell.execute_reply": "2020-11-05T14:50:55.311Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# pandas plot:\n",
        "plot_kind = 'bar'\n",
        "tmpdf3.plot(kind=plot_kind, x='mpi', y=sph_l, stacked=True).legend(loc='center left',bbox_to_anchor=(1.0, 0.5));\n"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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rt+T5ox7HhhjzEC23yo3WFvPG6yllsHKykp89tlnFwYPHuxtaWmp6dq1a2FhYeFd8wQsLCzE5MmTr7355psdAaBDhw6qlStXZjz55JOet2/fJgBYsGBBZqdOncr0z/Hw8Ch/+eWXs0JDQ/1tbW1V3t7epba2tjWuBAwICCiaOnWqW0ZGhkX37t3zx44de0sqlWLBggWZvXv39hVCUP/+/W89/fTTtyo/99atW9LBgwd7l5WVEQC88847l+66QQvGJbkZY8xAPp+632BtPb+i5uIWXJK79vLy8iS2traa8vJyPPLII97PPPNMzrhx424ZO67mrEEluRljjLGWbs6cOR3kcrnC19dX6ebmVlZVbwGrPR62YIwxAwn/3ZCDDUkGbIutWrXqsrFjuJ9wzwNjjDHG6oSTB8YYY4zVCScPjDHGGKsTTh4YY4wxViecPDDGGDMofUlub29vpZ+fn2LBggXO+qJShvJ///d/bf73v/85AtqS3RkZGaY1PYcZDq+2YIyx+9jnU/cbtCT38yvC61SSOzMz02TEiBGe+fn50o8//viKoeJ45ZVXruu//vbbb506d+5cIpPJDLdLF7snTh4YY8xARr5quF+pcQZrybhcXFxUa9asyejevbti6dKlVzQaDZ5//nnXP/74w+b27ds0adKka3PmzMnZuXOnzcKFCzs4ODiUp6SkWAYGBhZv27btb4lEgmnTprns3bvXTiqVij59+uSvWrXq8syZMztYW1urPTw8bsfHx1uNGzfO08LCQvPWW29lrlmzxmnfvn3pAPDTTz+1Xr58eZuqCnSx+uPkgTHGWKNSKBS31Wo1MjMzTTZt2mRna2urjo+PTyopKaEHHnhAPmTIkHyg6lLdQUFBJbt27bKvrrT1hAkTcr/44ou2S5YsudSrV69ijUaDV1991fXKlSsmHTp0UH311VeOEyZM4B03DazGOQ9E9BURXSOi+ArHHIgomohSdX/b644TES0jojQiOktEXRozeMYYYy3Lvn37Wm/evNlRLpcrgoOD/XNzc00SExMtgKpLdde1tLVEIsHIkSNvrF692iEnJ0d66tQp6xEjRuQ1zav776jNhMmvAQysdGwegN+EED4AftM9BoBBAHx0fyYD+MIwYTLGGGupEhMTzaRSKVxcXFRCCFq6dOnF5OTkxOTk5MTMzMy4J554Ih+oulS3vrT1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bVudu+7Nzc3v7HoslUqhUqnI1NQUZ86cSdqxY0frLVu22H/xxRdtjx07dk4IgVOnTiVZWVndtVNyq1at7sTu4eFRbmdnpzp+/Ljljz/+6LBixYoLADB37lyX3r17F0RHR6enpKSYhYeH+9U13or0319A+31tLJw83Ie+fHiGAVvj5IEx1rj69u2bv3TpUuevv/76okQiwR9//GH50EMPlVS+rlu3boUbN260HzJkSMHJkyctzp07d+cTf3h4eNH06dPNEhISWsXFxSUAwJAhQwrefPNNWrJkidPs2bNzAOD48eOWubm50l69ehWsXr26zfTp029cu3bN5K+//rJetmzZpbNnz1pWvi8A5OXlSQoLCyWjRo3K69+/f6GXl1cgAPTo0SP//fffb/vOO+9cBbSrJLp3735X7AAQGRl587333mtXUFAg7dq1awkA5OfnS11dXW8DwMqVK530196rvHdwcHDRmjVr7J9//vmbK1eudAgNDS2s3XfacDh5YKyZ4U/UrKWrPOchPDw8b/ny5dWWKli8ePGVyZMnu8nlcoVGo6GOHTuWHThwIK3ydXPmzLk+cuRImZeXl9LLy6vU29u71N7e/k6Z6qFDh+aePXvWqk2bNmoAkEgk2LFjR/q0adM6fvrpp+3Mzc2Fq6tr2WeffXbp4YcfLjx69Ki1v7+/kojE22+/fdnNzU119uzZKmO8deuWdPDgwd5lZWUEAO+8884lAFi1atWliRMnuvn6+irUajV17dq1oHv37herauPpp5/OffPNN91efPHFK/pjc+fOzZ44caLHBx980GHAgAG39MfvVd57xYoVF8eNGyf79NNP2zk6OqrWr1+fUd33trE0qCS3oXBJbsNqlqWKm6HL8w4brC3XxT0N1pah4jJkTG+99Vazagdopv9+XJK7UalUKty+fZusrKxEQkKC+cMPP+ybnp4er++q79u3r/dLL7109fHHHy8wdqz3g8Ysyc0YY0ax/Va5wdp63mAtscZUUFAg6dmzp195eTkJIfDxxx9fsLCwEPoVGv7+/sWcODQNTh4YY4y1CPb29pr4+PikysednJzUGRkZ8caI6b+qRSUPhuqON2RXfHOMqTnioRTGGLt/tKjkgdVOc912ublprt3ehorrfu+KD//dkK/wrg+zjLF74O2pGWOMMVYnnDwwxhhjrE542KKBuAJi7TTHoZTm2u1tuLgMFxPvPcHqau7cue22bt3qKJFIhEQiwfLlyy+Eh4cXGfo+KSkpZgcOHLCeOnXqTUBbA6JiTYiKevfu7b1169a/nZyc1He3dG87d+60Wbp0qXNV+08YQk5OjnTNmjUO8+bNu94U92uoeicPRNQRwHoAzgAEgFVCiE+JyAHAJgAyABkARgohGqUwB2OMsRq8ZWvQktx4K6/Gktz79u1rtXfvXru4uLhES0tLkZWVZaLfXMnQUlNTzTdt2uSgTx7u5eDBg83yjRgAbty4If3yyy/b6pOH5q4hPQ8qALOEEKeIyAbASSKKBvAMgN+EEIuJaB6AeQDmNjxU/pTPGGMtQWZmpqmDg4PK0tJSAED79u1VgLYk99ChQ2/+9ttvtiYmJmLFihUX5s2b53LhwgXzF1544eorr7xyXaPRICoqynX//v22RCTmzJmTNWnSpNzqjr/++usu58+ft5DL5Yqnnnoqx97eXp2dnW3as2dPn4sXL5oPGjTo1ooVKy7r7x8TE5OUn58vGTRokE9YWFhhTEyMtbOz8+29e/emWVtbi4MHD1pNmjRJJpFI0Lt37/z9+/fbpqamJlT3Wn/88cfWCxcu7HD79m1yd3cv27hxY4atra3GxcUlcOTIkTf27t1rq1KpaNOmTeeDg4NLr1y5YjJ8+HCPa9eumYWEhBQePny49cmTJ5NmzZrleunSJXO5XK7o3bt3/pAhQ/KKioqkAwcO9ExJSbEMDAws3rZt298SSfOYbVDvKIQQWUKIU7qvC6DtI3UB8DiAdbrL1gEY2sAYGWOMtSBDhw7Nv3LliplMJgt4+umn3X755Rdr/Tk3N7fbycnJiV27di189tlnZT///HP68ePHkz/44IMOwL9LZf/222/n5s+f73rhwgXT6o4vWrQoMzQ0tDA5OTlxwYIF1wAgMTHRatu2beeTkpISduzYYZ+WlnZXdcmLFy9azJgx41paWlqCra2tev369fYAMHHiRI/ly5dfSE5OTpRKpffcgjkrK8vkvffea3/o0KFziYmJSV26dCl+5513nPXn9eXHn3322euLFy92BoB58+Z16N27d0FaWlrCiBEjcrOysswAYOnSpZc7duxYlpycnLhy5crLgLY0+Oeff34pLS0t4eLFi+bR0dHWVUfS9Awy54GIZACCARwH4CyE0O/DnQ3tsAZrQjw+zQytOS4fHfmq4aZsxRmsJQZoS2THx8cn7tmzx+a3336zGT9+vNf8+fMvA8DIkSNvAUBgYGBxUVGRxN7eXmNvb68xMzPT5OTkSKsrlX2vEtqV79+jR498R0dHNQB4e3uXpqenm3t7e//rh9jFxaVMX8AqODi4OCMjwzwnJ0daVFQk6d+/fxEAjB8//mZ0dLRdda/z999/b5Wenm4RFhYmB4Dy8nIKCQm5U6SqqvLjf/31l/W2bdvSAGD48OH5rVu3rnb+RVWlwWv+7jeNBv/vIyJrAFsBvCSEyCf6Z1hLCCGIqMrMjYgmA5gMAG5ubg0Ng7E6a65vPoaKi98QmTGZmJhg8ODBBYMHDy7o1KlTyTfffOMI/FMyWiKRwMzM7M77g0QiQXl5uUHmRVRsVyqViqrarXxNSUlJnXvihRDo0aNH/s8///x3VeerKj9eF1WVBq9rG42lQYMnRGQKbeKwQQjxo+7wVSJqrzvfHsC1qp4rhFglhAgVQoS2adOmIWEwxhhrRmJjY83j4uLM9Y9Pnz5tqS87XZNevXoVbNmyxUGlUuHKlSsmf/31l3XPnj2Lqjtua2urLiwslBoibicnJ3WrVq00+/fvbwUA33zzjcO9ru/Tp09RTEyMdXx8vDkA5OfnS86ePWt+r+c88MADhfp2f/zxx9b5+flSALC1tVUXFRU1jwkNtdCQ1RYE4EsASUKIjyqc2gFgPIDFur+3NyjCZo6HCGqHv08tW3NcPsqar/z8fOmMGTPc8vPzpVKpVMhksrJ169ZdCA0NrbHs6NixY29VVSq7uuPOzs5qqVQq/Pz8FKNHj86pWKK7PlauXJkxdepUd4lEgm7duhXY2Njcae/PP/9s7ezs3En/eMOGDekrV67MePLJJz1v375NALBgwYLMTp06lVXX/uLFi68MHz7c08fHxzEkJKTQycmp3M7OTm1paSlCQkIKfXx8lOHh4XlDhgypuayqEdW7JDcR9QBwGNreUf2Y02vQznvYDMANwAVol2recwlNbUty389lgQ1ZPvnzqfsN1tbzKwyzNIXLJ9de4LpAg7QTN95wAxdJcn+DtOOfbMDkoTn++3FJ7hYvLy9Pop9H8dprr7XLysoyXbt27SVDtV9SUkImJibC1NQU+/btazV9+nT35OTkREO1b0iNUpJbCHEEQHXjL43yMZM/vbL/gri/79rbhjHWRDZv3my7dOnS9mq1mlxcXMq+++67DEO2n5aWZjZy5EgvjUYDU1NTsXLlSoO231R4h0nGGGNMZ9KkSbmTJk1qtI0NAwMDy5KSkpplT0NdcPLQQM1xCVtz3Ha5uVawZIwxVnctZmYnY4yxWtFoNJpms6SPtUy6n6G79tDQa1E9D83xUz5jjDUz8devX1e0adMmTyKR1G9GPPtP02g0dP36dVsA8dVd06KSh+aIl7DVTnMcSmG1xxtXtRwqlWpidnb2muzs7ABw7zKrHw2AeJVKNbG6Czh5YIyx+0hISMg1ABHGjoPd31pU8sCf8hljjDHja1HJA6ud5lqzgbVcvPdE7chKvzNYWxkGa4kxw+PxMMYYY4zVCfc8sCbBvSGMMXb/4OShgXgWOmOMsf8aTh7uQ81xfLo5xsRaNp5fwJjxtKjkoTl+yuc3RfZfYKg36gyDtMIYMzaeMMkYY4yxOmlRPQ/8KZ8xxhgzvhaVPDD2X8BDBIyx5o6ThwZqjr/om+NEMo6JMcbuH42WPBDRQACfApACWCOEWNzQNpvjGzVjjDH2X9MoEyaJSArgcwCDACgAPEVEisa4F2OMMcaaVmOttggDkCaEOC+EuA1gI4DHG+lejDHGGGtCJIQwfKNEwwEMFEJM1D0eC6CrEGJ6hWsmA5ise+gHIMVAt3cCkGOgtgyFY6qd5hgT0Dzj4phq536PyV0I0cZAbTFWa0abMCmEWAVglaHbJaIYIUSoodttCI6pdppjTEDzjItjqh2OibHG0VjDFpkAOlZ47Ko7xhhjjLEWrrGShxMAfIjIg4jMADwJYEcj3YsxxhhjTahRhi2EECoimg5gL7RLNb8SQiQ0xr2qYPChEAPgmGqnOcYENM+4OKba4ZgYawSNMmGSMcYYY/cvLozFGGOMsTrh5IExxhhjdcLJA2OMMcbqhJMHxhhjjNUJJw8GRkRmREQVHvclollENMiYceliMa3imJMxYmmuiKgXEfnpvn6IiGYT0WNGjMeNiCx0XxMRTSCiz4goioiMWhWXiORE1I+IrCsdH2ismJobIgologNE9C0RdSSiaCLKI6ITRBRs7PgYq68Wnzzofrna6b6WEdFwIgowYkgnAOjjmQNgEQBLADOJ6H1jBKRLYC4DyCKiX4lIVuH0r8aIqTpEtN6I9/4EwGIA3xDROwA+hPbf7mUi+tBIYe3CP/9PFwN4DMBxAA/AiEv+iGgGgO0AXgAQT0QVa9e8Z5yo7kZE54wcwnIA/wfgFwBHAawUQtgCmKc7x1iL1KKXahLRPABTAJQBWAJgNoA/ADwI4EshxEdGiCleCBGg+zoGQE8hRInuU+IpIUQnI8R0AsAzQogEXd2R9wGMFUIcI6LTQgijfAIiosobhxGAvgD2A4AQIqKJ40kAEABtwpAJwEUIUazrsTmt/3dt4pgShRAK3dcnATwghNDoHscKIYKaOibdveMAdBNCFOqS0S0AvhFCfGqsnykiKgCg/4Wm7/2zAlAMQAghWhshpjvfCyK6KIRwq+ocYy2NUbs9DWAstCW/rQBkAPAUQlwnolbQfjpr8uQBQD4RBQgh4qEtfmMBoATa77WxenrM9Jt0CSG2EFESgB+JaC7++WVrDK4AEgGs0cVBAEIBLDVSPEIIIYhIo3+s+1sD4/3bXSKicCHEfmh/xjsCuEBEjkaKR08ihCgEACFEBhH1AbCFiNzxzxt3U1sLba/fHCHEVQAgor+FEB5GigcASonoYQC2AAQRDRVCbCOi3gDURoyLsQZp6cmDWvep/ja0b9A3AEAIUVRh2kFTmwpgAxHFArgGIIaIDgEIhPG6c8uJqJ0QIhsAdD0Q/QDsBOBlpJgAbaLwIoDXof2Ff4aISoQQB40Uzy9EdBjahG8NgM1EdAxAbwCHjBTTRADriegtAHkAzhDRGWjfJGcaKSYAuEpEnYUQZwBA1wMxGMBX0P6sNzkhxAwiCgHwPRFtA/A/GDc5BrS/D/4P2gT0EQBRRPQ1tD1bk+/xPMaatZY+bPE1ADMAraDtmlQB2AMgHICNEGKkkeKSAngYgC+0CdplAHuFELeMFE9/ANeFELGVjtsCmC6EWGSMuCrE4QrgYwBXAURU7No1QizdoO2BOEZEXgCGAbgIYIt+uMBIcfnj3z9PJ4wcjysAlT4hrXTuISHEH0YIS39/CYDpAEYA8BJCdDBWLIzdr1p68mAC7S8IAe2YaxiA0dD+sv9cCFFkxPBYHelWNTwkhHjN2LHoEVGEEKJZFHUjIntoe9vyjR2LHhG1gXb4SQ3gvH4oozkgovYAgoUQu4wYQ1cASUKIfCKyhHaiZBdoh+veE0LkGSs2xhqiRScPzRERDRRC7NF9bQvtvIsHAMQDeFk/FttcENFuIYTRl5E2B0T0ROVDAD4HMA0AhBA/GiGmDtCusngcgDX+KW3/FYBFQojypo5JF5cCwDIAMgBuAE4DaAvgIIAXjfGmSP9U8L0ihNhHRKMBdAeQBGCVMb5Xukm4Qbpigaug7SHdAqCf7njlnznGWoQWnTwQUWsAr0L7yWe3EOK7CueWCyGmGSGmU0KILrqv1wDIBrAawBMAegshhhohpi7VnQKwUwjRvinjuXNzokBovzcuAHYDmCuEyNWd+0sIEdbE8ZRDWwn2Gv6Z9Dcc2l/2QgjxbFPGo4tpP4CFQojfdclNTwBvQPtz31YIYZRxc91ckPFCiBQiCgPwvBBiPBFNAvCIEGK4EWLaAO2wjhWAW9AmWz9C+0ZNQojxRogpSQjhr/v6zu8G3eMzQojOTR0TY4bQ0pOHrQBSARwD8CyAcgCjhRBllf+jNmFMFZOHf/1yMNYvCyJSQ/uJsKpZpA8KISybOCQAABEdAfAutP9+EwFMgHbOQ7oxlrER0QPQfsrfIoT4QnfMqLP1Ky/HJKKTQogQ3dfJQgh5M4mr4s/9nTfMJo7prBCik244MxNAByGEmrSzp2ONtEz6BwC7hBBriWgttMOpMUTkC2CDEOKBpo6JMUNo6astvIQQkbqvtxHR6wD2E1GT7g9QSVsimgntG3VrIiLxT4ZmrOV+SQCmCCFSK58goktGiEfPRj/EA2CJbh+DPUQ0FkaYJS+EOEFEAwC8QEQHABh7KSsAXCeipwEcgLb3KgPQ7jYJ427ylk5Eb0K7J8cTAM7o4jI1YlwS3dBFK2h7H2wB3ARgDuCu3VWbyEQAnxLRG9Au3f5T93/uku4cYy1SS08ezIlIop91LoRYRESZ0C6rs773UxvNagA2uq/XAXCC9g2gHXS/YI3gLVT/C/2FJozjLkRkqx8fF0IcIKJIAFsBOBgjHt3P0qdEtAXaFSDG9iy0G6DNg/bnZ7ruuAO0QxfG8iyA13QxxEK75BbQvmk3+fCAzpcAkgFIoV3++wMRnYd207iNxghI97P9jG6I1QO61TLNbe4TY3XV0oct/g/Ar0KIfZWODwTwmRDCx0hxyaEdxz9ecfZ5xcmUxkREPaBdmRIvhDDa9tS6CW3nhRDHKh13A/CmEGKScSJjLZVugimEEFdIu219fwAXhRB/GSkeO2Mt0WasMbXo5OFeiGiCEGKtEe77ArSfDpMAdIZ25vl23TljzcO4M/lQN6HteQA/QbsXxc9CiMVNHVNzpFsd8yqAodCuHBDQTp7cDmCxMd4EdOP3z+lictEdztTF9KWxVlvcCxGtMuJETgmg7UHSDWEEAMgQQtw0UjwqAL8D+B7AVk4k2P3ifk4e/rWPfBPetznu+X/nvqStc/Go+Gcb72NCCKPsCNjc3qyJaC+0Y/jr9Jsf6YabxgPoJ4R4uCnj0d3/e2hXDqyDdnMoQLu6aDwAByHEqKaOSRdXdcNK+smJrk0ZDwAQ0VAAK6HdzXEqtMMqhQD8AEQJIX42Qkxx0P6MPwVgIIAj0CYS24UQJU0dD2OG0qKTByI6W90pAL5CCPOmjAfQrusWQigrPLaGNoFIBBBupNUWsQD6QDvvYa8QIrTCOaMkNLp7N6s3ayJKEUL41fVcI8d0TgjhW9dzjU23gucC/r2CR1+fxEUIYWaEmE4DGARtYbNYaIuIpZC23sbWij/3TRhTxVUolgCGQLsXRW9o/y+ObuqYGDOElj5h0hna/eJzKx0naMvfGkOz2/Mf2lnnJ6H9vggiai+EyNIlNkYrAgJAJoT4oOIBXRLxARE1+Z4K0BacegXaZEZfWMkZwDPQzo43hptENALaNz99NU0JtDurVv65b0rnoU3wLlY+YcwVPBWS0ItCiBTdsQv64QwjuPP/S9fTsBnamim20Pa4MdYiGXOplyHsBGAthLhQ6U8GtOOMxjAO2o2h7hBCqIQQ4wD0MkZAQgiZEMJTCOGh+ztLd0oDbe0GY7lARK/o3qABaN+sSVvt0xhvQKMAOAI4SES5RHQT2p8jBwBGqZMC7afU4dAmpeeIKBXan68ndOeM5RMA9tWc+78mjONfKiQJz1Y4JoW2Bo4xbKjqoBAiTwixrqmDYcxQWvSwBWvZSFurYR60Wy+31R2+CmAHtHMemvyTtW6ljCu0c0Ga1UoZ+qcM96dCiKeNHIs5tMlWc9oK+gEAcUKI0krHZQB6CCG+beqYGLtfcfLAmiVjrJYhohnQrkRpTitlqirKFQ7tXBEIIYyyIRo1w62gq0JEjkKIG0a8vxTazaBcAewRFaqNEtEbQoh3jRUbYw3ByQNrloyxWqaZrpQ5Be1k2zX4Z0Li99ANWQghDjZ1TLq4muNW0IsBLBFC5BBRKLTzCzTQ7i45zhjfK9LWt7EC8BeAsQAOCiFm6s4ZJSFlzBBa+oRJ1oLVsFrGuZpzjUmiH6oQQmQQUR8AW3Sz9Y01sTQU2t0bXwcwRwhxhohKjJU0VNAct4J+TAgxT/f1hwBGCe2W474AvoP2e9nUwvSJFBH9D8ByIvoR2qWbxpyszFiDcPLAjKm5rZZpditldCssPiZtgaWPiegqmsf/22a3FTQAEyIyEUKoAFgKIU4AgBDinG6OhjHcmaipi2syES2AdtjJWFvoM9ZgPGzBjIaIvgSwVghxpIpz3zX1GngicgWg0i/3q3TuoYrj1cZCRI8BeEgI8VoziKW5bQX9ArT7KCyGdmWTPbTzMMIBeAohxhohpm8BfFt5si0RTQTwhRDCWL00jDUIJw+MsfuGbqgpCoAvtD00lwBsA/CV7pO/MWIKAyB0QygKaHeaTBZC7DJGPIwZAicPjLH7nhFr3SyAdtdLEwDRALpCW159ALQ7TC5q6pgYMwROHhhj9z0j17rpDO1E0mwArkKIfN1W1ceNsSqFMUNoDhOvGGOswZrh6h1AO4dGDaCYiNKFEPmAdqtqItIYKSbGGoyTB8bY/aK5rd4BgNtEZCWEKAYQcicgbW0LTh5Yi8XJA2PsfqGvdXOm8gki+r3Jo9HqJYQoA+4su9UzhbZ6LGMtEs95YIwxxlidtPSqmowxxhhrYpw8MMYYY6xOOHlgrJ6IqAMRbTF2HIwx1tR4zgNjjDHG6oR7Hth/GhHJiCiZiL4monNEtIGI+hPRH0SUSkRhRPQWEX1DRH/qjk2q8Nx4Y78GxhhrarxUkzHAG8AIAM8COAFgNIAeACIAvAbgDIBO0FaMbAXgNBH9YpRIGWOsGeCeB8aAv4UQcbp1+AkAfhPa8bw4ADLdNduFECVCiBxoaxOEGSdUxhgzPk4eGAPKKnytqfBYg3965ypPDuLJQoyx/yxOHhirnceJyIKIHAH0gXZ4gzHG/pN4zgNjtXMW2uEKJwDvCCGuEJHMuCExxphx8FJNxmpARG8BKBRCLDF2LIwx1hzwsAVjjDHG6oR7HhhjjDFWJ9zzwBhjjLE64eSBMcYYY3XCyQNjjDHG6oSTB8YYY4zVCScPjDHGGKsTTh4YY4wxVif/Dxf9ODT1fbu+AAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 63,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:47:58.227Z",
          "iopub.execute_input": "2020-11-05T14:47:58.233Z",
          "iopub.status.idle": "2020-11-05T14:47:58.651Z",
          "shell.execute_reply": "2020-11-05T14:47:58.660Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# plotly:\n",
        "import plotly.express as px\n",
        "fig = px.bar(tmpdf3, x='mpi', y=sph_l, title='Weak scaling', labels={'value':'Walltime / s'}) # , color=\"continent\", line_group=\"country\")\n",
        "# fig = px.bar(long_df, x=\"nation\", y=\"count\", color=\"medal\", title=\"Long-Form Input\")\n",
        "fig.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=domain_distribute<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "domain_distribute",
                  "marker": {
                    "color": "#636efa"
                  },
                  "name": "domain_distribute",
                  "offsetgroup": "domain_distribute",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    2.5859,
                    2.8955,
                    3.1797,
                    3.0239,
                    3.5569,
                    4.1697,
                    6.6821,
                    7.2803,
                    10.3754
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=mpi_synchronizeHalos<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "mpi_synchronizeHalos",
                  "marker": {
                    "color": "#EF553B"
                  },
                  "name": "mpi_synchronizeHalos",
                  "offsetgroup": "mpi_synchronizeHalos",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    2.1741,
                    3.2091,
                    4.1907,
                    4.0796,
                    13.8668,
                    12.6808,
                    3.3354,
                    9.9729,
                    90.0528
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=BuildTree<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "BuildTree",
                  "marker": {
                    "color": "#00cc96"
                  },
                  "name": "BuildTree",
                  "offsetgroup": "BuildTree",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    1.9037,
                    2.0939,
                    3.097,
                    1.292,
                    1.9449,
                    2.5802,
                    2.7411,
                    3.3023,
                    4.1116
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=FindNeighbors<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "FindNeighbors",
                  "marker": {
                    "color": "#ab63fa"
                  },
                  "name": "FindNeighbors",
                  "offsetgroup": "FindNeighbors",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    4.0965,
                    4.2277,
                    4.2274,
                    4.1799,
                    4.3819,
                    4.3712,
                    5.3852,
                    5.4277,
                    5.4494
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=Density<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "Density",
                  "marker": {
                    "color": "#FFA15A"
                  },
                  "name": "Density",
                  "offsetgroup": "Density",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    2.4026,
                    2.4946,
                    2.5317,
                    2.5854,
                    2.4535,
                    2.5059,
                    2.4364,
                    2.5266,
                    2.5907
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=EquationOfState<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "EquationOfState",
                  "marker": {
                    "color": "#19d3f3"
                  },
                  "name": "EquationOfState",
                  "offsetgroup": "EquationOfState",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    0.008,
                    0.0081,
                    0.0082,
                    0.0082,
                    0.0085,
                    0.0082,
                    0.0082,
                    0.0082,
                    0.0087
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=IAD<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "IAD",
                  "marker": {
                    "color": "#FF6692"
                  },
                  "name": "IAD",
                  "offsetgroup": "IAD",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    3.2074,
                    3.274,
                    3.3898,
                    3.307,
                    3.3188,
                    3.3264,
                    3.2735,
                    3.3768,
                    3.0592
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=MomentumEnergyIAD<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "MomentumEnergyIAD",
                  "marker": {
                    "color": "#B6E880"
                  },
                  "name": "MomentumEnergyIAD",
                  "offsetgroup": "MomentumEnergyIAD",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    5.3977,
                    5.5122,
                    5.6364,
                    5.5877,
                    5.2044,
                    4.7544,
                    5.4943,
                    5.6284,
                    5.0892
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=Timestep<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "Timestep",
                  "marker": {
                    "color": "#FF97FF"
                  },
                  "name": "Timestep",
                  "offsetgroup": "Timestep",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    5.0018,
                    2.9154,
                    4.718,
                    2.5514,
                    9.7925,
                    4.6981,
                    32.192,
                    6.5853,
                    41.4034
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=UpdateQuantities<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "UpdateQuantities",
                  "marker": {
                    "color": "#FECB52"
                  },
                  "name": "UpdateQuantities",
                  "offsetgroup": "UpdateQuantities",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    0.1226,
                    0.1223,
                    0.1227,
                    0.1226,
                    0.122,
                    0.1209,
                    0.1194,
                    0.1242,
                    0.1247
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=EnergyConservation<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "EnergyConservation",
                  "marker": {
                    "color": "#636efa"
                  },
                  "name": "EnergyConservation",
                  "offsetgroup": "EnergyConservation",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    0.0241,
                    0.0249,
                    0.1599,
                    0.4183,
                    0.1208,
                    0.1905,
                    0.7143,
                    0.5084,
                    0.2202
                  ],
                  "yaxis": "y"
                },
                {
                  "alignmentgroup": "True",
                  "hovertemplate": "variable=SmoothingLength<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>",
                  "legendgroup": "SmoothingLength",
                  "marker": {
                    "color": "#EF553B"
                  },
                  "name": "SmoothingLength",
                  "offsetgroup": "SmoothingLength",
                  "orientation": "v",
                  "showlegend": true,
                  "textposition": "auto",
                  "type": "bar",
                  "x": [
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768
                  ],
                  "xaxis": "x",
                  "y": [
                    0.0348,
                    0.0352,
                    0.0358,
                    0.0358,
                    0.0348,
                    0.035,
                    0.035,
                    0.0349,
                    0.0364
                  ],
                  "yaxis": "y"
                }
              ],
              "layout": {
                "barmode": "relative",
                "legend": {
                  "title": {
                    "text": "variable"
                  },
                  "tracegroupgap": 0
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2dcontour"
                      }
                    ],
                    "mesh3d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "mesh3d"
                      }
                    ],
                    "parcoords": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "parcoords"
                      }
                    ],
                    "pie": [
                      {
                        "automargin": true,
                        "type": "pie"
                      }
                    ],
                    "scatter": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter"
                      }
                    ],
                    "scatter3d": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter3d"
                      }
                    ],
                    "scattercarpet": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattercarpet"
                      }
                    ],
                    "scattergeo": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergeo"
                      }
                    ],
                    "scattergl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergl"
                      }
                    ],
                    "scattermapbox": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattermapbox"
                      }
                    ],
                    "scatterpolar": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolar"
                      }
                    ],
                    "scatterpolargl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolargl"
                      }
                    ],
                    "scatterternary": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterternary"
                      }
                    ],
                    "surface": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "surface"
                      }
                    ],
                    "table": [
                      {
                        "cells": {
                          "fill": {
                            "color": "#EBF0F8"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "header": {
                          "fill": {
                            "color": "#C8D4E3"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "type": "table"
                      }
                    ]
                  },
                  "layout": {
                    "annotationdefaults": {
                      "arrowcolor": "#2a3f5f",
                      "arrowhead": 0,
                      "arrowwidth": 1
                    },
                    "coloraxis": {
                      "colorbar": {
                        "outlinewidth": 0,
                        "ticks": ""
                      }
                    },
                    "colorscale": {
                      "diverging": [
                        [
                          0,
                          "#8e0152"
                        ],
                        [
                          0.1,
                          "#c51b7d"
                        ],
                        [
                          0.2,
                          "#de77ae"
                        ],
                        [
                          0.3,
                          "#f1b6da"
                        ],
                        [
                          0.4,
                          "#fde0ef"
                        ],
                        [
                          0.5,
                          "#f7f7f7"
                        ],
                        [
                          0.6,
                          "#e6f5d0"
                        ],
                        [
                          0.7,
                          "#b8e186"
                        ],
                        [
                          0.8,
                          "#7fbc41"
                        ],
                        [
                          0.9,
                          "#4d9221"
                        ],
                        [
                          1,
                          "#276419"
                        ]
                      ],
                      "sequential": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ],
                      "sequentialminus": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ]
                    },
                    "colorway": [
                      "#636efa",
                      "#EF553B",
                      "#00cc96",
                      "#ab63fa",
                      "#FFA15A",
                      "#19d3f3",
                      "#FF6692",
                      "#B6E880",
                      "#FF97FF",
                      "#FECB52"
                    ],
                    "font": {
                      "color": "#2a3f5f"
                    },
                    "geo": {
                      "bgcolor": "white",
                      "lakecolor": "white",
                      "landcolor": "#E5ECF6",
                      "showlakes": true,
                      "showland": true,
                      "subunitcolor": "white"
                    },
                    "hoverlabel": {
                      "align": "left"
                    },
                    "hovermode": "closest",
                    "mapbox": {
                      "style": "light"
                    },
                    "paper_bgcolor": "white",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                      "angularaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "radialaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "scene": {
                      "xaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "yaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "zaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      }
                    },
                    "shapedefaults": {
                      "line": {
                        "color": "#2a3f5f"
                      }
                    },
                    "ternary": {
                      "aaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "baxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "caxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "title": {
                      "x": 0.05
                    },
                    "xaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    },
                    "yaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    }
                  }
                },
                "title": {
                  "text": "Weak scaling"
                },
                "xaxis": {
                  "anchor": "y",
                  "domain": [
                    0,
                    1
                  ],
                  "title": {
                    "text": "mpi"
                  }
                },
                "yaxis": {
                  "anchor": "x",
                  "domain": [
                    0,
                    1
                  ],
                  "title": {
                    "text": "Walltime / s"
                  }
                }
              }
            },
            "text/html": "<div>                            <div id=\"284801a3-cf60-4149-ad8a-cfb2a3e276fa\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"284801a3-cf60-4149-ad8a-cfb2a3e276fa\")) {                    Plotly.newPlot(                        \"284801a3-cf60-4149-ad8a-cfb2a3e276fa\",                        [{\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=domain_distribute<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"domain_distribute\", \"marker\": {\"color\": \"#636efa\"}, \"name\": \"domain_distribute\", \"offsetgroup\": \"domain_distribute\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [2.5859, 2.8955, 3.1797, 3.0239, 3.5569, 4.1697, 6.6821, 7.2803, 10.3754], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=mpi_synchronizeHalos<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"mpi_synchronizeHalos\", \"marker\": {\"color\": \"#EF553B\"}, \"name\": \"mpi_synchronizeHalos\", \"offsetgroup\": \"mpi_synchronizeHalos\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [2.1741, 3.2091, 4.1907, 4.0796, 13.8668, 12.6808, 3.3354, 9.9729, 90.0528], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=BuildTree<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"BuildTree\", \"marker\": {\"color\": \"#00cc96\"}, \"name\": \"BuildTree\", \"offsetgroup\": \"BuildTree\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [1.9037, 2.0939, 3.097, 1.292, 1.9449, 2.5802, 2.7411, 3.3023, 4.1116], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=FindNeighbors<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"FindNeighbors\", \"marker\": {\"color\": \"#ab63fa\"}, \"name\": \"FindNeighbors\", \"offsetgroup\": \"FindNeighbors\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [4.0965, 4.2277, 4.2274, 4.1799, 4.3819, 4.3712, 5.3852, 5.4277, 5.4494], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=Density<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"Density\", \"marker\": {\"color\": \"#FFA15A\"}, \"name\": \"Density\", \"offsetgroup\": \"Density\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [2.4026, 2.4946, 2.5317, 2.5854, 2.4535, 2.5059, 2.4364, 2.5266, 2.5907], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=EquationOfState<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"EquationOfState\", \"marker\": {\"color\": \"#19d3f3\"}, \"name\": \"EquationOfState\", \"offsetgroup\": \"EquationOfState\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [0.008, 0.0081, 0.0082, 0.0082, 0.0085, 0.0082, 0.0082, 0.0082, 0.0087], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=IAD<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"IAD\", \"marker\": {\"color\": \"#FF6692\"}, \"name\": \"IAD\", \"offsetgroup\": \"IAD\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [3.2074, 3.274, 3.3898, 3.307, 3.3188, 3.3264, 3.2735, 3.3768, 3.0592], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=MomentumEnergyIAD<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"MomentumEnergyIAD\", \"marker\": {\"color\": \"#B6E880\"}, \"name\": \"MomentumEnergyIAD\", \"offsetgroup\": \"MomentumEnergyIAD\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [5.3977, 5.5122, 5.6364, 5.5877, 5.2044, 4.7544, 5.4943, 5.6284, 5.0892], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=Timestep<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"Timestep\", \"marker\": {\"color\": \"#FF97FF\"}, \"name\": \"Timestep\", \"offsetgroup\": \"Timestep\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [5.0018, 2.9154, 4.718, 2.5514, 9.7925, 4.6981, 32.192, 6.5853, 41.4034], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=UpdateQuantities<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"UpdateQuantities\", \"marker\": {\"color\": \"#FECB52\"}, \"name\": \"UpdateQuantities\", \"offsetgroup\": \"UpdateQuantities\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [0.1226, 0.1223, 0.1227, 0.1226, 0.122, 0.1209, 0.1194, 0.1242, 0.1247], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=EnergyConservation<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"EnergyConservation\", \"marker\": {\"color\": \"#636efa\"}, \"name\": \"EnergyConservation\", \"offsetgroup\": \"EnergyConservation\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [0.0241, 0.0249, 0.1599, 0.4183, 0.1208, 0.1905, 0.7143, 0.5084, 0.2202], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hovertemplate\": \"variable=SmoothingLength<br>mpi=%{x}<br>Walltime / s=%{y}<extra></extra>\", \"legendgroup\": \"SmoothingLength\", \"marker\": {\"color\": \"#EF553B\"}, \"name\": \"SmoothingLength\", \"offsetgroup\": \"SmoothingLength\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768], \"xaxis\": \"x\", \"y\": [0.0348, 0.0352, 0.0358, 0.0358, 0.0348, 0.035, 0.035, 0.0349, 0.0364], \"yaxis\": \"y\"}],                        {\"barmode\": \"relative\", \"legend\": {\"title\": {\"text\": \"variable\"}, \"tracegroupgap\": 0}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"Weak scaling\"}, \"xaxis\": {\"anchor\": \"y\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"mpi\"}}, \"yaxis\": {\"anchor\": \"x\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"Walltime / s\"}}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('284801a3-cf60-4149-ad8a-cfb2a3e276fa');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 90,
      "metadata": {
        "collapsed": false,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:35:17.204Z",
          "iopub.execute_input": "2020-11-05T15:35:17.213Z",
          "iopub.status.idle": "2020-11-05T15:35:17.320Z",
          "shell.execute_reply": "2020-11-05T15:35:17.325Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "type(tmpdf3['mpi'])"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 94,
          "data": {
            "text/plain": "pandas.core.series.Series"
          },
          "metadata": {}
        }
      ],
      "execution_count": 94,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:40:28.883Z",
          "iopub.execute_input": "2020-11-05T15:40:28.893Z",
          "iopub.status.idle": "2020-11-05T15:40:28.912Z",
          "shell.execute_reply": "2020-11-05T15:40:28.921Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf3['mpi']"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 95,
          "data": {
            "text/plain": "0      128\n1      256\n2      512\n3     1024\n4     2048\n5     4096\n6     8192\n7    16384\n8    32768\nName: mpi, dtype: int64"
          },
          "metadata": {}
        }
      ],
      "execution_count": 95,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:41:02.326Z",
          "iopub.execute_input": "2020-11-05T15:41:02.336Z",
          "iopub.status.idle": "2020-11-05T15:41:02.356Z",
          "shell.execute_reply": "2020-11-05T15:41:02.363Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        " tmpdf3['IAD']"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 157,
          "data": {
            "text/plain": "0    3.2074\n1    3.2740\n2    3.3898\n3    3.3070\n4    3.3188\n5    3.3264\n6    3.2735\n7    3.3768\n8    3.0592\nName: IAD, dtype: float64"
          },
          "metadata": {}
        }
      ],
      "execution_count": 157,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T16:18:48.833Z",
          "iopub.execute_input": "2020-11-05T16:18:48.843Z",
          "iopub.status.idle": "2020-11-05T16:18:48.864Z",
          "shell.execute_reply": "2020-11-05T16:18:48.873Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# ---- OK ----\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "# must convert pandas df into a list of str:\n",
        "labels = list(map(str, tmpdf3['mpi'].tolist())) # same as  ['128', '256', ...]\n",
        "# men_means = [20, 35, 30, 35, 27]\n",
        "# men_means = tmpdf3['IAD']  # same as tmpdf3['IAD'].tolist()\n",
        "# print(f'labels={type(labels)}, {labels}')\n",
        "# print(f'men_means={type(men_means)}, {type(men_means)}')\n",
        "width = 0.35  # the width of the bars: can also be len(x) sequence\n",
        "fig, ax = plt.subplots()\n",
        "voffset = 0\n",
        "# ax.bar(labels, tmpdf3['domain_distribute'], width, label='domain_distribute'); voffset += tmpdf3['domain_distribute']\n",
        "# ax.bar(labels, tmpdf3['mpi_synchronizeHalos'], width, label='mpi_synchronizeHalos', bottom=voffset); voffset += tmpdf3['mpi_synchronizeHalos']\n",
        "ll = 'domain_distribute'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'mpi_synchronizeHalos'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'BuildTree'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'FindNeighbors'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'Density'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'EquationOfState'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'IAD'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'MomentumEnergyIAD'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'Timestep'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'UpdateQuantities'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'EnergyConservation'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "ll = 'SmoothingLength'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "# ll = ''; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "# ['domain_distribute', 'mpi_synchronizeHalos',\t'BuildTree', 'FindNeighbors', 'Density', 'EquationOfState', 'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities', 'EnergyConservation', 'SmoothingLength']\n",
        "ax.set_xlabel('# of cores')\n",
        "ax.set_ylabel('Elapsed / s')\n",
        "ax.set_title('AMD: Weak scaling: sedov test (PrgEnv-cray, -s 1)')\n",
        "# ax.legend()\n",
        "leg_handles, leg_labels = ax.get_legend_handles_labels()\n",
        "plt.legend(reversed(leg_handles), reversed(leg_labels), bbox_to_anchor=(1.0, 1.0), loc='upper left')\n",
        "\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 185,
      "metadata": {
        "collapsed": false,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T17:02:21.972Z",
          "iopub.execute_input": "2020-11-05T17:02:22.120Z",
          "iopub.status.idle": "2020-11-05T17:02:22.465Z",
          "shell.execute_reply": "2020-11-05T17:02:22.487Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# type(tmpdf3['Timestep'])\n",
        "tmpdf3['Timestep'], tmpdf3['Timestep'].value_counts(normalize=True)"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 192,
          "data": {
            "text/plain": "(0     5.0018\n 1     2.9154\n 2     4.7180\n 3     2.5514\n 4     9.7925\n 5     4.6981\n 6    32.1920\n 7     6.5853\n 8    41.4034\n Name: Timestep, dtype: float64,\n 32.1920    0.111111\n 2.5514     0.111111\n 2.9154     0.111111\n 4.6981     0.111111\n 41.4034    0.111111\n 9.7925     0.111111\n 5.0018     0.111111\n 4.7180     0.111111\n 6.5853     0.111111\n Name: Timestep, dtype: float64)"
          },
          "metadata": {}
        }
      ],
      "execution_count": 192,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T17:52:05.627Z",
          "iopub.execute_input": "2020-11-05T17:52:05.641Z",
          "iopub.status.idle": "2020-11-05T17:52:05.662Z",
          "shell.execute_reply": "2020-11-05T17:52:05.672Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf2.transpose()"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 199,
          "data": {
            "text/plain": "                           0       1       2       3        4        5  \\\ndomain_distribute     2.5859  2.8955  3.1797  3.0239   3.5569   4.1697   \nmpi_synchronizeHalos  2.1741  3.2091  4.1907  4.0796  13.8668  12.6808   \nBuildTree             1.9037  2.0939  3.0970  1.2920   1.9449   2.5802   \nFindNeighbors         4.0965  4.2277  4.2274  4.1799   4.3819   4.3712   \nDensity               2.4026  2.4946  2.5317  2.5854   2.4535   2.5059   \nEquationOfState       0.0080  0.0081  0.0082  0.0082   0.0085   0.0082   \nIAD                   3.2074  3.2740  3.3898  3.3070   3.3188   3.3264   \nMomentumEnergyIAD     5.3977  5.5122  5.6364  5.5877   5.2044   4.7544   \nTimestep              5.0018  2.9154  4.7180  2.5514   9.7925   4.6981   \nUpdateQuantities      0.1226  0.1223  0.1227  0.1226   0.1220   0.1209   \nEnergyConservation    0.0241  0.0249  0.1599  0.4183   0.1208   0.1905   \nSmoothingLength       0.0348  0.0352  0.0358  0.0358   0.0348   0.0350   \n\n                            6       7        8  \ndomain_distribute      6.6821  7.2803  10.3754  \nmpi_synchronizeHalos   3.3354  9.9729  90.0528  \nBuildTree              2.7411  3.3023   4.1116  \nFindNeighbors          5.3852  5.4277   5.4494  \nDensity                2.4364  2.5266   2.5907  \nEquationOfState        0.0082  0.0082   0.0087  \nIAD                    3.2735  3.3768   3.0592  \nMomentumEnergyIAD      5.4943  5.6284   5.0892  \nTimestep              32.1920  6.5853  41.4034  \nUpdateQuantities       0.1194  0.1242   0.1247  \nEnergyConservation     0.7143  0.5084   0.2202  \nSmoothingLength        0.0350  0.0349   0.0364  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>0</th>\n      <th>1</th>\n      <th>2</th>\n      <th>3</th>\n      <th>4</th>\n      <th>5</th>\n      <th>6</th>\n      <th>7</th>\n      <th>8</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>domain_distribute</th>\n      <td>2.5859</td>\n      <td>2.8955</td>\n      <td>3.1797</td>\n      <td>3.0239</td>\n      <td>3.5569</td>\n      <td>4.1697</td>\n      <td>6.6821</td>\n      <td>7.2803</td>\n      <td>10.3754</td>\n    </tr>\n    <tr>\n      <th>mpi_synchronizeHalos</th>\n      <td>2.1741</td>\n      <td>3.2091</td>\n      <td>4.1907</td>\n      <td>4.0796</td>\n      <td>13.8668</td>\n      <td>12.6808</td>\n      <td>3.3354</td>\n      <td>9.9729</td>\n      <td>90.0528</td>\n    </tr>\n    <tr>\n      <th>BuildTree</th>\n      <td>1.9037</td>\n      <td>2.0939</td>\n      <td>3.0970</td>\n      <td>1.2920</td>\n      <td>1.9449</td>\n      <td>2.5802</td>\n      <td>2.7411</td>\n      <td>3.3023</td>\n      <td>4.1116</td>\n    </tr>\n    <tr>\n      <th>FindNeighbors</th>\n      <td>4.0965</td>\n      <td>4.2277</td>\n      <td>4.2274</td>\n      <td>4.1799</td>\n      <td>4.3819</td>\n      <td>4.3712</td>\n      <td>5.3852</td>\n      <td>5.4277</td>\n      <td>5.4494</td>\n    </tr>\n    <tr>\n      <th>Density</th>\n      <td>2.4026</td>\n      <td>2.4946</td>\n      <td>2.5317</td>\n      <td>2.5854</td>\n      <td>2.4535</td>\n      <td>2.5059</td>\n      <td>2.4364</td>\n      <td>2.5266</td>\n      <td>2.5907</td>\n    </tr>\n    <tr>\n      <th>EquationOfState</th>\n      <td>0.0080</td>\n      <td>0.0081</td>\n      <td>0.0082</td>\n      <td>0.0082</td>\n      <td>0.0085</td>\n      <td>0.0082</td>\n      <td>0.0082</td>\n      <td>0.0082</td>\n      <td>0.0087</td>\n    </tr>\n    <tr>\n      <th>IAD</th>\n      <td>3.2074</td>\n      <td>3.2740</td>\n      <td>3.3898</td>\n      <td>3.3070</td>\n      <td>3.3188</td>\n      <td>3.3264</td>\n      <td>3.2735</td>\n      <td>3.3768</td>\n      <td>3.0592</td>\n    </tr>\n    <tr>\n      <th>MomentumEnergyIAD</th>\n      <td>5.3977</td>\n      <td>5.5122</td>\n      <td>5.6364</td>\n      <td>5.5877</td>\n      <td>5.2044</td>\n      <td>4.7544</td>\n      <td>5.4943</td>\n      <td>5.6284</td>\n      <td>5.0892</td>\n    </tr>\n    <tr>\n      <th>Timestep</th>\n      <td>5.0018</td>\n      <td>2.9154</td>\n      <td>4.7180</td>\n      <td>2.5514</td>\n      <td>9.7925</td>\n      <td>4.6981</td>\n      <td>32.1920</td>\n      <td>6.5853</td>\n      <td>41.4034</td>\n    </tr>\n    <tr>\n      <th>UpdateQuantities</th>\n      <td>0.1226</td>\n      <td>0.1223</td>\n      <td>0.1227</td>\n      <td>0.1226</td>\n      <td>0.1220</td>\n      <td>0.1209</td>\n      <td>0.1194</td>\n      <td>0.1242</td>\n      <td>0.1247</td>\n    </tr>\n    <tr>\n      <th>EnergyConservation</th>\n      <td>0.0241</td>\n      <td>0.0249</td>\n      <td>0.1599</td>\n      <td>0.4183</td>\n      <td>0.1208</td>\n      <td>0.1905</td>\n      <td>0.7143</td>\n      <td>0.5084</td>\n      <td>0.2202</td>\n    </tr>\n    <tr>\n      <th>SmoothingLength</th>\n      <td>0.0348</td>\n      <td>0.0352</td>\n      <td>0.0358</td>\n      <td>0.0358</td>\n      <td>0.0348</td>\n      <td>0.0350</td>\n      <td>0.0350</td>\n      <td>0.0349</td>\n      <td>0.0364</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 199,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T20:19:31.279Z",
          "iopub.execute_input": "2020-11-05T20:19:31.292Z",
          "iopub.status.idle": "2020-11-05T20:19:31.317Z",
          "shell.execute_reply": "2020-11-05T20:19:31.328Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# --- % stacked bar ---\n",
        "# tmpdf2T = tmpdf2.transpose()\n",
        "np = tmpdf2.to_numpy()\n",
        "np_pct = np  # tmpdf2.to_numpy()\n",
        "\n",
        "i=0\n",
        "print(np[i])\n",
        "print(sum(np[i]))\n",
        "print(np[i])\n",
        "\n",
        "for i in range(len(np)):\n",
        "  s = sum(np[i])\n",
        "  np_pct[i] = np[i] / s * 100\n",
        "  # print(f'{i}, {np[i]}, {np_pct[i]}\\n')\n",
        "  # print(f'{i}, {np[i]}, s={s},  {np[i]/s*100}\\n')\n",
        "  # print(f'{i}, {np[i]}, {np_pct[i]}\\n')\n",
        "\n",
        "# print(f'{i-1}, {np[i-1]}, {np_pct[i-1]}\\n')\n",
        "# print(f'{i}, {type(np[i])} {np[i].size} {np[i].ndim} {np_pct[i]}\\n')\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "# must convert pandas df into a list of str:\n",
        "### labels = list(map(str, tmpdf3['mpi'].tolist())) # same as  ['128', '256', ...]\n",
        "labels = ['a']\n",
        "width = 0.35  # the width of the bars: can also be len(x) sequence\n",
        "fig, ax = plt.subplots()\n",
        "voffset = 0\n",
        "ll = 'domain_distribute'; ax.bar(labels, np_pct[0], width, label=ll, bottom=voffset); voffset += np_pct[0]\n",
        "ll = 'mpi_synchronizeHalos'; ax.bar(labels, np_pct[1], width, label=ll, bottom=voffset); voffset += np_pct[1]\n",
        "ll = 'BuildTree'; ax.bar(labels, np_pct[2], width, label=ll, bottom=voffset); voffset += np_pct[2]\n",
        "#ll = 'FindNeighbors'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'Density'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'EquationOfState'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'IAD'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'MomentumEnergyIAD'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'Timestep'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'UpdateQuantities'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'EnergyConservation'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "#ll = 'SmoothingLength'; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "# ll = ''; ax.bar(labels, tmpdf3[ll], width, label=ll, bottom=voffset); voffset += tmpdf3[ll]\n",
        "\n",
        "# ['domain_distribute', 'mpi_synchronizeHalos',\t'BuildTree', 'FindNeighbors', 'Density', 'EquationOfState', 'IAD', 'MomentumEnergyIAD', 'Timestep', 'UpdateQuantities', 'EnergyConservation', 'SmoothingLength']\n",
        "ax.set_xlabel('# of cores')\n",
        "ax.set_ylabel('Elapsed / s')\n",
        "ax.set_title('AMD: Weak scaling: sedov test (PrgEnv-cray, -s 1)')\n",
        "# ax.legend()\n",
        "leg_handles, leg_labels = ax.get_legend_handles_labels()\n",
        "plt.legend(reversed(leg_handles), reversed(leg_labels), bbox_to_anchor=(1.0, 1.0), loc='upper left')\n",
        "\n",
        "plt.show()  "
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[ 9.59190184  8.06440844  7.06141132 15.19518383  8.91198552  0.02967447\n",
            " 11.89723731 20.02173655 18.55322116  0.45476127  0.08939434  0.12908395]\n",
            "100.0\n",
            "[ 9.59190184  8.06440844  7.06141132 15.19518383  8.91198552  0.02967447\n",
            " 11.89723731 20.02173655 18.55322116  0.45476127  0.08939434  0.12908395]\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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cfsfAx+Hdz2E4M6BfYFPzawNQPi/wiYVERGJiwQlFnKkws9QpTlE3JKL8HbmH5lZZjjrdILbSU8juP054X/dL0JEROQoEu+LaN0CTDaz+sA6YAxBQvOCmV0LfAhcGucYRESkEr2e6pUby/qWjl664GBlEhMTc7t27Vro7iQmJvpvf/vbDWecccbeqta57LLLOv7whz/8NDc3d3+7du165eXlrWjTpk1xZJnx48e3TUlJKfnggw8azJ8/P6WoqMg2btzYID09fT/AHXfcsWnMmDHbj+wZSjTimly4+yKgXwWLTo/ndiP1eqpXdW1KRCSmlo5eWtMhxEWDBg1KV65cuRzgxRdfbPzjH/+4/RlnnLGqqnWmTJkS9dVGn3nmmQ0Aq1atqn/eeed1LdtWmaKiIurVq3c4oUuUdBqSiIjUmJ07dyY2adKkGGD69OmpQ4cOzShbNmrUqA4TJkxoAdC/f//MuXPnNiq//h133NE6PT29Z25ububq1asbVLad6dOnp+bm5mYOGzYso2vXrj2Li4u58cYb2/fs2bN7t27devz6179uWVb2Jz/5Sauy+d///vfbxvYZHxvqxL1FRETk6HHgwIGErKysHgcOHLCtW7fWmzFjxvuHU8+8efMavfTSS82XLl26vKioiBNPPLFHnz599lVWfvny5Y0WLlyYn5WV9fmDDz7YskmTJiXLli1bUVhYaCeddFLW+eefv2v58uXJa9asSV6yZMkKd2f48OEZr776asrZZ5+95/Cf8bFHyYWIiFSryG6R119//bgxY8Z0ev/99/MPtZ633nor5ZxzztmRmppaCnDmmWfuqKp8796992ZlZX0ebrfxypUrG02bNq0ZwO7duxOXL1+ePHPmzMZz585t3KNHjx4A+/btS1i5cmWykotDo+RCRERqzPDhw/du3749adOmTUn16tXz0tLSL5YdOHDAYrmtRo0afVG5u9tDDz20YeTIkbsiy7z66quNb7311k0/+MEPtsZy28cajbkQEZEas3DhwuTS0lJatWpV3KVLlwNr1qxpWFhYaFu3bk18++23G1e17rBhw/bMmDGj6Z49e2z79u0Js2bNahrtds8444ydjz76aFpZArNkyZIGu3btSjj77LN3PfPMMy137tyZAPDBBx/U27hxow7ED5FeMBGRY1g0p47GWtmYCwB359FHH12flJRERkZG0fnnn789Kysru3379geys7MrHT8BMGjQoH0jRozY1rNnz+wWLVoU9e7du8rTWSN9//vf37p+/foGvXr16u7u1rx586IZM2as/da3vrUrPz8/+aSTTsqCoLVj8uTJH7Rr1674YHXKlyy4Anft1q9fP8/LyzusdXUqqojUVUd6KqqZLXD3r1wOYPHixetzcnLU5C9HbPHixS1zcnLSK1qmbhERERGJKSUXIiIiElNKLkRERCSmlFyIiIhITCm5EBERkZhSciEiIiIxpetciIgcy+5pEtNbrnPPzmq/bobUPmq5EBGROmP9+vX1zjrrrM41se0JEya0GDVqVId41H3rrbe2ffnll1MPdb3x48e3vfvuu1tFzmvXrl2vTZs2Vdl4EE2ZI6GWCxERqTPS09OLZs6cua6m46hKcXExSUmHtnv9zW9+80mcwqkRarkQEZFqtWrVqvqdOnXKHjlyZHp6enrPCy64oNPLL7+c2rdv36yOHTv2fOuttxqNHz++7UUXXdTpxBNPzOrYsWPPhx56qGXZul27ds2urO68vLzkXr16dc/KyurRrVu3HkuXLm1w6623tv35z39+fFmZW265pd299957/PTp01P79++fedZZZ3Xu1KlT9gUXXNCp7MZpc+bMadSnT5+szMzMHr169eq+ffv2BICCgoJ6gwcP7tqxY8eeN910U/uyOhs1atTn+uuvb5+ZmdnjjTfeSLnnnntade3aNbtr167ZZdtetWpV/c6dO2dffvnlHTMyMrJPOeWUrnv27DGAkSNHpk+aNKnZ3LlzG2VlZfUoi9/McgHy8/MbDB48uGt2dnb33NzczIULFyZH81oPHz68S3Z2dveMjIzsBx98sGVFZSqKddeuXQmnnXZaRmZmZo+uXbtmP/bYY82i2V4ZtVyIiEi1++ijj5KnTJmyLjc3d33v3r27T548uUVeXt7K5557rul9993Xpnfv3oUrVqxouGDBghW7d+9O7NOnT4+RI0fuPFi9v/vd79JuvvnmT8eOHbtt//79VlxczNixY7eOGDGiy9133725pKSEl19+udn8+fNX5OXlNVqxYkXDRYsWrUtPTy/Kzc3NmjVrVsqQIUP2XnnllV0mT568dsiQIfu2bduWkJKSUgqwfPnyRosXL17esGHD0oyMjJ633377pxkZGUWFhYUJ3/jGN/Y+9thjH8+bN6/Rc88912LBggUr3J3c3Nzup59++u6WLVuWbNiwIfnZZ59dN3DgwA/POeeczk8//XSzm2++eVtZ/Keeeuq+stvR33jjje2HDh26C+C6667rOHHixA979ep14M033zxu7NixHd599933Af74xz+2euGFF1qU1bF58+Z6ZY8nT568vlWrViV79uyxPn369PjOd76zvXXr1iVlyyuLdfXq1Q1at25dNHv27DUAn332WeKhvL9quRARkWrXrl27A/379y9MTEykW7duhcOGDduVkJBA375993388ccNAM4+++wdKSkp3qZNm+IBAwbsmjdv3nEHq3fAgAF7H3rooTZ33XVX69WrV9dPSUnxzMzMz5s2bVr8r3/9q+FLL73UODs7e1/ZDrZXr157u3TpUpSYmEh2dva+tWvX1l+yZEny8ccfXzRkyJB9AM2bNy+tVy/YXw8aNGhXixYtSho1auQZGRn7165d2wAgMTGRq6++ejvA7NmzU84555wdjRs3Lm3SpEnpueeeu/2tt95KLXveAwcOLATo06fPvvXr1zeo6Hk89thjzZYsWdLo97///cc7d+5MWLhwYcoll1zSJSsrq8fNN9/cMTKBuOmmmz5duXLl8rK/448/vqhs2QMPPNAqMzOzR25ubveCgoJ6+fn5X2nxqCzWvn37Fs6bN6/x2LFj282cOTOlRYsWJRwCJRciIlLt6tev/8VdMxMSEkhOTnYIdtIlJSUGYGZfWaf8dEVuuummbVOnTl3TsGHD0vPOO6/rtGnTUgHGjBmz9fHHH285adKklmPGjPmsrHyDBg2+iCMxMZHi4uIqNxIZd2JiohcVFVk4vzSacRbl169oe/Pnz0/+5S9/2fbFF19cl5SURElJCampqcWRCcS6devyD7at6dOnp86ZMyc1Ly9v5apVq5Z37969sLCwMKr9fu/evQ/897//Xd6rV6/Cn/zkJ+1uv/32NtGsV0bdIiIix7JafOroq6++2vS+++7btGvXroR333039ZFHHtl44MCBKnf+y5cvr9+9e/cD2dnZmzds2FB/0aJFDS+44ILdV1111Y777ruvXXFxsY0cObLKAaG9e/fev3nz5npz5sxpNGTIkH3bt2//olskGkOHDt1zzTXXpN97770F7s6MGTOaPfnkk1ENQt26dWvilVde2XnSpEkftG3bthiClpP27dt//uc//7nZ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L29lampqaf/+/TMLCwu/1jJfv379L9ZNTEz0isocivvvv7/goosu2jl16tQmgwcPznrllVdWV1SuUaNGld6u3cy+Np2UlOSlpV+usn///grjdHfLyMgoXLRo0crDewbxo+RCROQYVt2njg4bNmzPNddck/6LX/xiU1FRkc2aNavp6NGjtzRu3Lhk5syZKWedddaeJ554osWAAQP2RFvnjh07Eps0aVKSmppaunDhwuSyrpbD1bJly5LU1NSS1157LeWb3/zmnieffLLCAZr5+fkN+vfvX9i/f//CBQsWNFq2bFlyenr653v27In67JS333678aeffpp43HHHlc6YMaPp448/vr59+/bF27ZtSyooKEhs0qRJ6Wuvvdbk9NNP3wWQkpJSsnPnzkSA3r1779+2bVvS66+/ftzw4cP3HjhwwJYuXdqgX79++4/k+ceCkgsREak2gwYN2jdixIhtPXv2zG7RokVR79699wJMmjTpg7Fjx3YcN25cQocOHQ48//zz66Otc+TIkTsnTpyY1rlz5+zOnTvvz8nJ2Xvwtar2xBNPrL/uuuvSzYzTTjttV0Vl/vd///f4d955p7GZeWZmZuHFF1+8MyEhgcTERM/MzOzx7W9/e2uzZs2qPFOld+/eey+44IIuBQUF9S+++OLPTj311H0At91226aTTjqpe6tWrYoyMjK+SBZGjRq19ZZbbun4gx/8oDQvL2/FX/7yl7Xjxo3rsHv37sSSkhIbO3bsp7UhubDgUhO1W79+/TwvL++w1u31VK8YRyMiUj2Wjj6yG3ma2YKIWy8AsHjx4vU5OTlbj6hiEWDx4sUtc3Jy0itaVhOX/xYREZGjmLpFRETkmHXVVVd1mD9/fkrkvLFjx376ve9977OaiulooORCROTYUlpaWmoJCQm1v0+8GjzzzDMbajqGuqi0tNSASs+CUbeIiMixZdmWLVuahDsHkUNWWlpqW7ZsaUJw1e0KqeVCROQYUlxcfF1BQcHjBQUFPdEBphyeUmBZcXHxdZUVUHIhInIMyc3N3QxcUNNxyNFNWauIiIjElJILERERiSklFyIiIhJTSi5EREQkppRciIiISEwpuRAREZGYUnIhIiIiMaXkQkRERGJKyYWIiIjElJILERERiSklFyIiIhJTSi5EREQkppRciIiISEwpuRAREZGYUnIhIiIiMaXkQkRE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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 262,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T21:22:17.268Z",
          "iopub.execute_input": "2020-11-05T21:22:17.282Z",
          "iopub.status.idle": "2020-11-05T21:22:17.448Z",
          "shell.execute_reply": "2020-11-05T21:22:17.460Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tmpdf2.transpose().value_counts(normalize=True)"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 206,
          "data": {
            "text/plain": "0       1       2       3       4        5        6        7       8      \n5.3977  5.5122  5.6364  5.5877  5.2044   4.7544   5.4943   5.6284  5.0892     0.083333\n5.0018  2.9154  4.7180  2.5514  9.7925   4.6981   32.1920  6.5853  41.4034    0.083333\n4.0965  4.2277  4.2274  4.1799  4.3819   4.3712   5.3852   5.4277  5.4494     0.083333\n3.2074  3.2740  3.3898  3.3070  3.3188   3.3264   3.2735   3.3768  3.0592     0.083333\n2.5859  2.8955  3.1797  3.0239  3.5569   4.1697   6.6821   7.2803  10.3754    0.083333\n2.4026  2.4946  2.5317  2.5854  2.4535   2.5059   2.4364   2.5266  2.5907     0.083333\n2.1741  3.2091  4.1907  4.0796  13.8668  12.6808  3.3354   9.9729  90.0528    0.083333\n1.9037  2.0939  3.0970  1.2920  1.9449   2.5802   2.7411   3.3023  4.1116     0.083333\n0.1226  0.1223  0.1227  0.1226  0.1220   0.1209   0.1194   0.1242  0.1247     0.083333\n0.0348  0.0352  0.0358  0.0358  0.0348   0.0350   0.0350   0.0349  0.0364     0.083333\n0.0241  0.0249  0.1599  0.4183  0.1208   0.1905   0.7143   0.5084  0.2202     0.083333\n0.0080  0.0081  0.0082  0.0082  0.0085   0.0082   0.0082   0.0082  0.0087     0.083333\ndtype: float64"
          },
          "metadata": {}
        }
      ],
      "execution_count": 206,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T20:20:58.360Z",
          "iopub.execute_input": "2020-11-05T20:20:58.370Z",
          "iopub.status.idle": "2020-11-05T20:20:58.393Z",
          "shell.execute_reply": "2020-11-05T20:20:58.404Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "labels = ['G1', 'G2', 'G3', 'G4', 'G5']\n",
        "men_means = [20, 35, 30, 35, 27]\n",
        "women_means = [25, 32, 34, 20, 25]\n",
        "# men_std = [2, 3, 4, 1, 2]\n",
        "# women_std = [3, 5, 2, 3, 3]\n",
        "width = 0.35       # the width of the bars: can also be len(x) sequence\n",
        "fig, ax = plt.subplots()\n",
        "ax.bar(labels, men_means, width, label='Men')\n",
        "ax.bar(labels, men_means, width, label='Women', bottom=men_means)\n",
        "# ax.bar(labels, men_means, width, yerr=men_std, label='Men')\n",
        "# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,\n",
        "#        label='Women')\n",
        "ax.set_ylabel('Scores')\n",
        "ax.set_title('Scores by group and gender')\n",
        "ax.legend()\n",
        "plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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DQRIP5v9LoyZmX1wnXLKKW9Nmzat/5o1azRv3rzeH/vYx1Y3zrvwwgsHHnzwwSufeeaZeQ8++OCCb37zm4NXrlzZDWDu3Lm9b7nllufnzZs3Z8aMGf0XLly4VTnrLkdonsTfD80CzAAmpuGJdM0HAZuZdWn77rvv2ldeeWXrX/7yl9sddthh7zk+f999921z2WWXDRwxYsSo8ePH775u3TotXLiwB8D48eNXbr/99ht79+4dw4YN+9uiRYu2LmfdhZ7TlNQH+DjZ0+IbXQxcJ+k04EXghCJrMDOzjumII45YftFFFw254447FixbtmxTHkUEN9xww8IxY8asK11+5syZfXr06LHplF737t1j/fr1KmfNhfY0I2J1RGwfEStKpr0ZEYdGxPCIOCwi3mptG2Zm9sF05plnvnHuuee+Om7cuLWl0w8++OCVl1566YCGhgYAHnrooV4VKbAZvo2emVkXlucrIkXZdddd13/zm99833UtF1988auTJk2qGTFixKiGhgYNGTJkXUf5KopD08zMymrNmjVPNp121FFHvXPUUUe9A9C3b9+45ppr3vcA7bPPPvtN4M3G8UoEqe89a2ZmlpND08zMLCeHppmZWU4OTTMzs5wcmmZmZjk5NM3MzHLyV07MzLqyyf3a9dFgTF7R6vc+TzvttCFDhw5d9+1vf3sZwPjx44cPGjTo3WnTpr0I8MUvfnHwoEGD1k+ePPn11rZTKe5pmplZ2YwfP37Vo48+2hdg48aNvP3221ULFizYdMefxx9/vO+ECRNWVa7C1jk0zcysbA4++OBVTzzxRF+A2bNn99p9993X9unTZ2N9fX33tWvXatGiRT2XL1/efeTIkaN22223Uccff3zt2rVrBTBo0KA9zzrrrEEjRowYNXr06JEzZ87sPX78+OFDhgwZ/YMf/GDTMyS/9a1vDRg9evTI3XbbbdTXvva1nQAWLFjQY5dddtnjxBNPHDps2LA9DjjggOGrVq3a7PvWOjTNzKxsamtr13fv3j2ee+65Hvfff3+f/fbbb3VdXd3qe+65p++DDz7Ye+jQoevOOuus2mnTpi3661//OnfDhg388Ic/3BSINTU1786fP3/uvvvuu+oLX/hC7a233rrosccem3/JJZfsBHDTTTdts3Dhwp5/+ctf5s2bN2/uU0891fu2227rC/DSSy/1PPvss5ctXLhwTr9+/TZeeeWV/Te3fp/TNDOzsho7duyqe++9t88jjzzS97zzznv9pZde6vHQQw/16dev38aBAwe+27Nnz4aPfOQj6wBOPfXUN3/+85/vSHr28gknnLAcYM8991yzevXqbv3792/o379/Q48ePRreeOON7rfffvs2DzzwwDajRo0aBbBmzZpu8+fP77nLLru8O2jQoHX777//WoC99957zeLFizf7sWIOTTMzK6v9999/1cMPP9x3/vz5vfbZZ5+1u+yyy7s//vGPB/Tt23fjgQce+M706dNb7AH27NkzALp160bpY8K6devG+vXrFRGcc845r5133nlvlK63YMGCHk0fK7Z27drNPtrqw7NmZlZWBx544Kq77rpr22233XZjVVUVAwYM2Lhy5cruTz75ZN+TTz757SVLlvR49tlntwa48sort58wYcI7ebd95JFHrvzd7363w4oVK7oBvPDCC1stWbKk3TqI7mmamXVlbXxFpAjjxo1bu3z58qrjjjtu0xNLRowYsXb16tXdd9111/WXX3754uOPP37XjRs3MmbMmDXnnntufd5tH3fccSvnzJnTc5999hkB0Lt374arr776haqqqmhr3TwU0S7bKVRdXV3MmjWr0mV8sEzuV4Z9rGh7Gesciv68+LNSCEmzI6KudNrTTz+9eMyYMW+0tI7B008/vcOYMWNqm5vnw7NmZmY5OTTNzMxycmiamXUtDQ0NDZv9pf6uIrVNQ0vzCw1NSdtKukHSfEnzJH1M0naS7pT0XPq52V8uNTOzLfZsfX19Pwfn+zU0NKi+vr4f8GxLyxR99exPgNsj4tOSegC9gQuBuyPiYkkXABcA5xdch5mZARs2bDh96dKlVyxdunQ0PtrYVAPw7IYNG05vaYHCQlNSP+BA4FSAiHgXeFfSMcBBabGpwH04NM3MymLs2LHLgKMrXUdnVWRPc2egHviNpDHAbOCrwICIeC0tsxQY0NzKkiYBkwBqamoKLNOshL9aYWatKLJrXgV8FPhFROwNrCY7FLtJZF8SbfaLohExJSLqIqKuurq6uUXMzMzKqsjQfAV4JSIeS+M3kIXo65IGAqSfywqswczMrN0UFpoRsRR4WdLuadKhwFxgBjAxTZsITC+qBjMzs/ZU9NWzXwGuTlfOPg98niyor5N0GvAicELBNZiZmbWLQkMzIp4C6pqZdWiR+zUzMyuCv6NjZmaWk0PTzMwsJ4emmZlZTg5NMzOznByaZmZmOTk0zczMcnJompmZ5eTQNDMzy8mhaWZmlpND08zMLCeHppmZWU4OTTMzs5yKfsqJmdkH1+R+BW9/RbHbt83mnqaZmVlODk0zM7OcHJpmZmY5OTTNzMxycmiamZnl5NA0MzPLyaFpZmaWk0PTzMwsp0JvbiBpMfAOsBHYEBF1krYDpgG1wGLghIh4u8g6zMzM2kM5epoHR8ReEVGXxi8A7o6I4cDdadzMzKzDq8Th2WOAqWl4KnBsBWowMzPbbEWHZgB3SJotaVKaNiAiXkvDS4EBza0oaZKkWZJm1dfXF1ymmZlZ24q+Yfv4iFgiaUfgTknzS2dGREiK5laMiCnAFIC6urpmlzEzMyunQnuaEbEk/VwG3AyMA16XNBAg/VxWZA1mZmbtpbDQlNRH0ocah4HDgWeBGcDEtNhEYHpRNZiZmbWnIg/PDgBultS4n2si4nZJjwPXSToNeBE4ocAazMzM2k1hoRkRzwNjmpn+JnBoUfs1MzMriu8IZGZmlpND08zMLCeHppmZWU4OTTMzs5wcmmZmZjk5NM3MzHJyaJqZmeXk0DQzM8vJoWlmZpaTQ9PMzCwnh6aZmVlODk0zM7OcHJpmZmY5OTTNzMxycmiamZnl5NA0MzPLyaFpZmaWk0PTzMwsJ4emmZlZTrlCU9KukrZOwwdJOlvStoVWZmZm1sHk7WneCGyUNAyYAgwBrsmzoqTukp6U9Ic0vrOkxyQtlDRNUo8tqtzMzKzM8oZmQ0RsAD4J/CwizgMG5lz3q8C8kvFLgMsiYhjwNnBa3mLNzMwqKW9orpd0EjAR+EOatlVbK0kaDPwzcEUaF3AIcENaZCpw7GbUa2ZmVjFVOZf7PHAG8P2IeEHSzsDvcqz3Y+AbwIfS+PbA8tRrBXgFGNTcipImAZMAampqcpbZjMn9tnzd3PtYUfw+zMys4nL1NCNiLnA+8EQafyEiLmltHUlHAcsiYvaWFBYRUyKiLiLqqqurt2QTZmZm7Srv1bOfAJ4Cbk/je0ma0cZqBwBHS1oM/J7ssOxPgG0lNfZwBwNLNr9sMzOz8st7TnMyMA5YDhARTwG7tLZCRPxrRAyOiFrgROCeiPgscC/w6bTYRGD65hZtZmZWCbkvBIqIpifuGrZwn+cD/1fSQrJznL/awu2YmZmVVd4LgeZIOhnoLmk4cDbwcN6dRMR9wH1p+HmyXquZmVmnkren+RVgD2Ad2U0NVgDnFFSTmZlZh9RmT1NSd+CPEXEw8P+KL8nMzKxjarOnGREbgQZJZfjCo5mZWceV95zmKuAZSXcCqxsnRsTZhVRlZmbWAeUNzZvSy8zMrMvKFZoRMTU9jWS3NGlBRKwvriwzM7OOJ1doSjqI7ObqiwEBQyRNjIgHCqvMzMysg8l7ePZS4PCIWAAgaTfgWmBsUYWZmZl1NHm/p7lVY2ACRMRfyfFoMDMzsw+SvD3NWZKuAK5K458FZhVTkpVD7d+uKXwfiwvfg5VL0Z+XxYVu3az95A3NM4GzyG6fB/Ag8J+FVGRmZtZB5Q3NKuAnEfEj2HSXoK0Lq8rMzKwDyntO826gV8l4L+Cu9i/HzMys48obmj0jYlXjSBruXUxJZmZmHVPe0Fwt6aONI5LqgLXFlGRmZtYx5T2neQ5wvaRX0/hA4DOFVGRmZtZBtdrTlLSPpA9HxOPACGAasB64HXihDPWZmZl1GG0dnv0v4N00/DHgQuDnwNvAlALrMjMz63DaOjzbPSLeSsOfAaZExI3AjZKeKrQyMzOzDqatnmZ3SY3BeihwT8m8vOdDzczMPhDaCr5rgfslvUF2teyDAJKGASsKrs3MzKxDaTU0I+L7ku4mu1r2joiINKsb8JXW1pXUE3iA7M5BVcANEXGRpJ2B3wPbA7OBUyLi3Za3ZGZm1jG0+T3NiHg0Im6OiNUl0/4aEU+0seo64JCIGAPsBRwhaT/gEuCyiBhGdkHRaVtcvZmZWRnlvbnBZotM412EtkqvAA4BbkjTpwLHFlWDmZlZeyr0Yp50Y/fZwDCyr6osApZHxIa0yCvAoBbWnQRMAqipqSmyTLNN/AgsM2tNYT1NgIjYGBF7AYOBcWQ3SMi77pSIqIuIuurq6qJKNDMzy63Q0GwUEcuBe8lukLBtyddYBgNLylGDmZnZP6qw0JRULWnbNNwL+Dgwjyw8P50WmwhML6oGMzOz9lTkOc2BwNR0XrMbcF1E/EHSXOD3kr4HPAn8qsAazMzM2k1hoRkRfwH2bmb682TnN83MzDqVspzTNDMz+yBwaJqZmeXk0DQzM8vJTyoxM9tCvhlG1+OeppmZWU4OTTMzs5wcmmZmZjk5NM3MzHJyaJqZmeXk0DQzM8vJoWlmZpaTQ9PMzCwnh6aZmVlODk0zM7OcHJpmZmY5OTTNzMxycmiamZnl5NA0MzPLyaFpZmaWk0PTzMwsp8JCU9IQSfdKmitpjqSvpunbSbpT0nPpZ/+iajAzM2tPRfY0NwBfj4hRwH7AWZJGARcAd0fEcODuNG5mZtbhFRaaEfFaRDyRht8B5gGDgGOAqWmxqcCxRdVgZmbWnspyTlNSLbA38BgwICJeS7OWAgPKUYOZmdk/qqroHUjqC9wInBMRKyVtmhcRISlaWG8SMAmgpqZmi/df+7drtnjdvBYXvgczM+sICu1pStqKLDCvjoib0uTXJQ1M8wcCy5pbNyKmRERdRNRVV1cXWaaZmVkuRV49K+BXwLyI+FHJrBnAxDQ8EZheVA1mZmbtqcjDswcApwDPSHoqTbsQuBi4TtJpwIvACQXWYGZm1m4KC82ImAmohdmHFrVfMzOzoviOQGZmZjk5NM3MzHJyaJqZmeXk0DQzM8vJoWlmZpaTQ9PMzCwnh6aZmVlODk0zM7OcHJpmZmY5OTTNzMxycmiamZnl5NA0MzPLyaFpZmaWk0PTzMwsJ4emmZlZTg5NMzOznByaZmZmOTk0zczMcnJompmZ5eTQNDMzy8mhaWZmllNhoSnp15KWSXq2ZNp2ku6U9Fz62b+o/ZuZmbW3InuavwWOaDLtAuDuiBgO3J3GzczMOoXCQjMiHgDeajL5GGBqGp4KHFvU/s3MzNpbuc9pDoiI19LwUmBASwtKmiRplqRZ9fX15anOzMysFRW7ECgiAohW5k+JiLqIqKuuri5jZWZmZs0rd2i+LmkgQPq5rMz7NzMz22LlDs0ZwMQ0PBGYXub9m5mZbbEiv3JyLfAIsLukVySdBlwMfFzSc8BhadzMzKxTqCpqwxFxUguzDi1qn2ZmZkXyHYHMzMxycmiamZnl5NA0MzPLyaFpZmaWk0PTzMwsJ4emmZlZTg5NMzOznByaZmZmOTk0zczMcnJompmZ5eTQNDMzy8mhaWZmlpND08zMLCeHppmZWU4OTTMzs5wcmmZmZjk5NM3MzHJyaJqZmeXk0DQzM8vJoWlmZpaTQ9PMzCynioSmpCMkLZC0UNIFlajBzMxsc5U9NCV1B34OHAmMAk6SNKrcdZiZmW2uSvQ0xwELI+L5iHgX+D1wTAXqMDMz2yyKiPLuUPo0cEREnJ7GTwH2jYgvN1luEjApje4OLChTiTsAb5RpX52J26V5bpfmuV2aV+52GRoR1WXc3wdeVaULaElETAGmlHu/kmZFRF2599vRuV2a53ZpntuleW6Xzq8Sh2eXAENKxgenaWZmZh1aJULzcWC4pJ0l9QBOBGZUoA4zM7PNUvbDsxGxQdKXgT8B3YFfR8ScctfRirIfEu4k3C7Nc7s0z+3SPLdLJ1f2C4HMzMw6K98RyMzMLCeHppmZWU5dOjQlDZB0jaTnJc2W9IikT0raXtK9klZJ+o9K11lurbTLx9P4M+nnIZWutZxaaZdxkp5Kr6clfbLStZZTS+1SMr8m/V86t5J1llsrn5daSWtLPjOXV7pWy6/Dfk+zaJIE3AJMjYiT07ShwNHA34BvAaPTq8too11mAp+IiFcljSa7mGtQpWotpzba5U9AXbrIbSDwtKRbI2JDxQoukzbapdGPgNvKX13ltNEuTwKLImKvihVoW6zLhiZwCPBuRGz6Ky8iXgR+lkZnShpWkcoqq612aTQH6CVp64hYV84CKyRvu/QEutLVda22i6RjgReA1RWprnJabBdJtRWryv5hXfnw7B7AE5UuogPK2y6fAp7oIoEJbbSLpH0lzQGeAc7oCr3MpMV2kdQXOB/4Tlkr6hja+n+0s6QnJd0vaUK5irJ/XFfuab6HpJ8D48n+Otyn0vV0FM21i6Q9gEuAwytZWyU1bZeIeAzYQ9JIYKqk2yLib5WtsvxK2wW4H7gsIlZlRyu7ribtMh6oiYg3JY0FbpG0R0SsrGiRlktX7mnOAT7aOBIRZwGHAl395sattoukwcDNwOciYlFFKqyMXJ+XiJgHrKLrnAtvrV32BX4gaTFwDnBhurFJV9Biu0TEuoh4M02fDSwCdqtIlbbZunJo3gP0lHRmybTelSqmA2mxXSRtC/wRuCAiHqpAbZXUWrvsLKkqDQ8FRgCLy15hZbTYLhExISJqI6IW+DHwbxHRVa5Gb+3zUp2eK4ykXYDhwPPlL9G2RJe+I1C60vEysr+I68kuVrg8Iqalv463AXoAy4HDI2JuhUotq5bahew/978Cz5UsfnhELCt7kRXQSrv0AC4A1gMNwHcj4pYKlVl2rf0/KllmMrAqIv69IkVWQCuflw3Ad/n75+WiiLi1UnXa5unSoWlmZrY5uvLhWTMzs83i0DQzM8vJoWlmZpaTQ9PMzCwnh6aZmVlODk0zM7OcHJpmZmY5/Q+PZW4HJqiT9wAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 155,
      "metadata": {
        "collapsed": false,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T16:17:20.045Z",
          "iopub.execute_input": "2020-11-05T16:17:20.056Z",
          "iopub.status.idle": "2020-11-05T16:17:20.168Z",
          "shell.execute_reply": "2020-11-05T16:17:20.192Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "labels = ['G1', 'G2', 'G3', 'G4', 'G5']\n",
        "men_means = [20, 34, 30, 35, 27]\n",
        "women_means = [25, 32, 34, 20, 25]\n",
        "x = np.arange(len(labels))  # the label locations\n",
        "width = 0.35  # the width of the bars\n",
        "fig, ax = plt.subplots()\n",
        "rects1 = ax.bar(x - width/2, men_means, width, label='Men')\n",
        "# rects2 = ax.bar(x + width/2, women_means, width, label='Women')\n",
        "# Add some text for labels, title and custom x-axis tick labels, etc.\n",
        "ax.set_ylabel('Scores')\n",
        "ax.set_title('Scores by group and gender')\n",
        "ax.set_xticks(x)\n",
        "ax.set_xticklabels(labels)\n",
        "ax.legend()\n",
        "plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')\n",
        "\n",
        "\n",
        "#def autolabel(rects):\n",
        "#    \"\"\"Attach a text label above each bar in *rects*, displaying its height.\"\"\"\n",
        "#    for rect in rects:\n",
        "#        height = rect.get_height()\n",
        "#        ax.annotate('{}'.format(height),\n",
        "#                    xy=(rect.get_x() + rect.get_width() / 2, height),\n",
        "#                    xytext=(0, 3),  # 3 points vertical offset\n",
        "#                    textcoords=\"offset points\",\n",
        "#                    ha='center', va='bottom')\n",
        "\n",
        "\n",
        "#autolabel(rects1)\n",
        "#autolabel(rects2)\n",
        "fig.tight_layout()\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 149,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T16:14:46.361Z",
          "iopub.execute_input": "2020-11-05T16:14:46.373Z",
          "iopub.status.idle": "2020-11-05T16:14:46.473Z",
          "shell.execute_reply": "2020-11-05T16:14:46.492Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "# = tmpdf3['mpi']\n",
        "fig, ax = plt.subplots()\n",
        "ax.stackplot(tmpdf3['mpi'], tmpdf3['IAD'], labels=['IAD'] ) # , labels=population_by_continent.keys())\n",
        "# ax.legend(loc='upper left')\n",
        "plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')\n",
        "# plt.tight_layout()\n",
        "# plt.legend(bbox_to_anchor=(1.05, 1))\n",
        "# plt.xticks(year, year)\n",
        "\n",
        "# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8], tmpdf3['mpi'])\n",
        "# plt.xticks(tmpdf3['mpi'], [0, 1, 2, 3, 4, 5, 6, 7, 8])\n",
        "# plt.xticks(tmpdf3['mpi'], tmpdf3['mpi'])\n",
        "\n",
        "plt.xticks(rotation=45)\n",
        "plt.grid(True)\n",
        "ax.set_title('Sedov test Weak scaling')\n",
        "ax.set_xlabel('# of cores')\n",
        "ax.set_ylabel('Walltime / s')\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 139,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T16:09:12.138Z",
          "iopub.execute_input": "2020-11-05T16:09:12.148Z",
          "iopub.status.idle": "2020-11-05T16:09:12.310Z",
          "shell.execute_reply": "2020-11-05T16:09:12.327Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(year)\n",
        "print(population_by_continent.values())\n",
        "print(population_by_continent.keys())\n",
        "a = type(year) # list\n",
        "b = type(population_by_continent.values()) # dict_values\n",
        "c = type(population_by_continent.keys()) # dict_keys\n",
        "print(a,b,c)"
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1950, 1960, 1970]\n",
            "dict_values([[228, 284, 365], [340, 425, 519]])\n",
            "dict_keys(['africa', 'americas'])\n",
            "<class 'list'> <class 'dict_values'> <class 'dict_keys'>\n"
          ]
        }
      ],
      "execution_count": 114,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:53:23.934Z",
          "iopub.execute_input": "2020-11-05T15:53:23.944Z",
          "iopub.status.idle": "2020-11-05T15:53:23.964Z",
          "shell.execute_reply": "2020-11-05T15:53:23.974Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "year = [1950, 1960, 1970]\n",
        "population_by_continent = {\n",
        "    'africa': [228, 284, 365],\n",
        "    'americas': [340, 425, 519],\n",
        "}\n",
        "fig, ax = plt.subplots()\n",
        "# ax.stackplot(year, population_by_continent.values(), labels=population_by_continent.keys())\n",
        "ax.stackplot(year, population_by_continent.values()) # , labels=population_by_continent.keys())\n",
        "ax.legend(loc='upper left')\n",
        "plt.xticks(year, year)\n",
        "ax.set_title('World population')\n",
        "ax.set_xlabel('Year')\n",
        "ax.set_ylabel('Number of people (millions)')\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "No handles with labels found to put in legend.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 115,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:57:52.275Z",
          "iopub.execute_input": "2020-11-05T15:57:52.287Z",
          "iopub.status.idle": "2020-11-05T15:57:52.338Z",
          "shell.execute_reply": "2020-11-05T15:57:52.358Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "# data from United Nations World Population Prospects (Revision 2019)\n",
        "# https://population.un.org/wpp/, license: CC BY 3.0 IGO\n",
        "year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]\n",
        "population_by_continent = {\n",
        "    'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],\n",
        "    'americas': [340, 425, 519, 619, 727, 840, 943, 1006],\n",
        "    'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],\n",
        "    'europe': [220, 253, 276, 295, 310, 303, 294, 293],\n",
        "    'oceania': [12, 15, 19, 22, 26, 31, 36, 39],\n",
        "}\n",
        "fig, ax = plt.subplots()\n",
        "ax.stackplot(year, population_by_continent.values(), labels=population_by_continent.keys())\n",
        "ax.legend(loc='upper left')\n",
        "ax.set_title('World population')\n",
        "ax.set_xlabel('Year')\n",
        "ax.set_ylabel('Number of people (millions)')\n",
        "\n",
        "plt.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 92,
      "metadata": {
        "collapsed": false,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:39:00.097Z",
          "iopub.execute_input": "2020-11-05T15:39:00.106Z",
          "iopub.status.idle": "2020-11-05T15:39:00.255Z",
          "shell.execute_reply": "2020-11-05T15:39:00.268Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# import plotly.graph_objects as go\n",
        "import plotly.express as px\n",
        "df = px.data.gapminder()\n",
        "fig = px.area(df, x=\"year\", y=\"pop\") # , color=\"continent\") # , line_group=\"country\")\n",
        "fig.show()"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.plotly.v1+json": {
              "config": {
                "plotlyServerURL": "https://plot.ly"
              },
              "data": [
                {
                  "hovertemplate": "year=%{x}<br>pop=%{y}<extra></extra>",
                  "legendgroup": "",
                  "line": {
                    "color": "#636efa"
                  },
                  "mode": "lines",
                  "name": "",
                  "orientation": "v",
                  "showlegend": false,
                  "stackgroup": "1",
                  "type": "scatter",
                  "x": [
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007,
                    1952,
                    1957,
                    1962,
                    1967,
                    1972,
                    1977,
                    1982,
                    1987,
                    1992,
                    1997,
                    2002,
                    2007
                  ],
                  "xaxis": "x",
                  "y": [
                    8425333,
                    9240934,
                    10267083,
                    11537966,
                    13079460,
                    14880372,
                    12881816,
                    13867957,
                    16317921,
                    22227415,
                    25268405,
                    31889923,
                    1282697,
                    1476505,
                    1728137,
                    1984060,
                    2263554,
                    2509048,
                    2780097,
                    3075321,
                    3326498,
                    3428038,
                    3508512,
                    3600523,
                    9279525,
                    10270856,
                    11000948,
                    12760499,
                    14760787,
                    17152804,
                    20033753,
                    23254956,
                    26298373,
                    29072015,
                    31287142,
                    33333216,
                    4232095,
                    4561361,
                    4826015,
                    5247469,
                    5894858,
                    6162675,
                    7016384,
                    7874230,
                    8735988,
                    9875024,
                    10866106,
                    12420476,
                    17876956,
                    19610538,
                    21283783,
                    22934225,
                    24779799,
                    26983828,
                    29341374,
                    31620918,
                    33958947,
                    36203463,
                    38331121,
                    40301927,
                    8691212,
                    9712569,
                    10794968,
                    11872264,
                    13177000,
                    14074100,
                    15184200,
                    16257249,
                    17481977,
                    18565243,
                    19546792,
                    20434176,
                    6927772,
                    6965860,
                    7129864,
                    7376998,
                    7544201,
                    7568430,
                    7574613,
                    7578903,
                    7914969,
                    8069876,
                    8148312,
                    8199783,
                    120447,
                    138655,
                    171863,
                    202182,
                    230800,
                    297410,
                    377967,
                    454612,
                    529491,
                    598561,
                    656397,
                    708573,
                    46886859,
                    51365468,
                    56839289,
                    62821884,
                    70759295,
                    80428306,
                    93074406,
                    103764241,
                    113704579,
                    123315288,
                    135656790,
                    150448339,
                    8730405,
                    8989111,
                    9218400,
                    9556500,
                    9709100,
                    9821800,
                    9856303,
                    9870200,
                    10045622,
                    10199787,
                    10311970,
                    10392226,
                    1738315,
                    1925173,
                    2151895,
                    2427334,
                    2761407,
                    3168267,
                    3641603,
                    4243788,
                    4981671,
                    6066080,
                    7026113,
                    8078314,
                    2883315,
                    3211738,
                    3593918,
                    4040665,
                    4565872,
                    5079716,
                    5642224,
                    6156369,
                    6893451,
                    7693188,
                    8445134,
                    9119152,
                    2791000,
                    3076000,
                    3349000,
                    3585000,
                    3819000,
                    4086000,
                    4172693,
                    4338977,
                    4256013,
                    3607000,
                    4165416,
                    4552198,
                    442308,
                    474639,
                    512764,
                    553541,
                    619351,
                    781472,
                    970347,
                    1151184,
                    1342614,
                    1536536,
                    1630347,
                    1639131,
                    56602560,
                    65551171,
                    76039390,
                    88049823,
                    100840058,
                    114313951,
                    128962939,
                    142938076,
                    155975974,
                    168546719,
                    179914212,
                    190010647,
                    7274900,
                    7651254,
                    8012946,
                    8310226,
                    8576200,
                    8797022,
                    8892098,
                    8971958,
                    8658506,
                    8066057,
                    7661799,
                    7322858,
                    4469979,
                    4713416,
                    4919632,
                    5127935,
                    5433886,
                    5889574,
                    6634596,
                    7586551,
                    8878303,
                    10352843,
                    12251209,
                    14326203,
                    2445618,
                    2667518,
                    2961915,
                    3330989,
                    3529983,
                    3834415,
                    4580410,
                    5126023,
                    5809236,
                    6121610,
                    7021078,
                    8390505,
                    4693836,
                    5322536,
                    6083619,
                    6960067,
                    7450606,
                    6978607,
                    7272485,
                    8371791,
                    10150094,
                    11782962,
                    12926707,
                    14131858,
                    5009067,
                    5359923,
                    5793633,
                    6335506,
                    7021028,
                    7959865,
                    9250831,
                    10780667,
                    12467171,
                    14195809,
                    15929988,
                    17696293,
                    14785584,
                    17010154,
                    18985849,
                    20819767,
                    22284500,
                    23796400,
                    25201900,
                    26549700,
                    28523502,
                    30305843,
                    31902268,
                    33390141,
                    1291695,
                    1392284,
                    1523478,
                    1733638,
                    1927260,
                    2167533,
                    2476971,
                    2840009,
                    3265124,
                    3696513,
                    4048013,
                    4369038,
                    2682462,
                    2894855,
                    3150417,
                    3495967,
                    3899068,
                    4388260,
                    4875118,
                    5498955,
                    6429417,
                    7562011,
                    8835739,
                    10238807,
                    6377619,
                    7048426,
                    7961258,
                    8858908,
                    9717524,
                    10599793,
                    11487112,
                    12463354,
                    13572994,
                    14599929,
                    15497046,
                    16284741,
                    556263527,
                    637408000,
                    665770000,
                    754550000,
                    862030000,
                    943455000,
                    1000281000,
                    1084035000,
                    1164970000,
                    1230075000,
                    1280400000,
                    1318683096,
                    12350771,
                    14485993,
                    17009885,
                    19764027,
                    22542890,
                    25094412,
                    27764644,
                    30964245,
                    34202721,
                    37657830,
                    41008227,
                    44227550,
                    153936,
                    170928,
                    191689,
                    217378,
                    250027,
                    304739,
                    348643,
                    395114,
                    454429,
                    527982,
                    614382,
                    710960,
                    14100005,
                    15577932,
                    17486434,
                    19941073,
                    23007669,
                    26480870,
                    30646495,
                    35481645,
                    41672143,
                    47798986,
                    55379852,
                    64606759,
                    854885,
                    940458,
                    1047924,
                    1179760,
                    1340458,
                    1536769,
                    1774735,
                    2064095,
                    2409073,
                    2800947,
                    3328795,
                    3800610,
                    926317,
                    1112300,
                    1345187,
                    1588717,
                    1834796,
                    2108457,
                    2424367,
                    2799811,
                    3173216,
                    3518107,
                    3834934,
                    4133884,
                    2977019,
                    3300000,
                    3832408,
                    4744870,
                    6071696,
                    7459574,
                    9025951,
                    10761098,
                    12772596,
                    14625967,
                    16252726,
                    18013409,
                    3882229,
                    3991242,
                    4076557,
                    4174366,
                    4225310,
                    4318673,
                    4413368,
                    4484310,
                    4494013,
                    4444595,
                    4481020,
                    4493312,
                    6007797,
                    6640752,
                    7254373,
                    8139332,
                    8831348,
                    9537988,
                    9789224,
                    10239839,
                    10723260,
                    10983007,
                    11226999,
                    11416987,
                    9125183,
                    9513758,
                    9620282,
                    9835109,
                    9862158,
                    10161915,
                    10303704,
                    10311597,
                    10315702,
                    10300707,
                    10256295,
                    10228744,
                    4334000,
                    4487831,
                    4646899,
                    4838800,
                    4991596,
                    5088419,
                    5117810,
                    5127024,
                    5171393,
                    5283663,
                    5374693,
                    5468120,
                    63149,
                    71851,
                    89898,
                    127617,
                    178848,
                    228694,
                    305991,
                    311025,
                    384156,
                    417908,
                    447416,
                    496374,
                    2491346,
                    2923186,
                    3453434,
                    4049146,
                    4671329,
                    5302800,
                    5968349,
                    6655297,
                    7351181,
                    7992357,
                    8650322,
                    9319622,
                    3548753,
                    4058385,
                    4681707,
                    5432424,
                    6298651,
                    7278866,
                    8365850,
                    9545158,
                    10748394,
                    11911819,
                    12921234,
                    13755680,
                    22223309,
                    25009741,
                    28173309,
                    31681188,
                    34807417,
                    38783863,
                    45681811,
                    52799062,
                    59402198,
                    66134291,
                    73312559,
                    80264543,
                    2042865,
                    2355805,
                    2747687,
                    3232927,
                    3790903,
                    4282586,
                    4474873,
                    4842194,
                    5274649,
                    5783439,
                    6353681,
                    6939688,
                    216964,
                    232922,
                    249220,
                    259864,
                    277603,
                    192675,
                    285483,
                    341244,
                    387838,
                    439971,
                    495627,
                    551201,
                    1438760,
                    1542611,
                    1666618,
                    1820319,
                    2260187,
                    2512642,
                    2637297,
                    2915959,
                    3668440,
                    4058319,
                    4414865,
                    4906585,
                    20860941,
                    22815614,
                    25145372,
                    27860297,
                    30770372,
                    34617799,
                    38111756,
                    42999530,
                    52088559,
                    59861301,
                    67946797,
                    76511887,
                    4090500,
                    4324000,
                    4491443,
                    4605744,
                    4639657,
                    4738902,
                    4826933,
                    4931729,
                    5041039,
                    5134406,
                    5193039,
                    5238460,
                    42459667,
                    44310863,
                    47124000,
                    49569000,
                    51732000,
                    53165019,
                    54433565,
                    55630100,
                    57374179,
                    58623428,
                    59925035,
                    61083916,
                    420702,
                    434904,
                    455661,
                    489004,
                    537977,
                    706367,
                    753874,
                    880397,
                    985739,
                    1126189,
                    1299304,
                    1454867,
                    284320,
                    323150,
                    374020,
                    439593,
                    517101,
                    608274,
                    715523,
                    848406,
                    1025384,
                    1235767,
                    1457766,
                    1688359,
                    69145952,
                    71019069,
                    73739117,
                    76368453,
                    78717088,
                    78160773,
                    78335266,
                    77718298,
                    80597764,
                    82011073,
                    82350671,
                    82400996,
                    5581001,
                    6391288,
                    7355248,
                    8490213,
                    9354120,
                    10538093,
                    11400338,
                    14168101,
                    16278738,
                    18418288,
                    20550751,
                    22873338,
                    7733250,
                    8096218,
                    8448233,
                    8716441,
                    8888628,
                    9308479,
                    9786480,
                    9974490,
                    10325429,
                    10502372,
                    10603863,
                    10706290,
                    3146381,
                    3640876,
                    4208858,
                    4690773,
                    5149581,
                    5703430,
                    6395630,
                    7326406,
                    8486949,
                    9803875,
                    11178650,
                    12572928,
                    2664249,
                    2876726,
                    3140003,
                    3451418,
                    3811387,
                    4227026,
                    4710497,
                    5650262,
                    6990574,
                    8048834,
                    8807818,
                    9947814,
                    580653,
                    601095,
                    627820,
                    601287,
                    625361,
                    745228,
                    825987,
                    927524,
                    1050938,
                    1193708,
                    1332459,
                    1472041,
                    3201488,
                    3507701,
                    3880130,
                    4318137,
                    4698301,
                    4908554,
                    5198399,
                    5756203,
                    6326682,
                    6913545,
                    7607651,
                    8502814,
                    1517453,
                    1770390,
                    2090162,
                    2500689,
                    2965146,
                    3055235,
                    3669448,
                    4372203,
                    5077347,
                    5867957,
                    6677328,
                    7483763,
                    2125900,
                    2736300,
                    3305200,
                    3722800,
                    4115700,
                    4583700,
                    5264500,
                    5584510,
                    5829696,
                    6495918,
                    6762476,
                    6980412,
                    9504000,
                    9839000,
                    10063000,
                    10223422,
                    10394091,
                    10637171,
                    10705535,
                    10612740,
                    10348684,
                    10244684,
                    10083313,
                    9956108,
                    147962,
                    165110,
                    182053,
                    198676,
                    209275,
                    221823,
                    233997,
                    244676,
                    259012,
                    271192,
                    288030,
                    301931,
                    372000000,
                    409000000,
                    454000000,
                    506000000,
                    567000000,
                    634000000,
                    708000000,
                    788000000,
                    872000000,
                    959000000,
                    1034172547,
                    1110396331,
                    82052000,
                    90124000,
                    99028000,
                    109343000,
                    121282000,
                    136725000,
                    153343000,
                    169276000,
                    184816000,
                    199278000,
                    211060000,
                    223547000,
                    17272000,
                    19792000,
                    22874000,
                    26538000,
                    30614000,
                    35480679,
                    43072751,
                    51889696,
                    60397973,
                    63327987,
                    66907826,
                    69453570,
                    5441766,
                    6248643,
                    7240260,
                    8519282,
                    10061506,
                    11882916,
                    14173318,
                    16543189,
                    17861905,
                    20775703,
                    24001816,
                    27499638,
                    2952156,
                    2878220,
                    2830000,
                    2900100,
                    3024400,
                    3271900,
                    3480000,
                    3539900,
                    3557761,
                    3667233,
                    3879155,
                    4109086,
                    1620914,
                    1944401,
                    2310904,
                    2693585,
                    3095893,
                    3495918,
                    3858421,
                    4203148,
                    4936550,
                    5531387,
                    6029529,
                    6426679,
                    47666000,
                    49182000,
                    50843200,
                    52667100,
                    54365564,
                    56059245,
                    56535636,
                    56729703,
                    56840847,
                    57479469,
                    57926999,
                    58147733,
                    1426095,
                    1535090,
                    1665128,
                    1861096,
                    1997616,
                    2156814,
                    2298309,
                    2326606,
                    2378618,
                    2531311,
                    2664659,
                    2780132,
                    86459025,
                    91563009,
                    95831757,
                    100825279,
                    107188273,
                    113872473,
                    118454974,
                    122091325,
                    124329269,
                    125956499,
                    127065841,
                    127467972,
                    607914,
                    746559,
                    933559,
                    1255058,
                    1613551,
                    1937652,
                    2347031,
                    2820042,
                    3867409,
                    4526235,
                    5307470,
                    6053193,
                    6464046,
                    7454779,
                    8678557,
                    10191512,
                    12044785,
                    14500404,
                    17661452,
                    21198082,
                    25020539,
                    28263827,
                    31386842,
                    35610177,
                    8865488,
                    9411381,
                    10917494,
                    12617009,
                    14781241,
                    16325320,
                    17647518,
                    19067554,
                    20711375,
                    21585105,
                    22215365,
                    23301725,
                    20947571,
                    22611552,
                    26420307,
                    30131000,
                    33505000,
                    36436000,
                    39326000,
                    41622000,
                    43805450,
                    46173816,
                    47969150,
                    49044790,
                    160000,
                    212846,
                    358266,
                    575003,
                    841934,
                    1140357,
                    1497494,
                    1891487,
                    1418095,
                    1765345,
                    2111561,
                    2505559,
                    1439529,
                    1647412,
                    1886848,
                    2186894,
                    2680018,
                    3115787,
                    3086876,
                    3089353,
                    3219994,
                    3430388,
                    3677780,
                    3921278,
                    748747,
                    813338,
                    893143,
                    996380,
                    1116779,
                    1251524,
                    1411807,
                    1599200,
                    1803195,
                    1982823,
                    2046772,
                    2012649,
                    863308,
                    975950,
                    1112796,
                    1279406,
                    1482628,
                    1703617,
                    1956875,
                    2269414,
                    1912974,
                    2200725,
                    2814651,
                    3193942,
                    1019729,
                    1201578,
                    1441863,
                    1759224,
                    2183877,
                    2721783,
                    3344074,
                    3799845,
                    4364501,
                    4759670,
                    5368585,
                    6036914,
                    4762912,
                    5181679,
                    5703324,
                    6334556,
                    7082430,
                    8007166,
                    9171477,
                    10568642,
                    12210395,
                    14165114,
                    16473477,
                    19167654,
                    2917802,
                    3221238,
                    3628608,
                    4147252,
                    4730997,
                    5637246,
                    6502825,
                    7824747,
                    10014249,
                    10419991,
                    11824495,
                    13327079,
                    6748378,
                    7739235,
                    8906385,
                    10154878,
                    11441462,
                    12845381,
                    14441916,
                    16331785,
                    18319502,
                    20476091,
                    22662365,
                    24821286,
                    3838168,
                    4241884,
                    4690372,
                    5212416,
                    5828158,
                    6491649,
                    6998256,
                    7634008,
                    8416215,
                    9384984,
                    10580176,
                    12031795,
                    1022556,
                    1076852,
                    1146757,
                    1230542,
                    1332786,
                    1456688,
                    1622136,
                    1841240,
                    2119465,
                    2444741,
                    2828858,
                    3270065,
                    516556,
                    609816,
                    701016,
                    789309,
                    851334,
                    913025,
                    992040,
                    1042663,
                    1096202,
                    1149818,
                    1200206,
                    1250882,
                    30144317,
                    35015548,
                    41121485,
                    47995559,
                    55984294,
                    63759976,
                    71640904,
                    80122492,
                    88111030,
                    95895146,
                    102479927,
                    108700891,
                    800663,
                    882134,
                    1010280,
                    1149500,
                    1320500,
                    1528000,
                    1756032,
                    2015133,
                    2312802,
                    2494803,
                    2674234,
                    2874127,
                    413834,
                    442829,
                    474528,
                    501035,
                    527678,
                    560073,
                    562548,
                    569473,
                    621621,
                    692651,
                    720230,
                    684736,
                    9939217,
                    11406350,
                    13056604,
                    14770296,
                    16660670,
                    18396941,
                    20198730,
                    22987397,
                    25798239,
                    28529501,
                    31167783,
                    33757175,
                    6446316,
                    7038035,
                    7788944,
                    8680909,
                    9809596,
                    11127868,
                    12587223,
                    12891952,
                    13160731,
                    16603334,
                    18473780,
                    19951656,
                    20092996,
                    21731844,
                    23634436,
                    25870271,
                    28466390,
                    31528087,
                    34680442,
                    38028578,
                    40546538,
                    43247867,
                    45598081,
                    47761980,
                    485831,
                    548080,
                    621392,
                    706640,
                    821782,
                    977026,
                    1099010,
                    1278184,
                    1554253,
                    1774766,
                    1972153,
                    2055080,
                    9182536,
                    9682338,
                    10332057,
                    11261690,
                    12412593,
                    13933198,
                    15796314,
                    17917180,
                    20326209,
                    23001113,
                    25873917,
                    28901790,
                    10381988,
                    11026383,
                    11805689,
                    12596822,
                    13329874,
                    13852989,
                    14310401,
                    14665278,
                    15174244,
                    15604464,
                    16122830,
                    16570613,
                    1994794,
                    2229407,
                    2488550,
                    2728150,
                    2929100,
                    3164900,
                    3210650,
                    3317166,
                    3437674,
                    3676187,
                    3908037,
                    4115771,
                    1165790,
                    1358828,
                    1590597,
                    1865490,
                    2182908,
                    2554598,
                    2979423,
                    3344353,
                    4017939,
                    4609572,
                    5146848,
                    5675356,
                    3379468,
                    3692184,
                    4076008,
                    4534062,
                    5060262,
                    5682086,
                    6437188,
                    7332638,
                    8392818,
                    9666252,
                    11140655,
                    12894865,
                    33119096,
                    37173340,
                    41871351,
                    47287752,
                    53740085,
                    62209173,
                    73039376,
                    81551520,
                    93364244,
                    106207839,
                    119901274,
                    135031164,
                    3327728,
                    3491938,
                    3638919,
                    3786019,
                    3933004,
                    4043205,
                    4114787,
                    4186147,
                    4286357,
                    4405672,
                    4535591,
                    4627926,
                    507833,
                    561977,
                    628164,
                    714775,
                    829050,
                    1004533,
                    1301048,
                    1593882,
                    1915208,
                    2283635,
                    2713462,
                    3204897,
                    41346560,
                    46679944,
                    53100671,
                    60641899,
                    69325921,
                    78152686,
                    91462088,
                    105186881,
                    120065004,
                    135564834,
                    153403524,
                    169270617,
                    940080,
                    1063506,
                    1215725,
                    1405486,
                    1616384,
                    1839782,
                    2036305,
                    2253639,
                    2484997,
                    2734531,
                    2990875,
                    3242173,
                    1555876,
                    1770902,
                    2009813,
                    2287985,
                    2614104,
                    2984494,
                    3366439,
                    3886512,
                    4483945,
                    5154123,
                    5884491,
                    6667147,
                    8025700,
                    9146100,
                    10516500,
                    12132200,
                    13954700,
                    15990099,
                    18125129,
                    20195924,
                    22430449,
                    24748122,
                    26769436,
                    28674757,
                    22438691,
                    26072194,
                    30325264,
                    35356600,
                    40850141,
                    46850962,
                    53456774,
                    60017788,
                    67185766,
                    75012988,
                    82995088,
                    91077287,
                    25730551,
                    28235346,
                    30329617,
                    31785378,
                    33039545,
                    34621254,
                    36227381,
                    37740710,
                    38370697,
                    38654957,
                    38625976,
                    38518241,
                    8526050,
                    8817650,
                    9019800,
                    9103000,
                    8970450,
                    9662600,
                    9859650,
                    9915289,
                    9927680,
                    10156415,
                    10433867,
                    10642836,
                    2227000,
                    2260000,
                    2448046,
                    2648961,
                    2847132,
                    3080828,
                    3279001,
                    3444468,
                    3585176,
                    3759430,
                    3859606,
                    3942491,
                    257700,
                    308700,
                    358900,
                    414024,
                    461633,
                    492095,
                    517810,
                    562035,
                    622191,
                    684810,
                    743981,
                    798094,
                    16630000,
                    17829327,
                    18680721,
                    19284814,
                    20662648,
                    21658597,
                    22356726,
                    22686371,
                    22797027,
                    22562458,
                    22404337,
                    22276056,
                    2534927,
                    2822082,
                    3051242,
                    3451079,
                    3992121,
                    4657072,
                    5507565,
                    6349365,
                    7290203,
                    7212583,
                    7852401,
                    8860588,
                    60011,
                    61325,
                    65345,
                    70787,
                    76595,
                    86796,
                    98593,
                    110812,
                    125911,
                    145608,
                    170372,
                    199579,
                    4005677,
                    4419650,
                    4943029,
                    5618198,
                    6472756,
                    8128505,
                    11254672,
                    14619745,
                    16945857,
                    21229759,
                    24501530,
                    27601038,
                    2755589,
                    3054547,
                    3430243,
                    3965841,
                    4588696,
                    5260855,
                    6147783,
                    7171347,
                    8307920,
                    9535314,
                    10870037,
                    12267493,
                    6860147,
                    7271135,
                    7616060,
                    7971222,
                    8313288,
                    8686367,
                    9032824,
                    9230783,
                    9826397,
                    10336594,
                    10111559,
                    10150265,
                    2143249,
                    2295678,
                    2467895,
                    2662190,
                    2879013,
                    3140897,
                    3464522,
                    3868905,
                    4260884,
                    4578212,
                    5359092,
                    6144562,
                    1127000,
                    1445929,
                    1750200,
                    1977600,
                    2152400,
                    2325300,
                    2651869,
                    2794552,
                    3235865,
                    3802309,
                    4197776,
                    4553009,
                    3558137,
                    3844277,
                    4237384,
                    4442238,
                    4593433,
                    4827803,
                    5048043,
                    5199318,
                    5302888,
                    5383010,
                    5410052,
                    5447502,
                    1489518,
                    1533070,
                    1582962,
                    1646912,
                    1694510,
                    1746919,
                    1861252,
                    1945870,
                    1999210,
                    2011612,
                    2011497,
                    2009245,
                    2526994,
                    2780415,
                    3080153,
                    3428839,
                    3840161,
                    4353666,
                    5828892,
                    6921858,
                    6099799,
                    6633514,
                    7753310,
                    9118773,
                    14264935,
                    16151549,
                    18356657,
                    20997321,
                    23935810,
                    27129932,
                    31140029,
                    35933379,
                    39964159,
                    42835005,
                    44433622,
                    43997828,
                    28549870,
                    29841614,
                    31158061,
                    32850275,
                    34513161,
                    36439000,
                    37983310,
                    38880702,
                    39549438,
                    39855442,
                    40152517,
                    40448191,
                    7982342,
                    9128546,
                    10421936,
                    11737396,
                    13016733,
                    14116836,
                    15410151,
                    16495304,
                    17587060,
                    18698655,
                    19576783,
                    20378239,
                    8504667,
                    9753392,
                    11183227,
                    12716129,
                    14597019,
                    17104986,
                    20367053,
                    24725960,
                    28227588,
                    32160729,
                    37090298,
                    42292929,
                    290243,
                    326741,
                    370006,
                    420690,
                    480105,
                    551425,
                    649901,
                    779348,
                    962344,
                    1054486,
                    1130269,
                    1133066,
                    7124673,
                    7363802,
                    7561588,
                    7867931,
                    8122293,
                    8251648,
                    8325260,
                    8421403,
                    8718867,
                    8897619,
                    8954175,
                    9031088,
                    4815000,
                    5126000,
                    5666000,
                    6063000,
                    6401400,
                    6316424,
                    6468126,
                    6649942,
                    6995447,
                    7193761,
                    7361757,
                    7554661,
                    3661549,
                    4149908,
                    4834621,
                    5680812,
                    6701172,
                    7932503,
                    9410494,
                    11242847,
                    13219062,
                    15081016,
                    17155814,
                    19314747,
                    8550362,
                    10164215,
                    11918938,
                    13648692,
                    15226039,
                    16785196,
                    18501390,
                    19757799,
                    20686918,
                    21628605,
                    22454239,
                    23174294,
                    8322925,
                    9452826,
                    10863958,
                    12607312,
                    14706593,
                    17129565,
                    19844382,
                    23040630,
                    26605473,
                    30686889,
                    34593779,
                    38139640,
                    21289402,
                    25041917,
                    29263397,
                    34024249,
                    39276153,
                    44148285,
                    48827160,
                    52910342,
                    56667095,
                    60216677,
                    62806748,
                    65068149,
                    1219113,
                    1357445,
                    1528098,
                    1735550,
                    2056351,
                    2308582,
                    2644765,
                    3154264,
                    3747553,
                    4320890,
                    4977378,
                    5701579,
                    662850,
                    764900,
                    887498,
                    960155,
                    975199,
                    1039009,
                    1116479,
                    1191336,
                    1183669,
                    1138101,
                    1101832,
                    1056608,
                    3647735,
                    3950849,
                    4286552,
                    4786986,
                    5303507,
                    6005061,
                    6734098,
                    7724976,
                    8523077,
                    9231669,
                    9770575,
                    10276158,
                    22235677,
                    25670939,
                    29788695,
                    33411317,
                    37492953,
                    42404033,
                    47328791,
                    52881328,
                    58179144,
                    63047647,
                    67308928,
                    71158647,
                    5824797,
                    6675501,
                    7688797,
                    8900294,
                    10190285,
                    11457758,
                    12939400,
                    15283050,
                    18252190,
                    21210254,
                    24739869,
                    29170398,
                    50430000,
                    51430000,
                    53292000,
                    54959000,
                    56079000,
                    56179000,
                    56339704,
                    56981620,
                    57866349,
                    58808266,
                    59912431,
                    60776238,
                    157553000,
                    171984000,
                    186538000,
                    198712000,
                    209896000,
                    220239000,
                    232187835,
                    242803533,
                    256894189,
                    272911760,
                    287675526,
                    301139947,
                    2252965,
                    2424959,
                    2598466,
                    2748579,
                    2829526,
                    2873520,
                    2953997,
                    3045153,
                    3149262,
                    3262838,
                    3363085,
                    3447496,
                    5439568,
                    6702668,
                    8143375,
                    9709552,
                    11515649,
                    13503563,
                    15620766,
                    17910182,
                    20265563,
                    22374398,
                    24287670,
                    26084662,
                    26246839,
                    28998543,
                    33796140,
                    39463910,
                    44655014,
                    50533506,
                    56142181,
                    62826491,
                    69940728,
                    76048996,
                    80908147,
                    85262356,
                    1030585,
                    1070439,
                    1133134,
                    1142636,
                    1089572,
                    1261091,
                    1425876,
                    1691210,
                    2104779,
                    2826046,
                    3389578,
                    4018332,
                    4963829,
                    5498090,
                    6120081,
                    6740785,
                    7407075,
                    8403990,
                    9657618,
                    11219340,
                    13367997,
                    15826497,
                    18701257,
                    22211743,
                    2672000,
                    3016000,
                    3421000,
                    3900000,
                    4506497,
                    5216550,
                    6100407,
                    7272406,
                    8381163,
                    9417789,
                    10595811,
                    11746035,
                    3080907,
                    3646340,
                    4277736,
                    4995432,
                    5861135,
                    6642107,
                    7636524,
                    9216418,
                    10704340,
                    11404948,
                    11926563,
                    12311143
                  ],
                  "yaxis": "y"
                }
              ],
              "layout": {
                "legend": {
                  "tracegroupgap": 0
                },
                "margin": {
                  "t": 60
                },
                "template": {
                  "data": {
                    "bar": [
                      {
                        "error_x": {
                          "color": "#2a3f5f"
                        },
                        "error_y": {
                          "color": "#2a3f5f"
                        },
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          }
                        },
                        "type": "bar"
                      }
                    ],
                    "barpolar": [
                      {
                        "marker": {
                          "line": {
                            "color": "#E5ECF6",
                            "width": 0.5
                          }
                        },
                        "type": "barpolar"
                      }
                    ],
                    "carpet": [
                      {
                        "aaxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "baxis": {
                          "endlinecolor": "#2a3f5f",
                          "gridcolor": "white",
                          "linecolor": "white",
                          "minorgridcolor": "white",
                          "startlinecolor": "#2a3f5f"
                        },
                        "type": "carpet"
                      }
                    ],
                    "choropleth": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "choropleth"
                      }
                    ],
                    "contour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "contour"
                      }
                    ],
                    "contourcarpet": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "contourcarpet"
                      }
                    ],
                    "heatmap": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmap"
                      }
                    ],
                    "heatmapgl": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "heatmapgl"
                      }
                    ],
                    "histogram": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "histogram"
                      }
                    ],
                    "histogram2d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2d"
                      }
                    ],
                    "histogram2dcontour": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "histogram2dcontour"
                      }
                    ],
                    "mesh3d": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "type": "mesh3d"
                      }
                    ],
                    "parcoords": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "parcoords"
                      }
                    ],
                    "pie": [
                      {
                        "automargin": true,
                        "type": "pie"
                      }
                    ],
                    "scatter": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter"
                      }
                    ],
                    "scatter3d": [
                      {
                        "line": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatter3d"
                      }
                    ],
                    "scattercarpet": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattercarpet"
                      }
                    ],
                    "scattergeo": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergeo"
                      }
                    ],
                    "scattergl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattergl"
                      }
                    ],
                    "scattermapbox": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scattermapbox"
                      }
                    ],
                    "scatterpolar": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolar"
                      }
                    ],
                    "scatterpolargl": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterpolargl"
                      }
                    ],
                    "scatterternary": [
                      {
                        "marker": {
                          "colorbar": {
                            "outlinewidth": 0,
                            "ticks": ""
                          }
                        },
                        "type": "scatterternary"
                      }
                    ],
                    "surface": [
                      {
                        "colorbar": {
                          "outlinewidth": 0,
                          "ticks": ""
                        },
                        "colorscale": [
                          [
                            0,
                            "#0d0887"
                          ],
                          [
                            0.1111111111111111,
                            "#46039f"
                          ],
                          [
                            0.2222222222222222,
                            "#7201a8"
                          ],
                          [
                            0.3333333333333333,
                            "#9c179e"
                          ],
                          [
                            0.4444444444444444,
                            "#bd3786"
                          ],
                          [
                            0.5555555555555556,
                            "#d8576b"
                          ],
                          [
                            0.6666666666666666,
                            "#ed7953"
                          ],
                          [
                            0.7777777777777778,
                            "#fb9f3a"
                          ],
                          [
                            0.8888888888888888,
                            "#fdca26"
                          ],
                          [
                            1,
                            "#f0f921"
                          ]
                        ],
                        "type": "surface"
                      }
                    ],
                    "table": [
                      {
                        "cells": {
                          "fill": {
                            "color": "#EBF0F8"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "header": {
                          "fill": {
                            "color": "#C8D4E3"
                          },
                          "line": {
                            "color": "white"
                          }
                        },
                        "type": "table"
                      }
                    ]
                  },
                  "layout": {
                    "annotationdefaults": {
                      "arrowcolor": "#2a3f5f",
                      "arrowhead": 0,
                      "arrowwidth": 1
                    },
                    "coloraxis": {
                      "colorbar": {
                        "outlinewidth": 0,
                        "ticks": ""
                      }
                    },
                    "colorscale": {
                      "diverging": [
                        [
                          0,
                          "#8e0152"
                        ],
                        [
                          0.1,
                          "#c51b7d"
                        ],
                        [
                          0.2,
                          "#de77ae"
                        ],
                        [
                          0.3,
                          "#f1b6da"
                        ],
                        [
                          0.4,
                          "#fde0ef"
                        ],
                        [
                          0.5,
                          "#f7f7f7"
                        ],
                        [
                          0.6,
                          "#e6f5d0"
                        ],
                        [
                          0.7,
                          "#b8e186"
                        ],
                        [
                          0.8,
                          "#7fbc41"
                        ],
                        [
                          0.9,
                          "#4d9221"
                        ],
                        [
                          1,
                          "#276419"
                        ]
                      ],
                      "sequential": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ],
                      "sequentialminus": [
                        [
                          0,
                          "#0d0887"
                        ],
                        [
                          0.1111111111111111,
                          "#46039f"
                        ],
                        [
                          0.2222222222222222,
                          "#7201a8"
                        ],
                        [
                          0.3333333333333333,
                          "#9c179e"
                        ],
                        [
                          0.4444444444444444,
                          "#bd3786"
                        ],
                        [
                          0.5555555555555556,
                          "#d8576b"
                        ],
                        [
                          0.6666666666666666,
                          "#ed7953"
                        ],
                        [
                          0.7777777777777778,
                          "#fb9f3a"
                        ],
                        [
                          0.8888888888888888,
                          "#fdca26"
                        ],
                        [
                          1,
                          "#f0f921"
                        ]
                      ]
                    },
                    "colorway": [
                      "#636efa",
                      "#EF553B",
                      "#00cc96",
                      "#ab63fa",
                      "#FFA15A",
                      "#19d3f3",
                      "#FF6692",
                      "#B6E880",
                      "#FF97FF",
                      "#FECB52"
                    ],
                    "font": {
                      "color": "#2a3f5f"
                    },
                    "geo": {
                      "bgcolor": "white",
                      "lakecolor": "white",
                      "landcolor": "#E5ECF6",
                      "showlakes": true,
                      "showland": true,
                      "subunitcolor": "white"
                    },
                    "hoverlabel": {
                      "align": "left"
                    },
                    "hovermode": "closest",
                    "mapbox": {
                      "style": "light"
                    },
                    "paper_bgcolor": "white",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                      "angularaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "radialaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "scene": {
                      "xaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "yaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      },
                      "zaxis": {
                        "backgroundcolor": "#E5ECF6",
                        "gridcolor": "white",
                        "gridwidth": 2,
                        "linecolor": "white",
                        "showbackground": true,
                        "ticks": "",
                        "zerolinecolor": "white"
                      }
                    },
                    "shapedefaults": {
                      "line": {
                        "color": "#2a3f5f"
                      }
                    },
                    "ternary": {
                      "aaxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "baxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      },
                      "bgcolor": "#E5ECF6",
                      "caxis": {
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": ""
                      }
                    },
                    "title": {
                      "x": 0.05
                    },
                    "xaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    },
                    "yaxis": {
                      "automargin": true,
                      "gridcolor": "white",
                      "linecolor": "white",
                      "ticks": "",
                      "title": {
                        "standoff": 15
                      },
                      "zerolinecolor": "white",
                      "zerolinewidth": 2
                    }
                  }
                },
                "xaxis": {
                  "anchor": "y",
                  "domain": [
                    0,
                    1
                  ],
                  "title": {
                    "text": "year"
                  }
                },
                "yaxis": {
                  "anchor": "x",
                  "domain": [
                    0,
                    1
                  ],
                  "title": {
                    "text": "pop"
                  }
                }
              }
            },
            "text/html": "<div>                            <div id=\"f6fe94e4-cc31-4865-b5bd-abf8281e8f47\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"f6fe94e4-cc31-4865-b5bd-abf8281e8f47\")) {                    Plotly.newPlot(                        \"f6fe94e4-cc31-4865-b5bd-abf8281e8f47\",                        [{\"hovertemplate\": \"year=%{x}<br>pop=%{y}<extra></extra>\", \"legendgroup\": \"\", \"line\": {\"color\": \"#636efa\"}, \"mode\": \"lines\", \"name\": \"\", \"orientation\": \"v\", \"showlegend\": false, \"stackgroup\": \"1\", \"type\": \"scatter\", \"x\": [1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007, 1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007], \"xaxis\": \"x\", \"y\": [8425333, 9240934, 10267083, 11537966, 13079460, 14880372, 12881816, 13867957, 16317921, 22227415, 25268405, 31889923, 1282697, 1476505, 1728137, 1984060, 2263554, 2509048, 2780097, 3075321, 3326498, 3428038, 3508512, 3600523, 9279525, 10270856, 11000948, 12760499, 14760787, 17152804, 20033753, 23254956, 26298373, 29072015, 31287142, 33333216, 4232095, 4561361, 4826015, 5247469, 5894858, 6162675, 7016384, 7874230, 8735988, 9875024, 10866106, 12420476, 17876956, 19610538, 21283783, 22934225, 24779799, 26983828, 29341374, 31620918, 33958947, 36203463, 38331121, 40301927, 8691212, 9712569, 10794968, 11872264, 13177000, 14074100, 15184200, 16257249, 17481977, 18565243, 19546792, 20434176, 6927772, 6965860, 7129864, 7376998, 7544201, 7568430, 7574613, 7578903, 7914969, 8069876, 8148312, 8199783, 120447, 138655, 171863, 202182, 230800, 297410, 377967, 454612, 529491, 598561, 656397, 708573, 46886859, 51365468, 56839289, 62821884, 70759295, 80428306, 93074406, 103764241, 113704579, 123315288, 135656790, 150448339, 8730405, 8989111, 9218400, 9556500, 9709100, 9821800, 9856303, 9870200, 10045622, 10199787, 10311970, 10392226, 1738315, 1925173, 2151895, 2427334, 2761407, 3168267, 3641603, 4243788, 4981671, 6066080, 7026113, 8078314, 2883315, 3211738, 3593918, 4040665, 4565872, 5079716, 5642224, 6156369, 6893451, 7693188, 8445134, 9119152, 2791000, 3076000, 3349000, 3585000, 3819000, 4086000, 4172693, 4338977, 4256013, 3607000, 4165416, 4552198, 442308, 474639, 512764, 553541, 619351, 781472, 970347, 1151184, 1342614, 1536536, 1630347, 1639131, 56602560, 65551171, 76039390, 88049823, 100840058, 114313951, 128962939, 142938076, 155975974, 168546719, 179914212, 190010647, 7274900, 7651254, 8012946, 8310226, 8576200, 8797022, 8892098, 8971958, 8658506, 8066057, 7661799, 7322858, 4469979, 4713416, 4919632, 5127935, 5433886, 5889574, 6634596, 7586551, 8878303, 10352843, 12251209, 14326203, 2445618, 2667518, 2961915, 3330989, 3529983, 3834415, 4580410, 5126023, 5809236, 6121610, 7021078, 8390505, 4693836, 5322536, 6083619, 6960067, 7450606, 6978607, 7272485, 8371791, 10150094, 11782962, 12926707, 14131858, 5009067, 5359923, 5793633, 6335506, 7021028, 7959865, 9250831, 10780667, 12467171, 14195809, 15929988, 17696293, 14785584, 17010154, 18985849, 20819767, 22284500, 23796400, 25201900, 26549700, 28523502, 30305843, 31902268, 33390141, 1291695, 1392284, 1523478, 1733638, 1927260, 2167533, 2476971, 2840009, 3265124, 3696513, 4048013, 4369038, 2682462, 2894855, 3150417, 3495967, 3899068, 4388260, 4875118, 5498955, 6429417, 7562011, 8835739, 10238807, 6377619, 7048426, 7961258, 8858908, 9717524, 10599793, 11487112, 12463354, 13572994, 14599929, 15497046, 16284741, 556263527, 637408000, 665770000, 754550000, 862030000, 943455000, 1000281000, 1084035000, 1164970000, 1230075000, 1280400000, 1318683096, 12350771, 14485993, 17009885, 19764027, 22542890, 25094412, 27764644, 30964245, 34202721, 37657830, 41008227, 44227550, 153936, 170928, 191689, 217378, 250027, 304739, 348643, 395114, 454429, 527982, 614382, 710960, 14100005, 15577932, 17486434, 19941073, 23007669, 26480870, 30646495, 35481645, 41672143, 47798986, 55379852, 64606759, 854885, 940458, 1047924, 1179760, 1340458, 1536769, 1774735, 2064095, 2409073, 2800947, 3328795, 3800610, 926317, 1112300, 1345187, 1588717, 1834796, 2108457, 2424367, 2799811, 3173216, 3518107, 3834934, 4133884, 2977019, 3300000, 3832408, 4744870, 6071696, 7459574, 9025951, 10761098, 12772596, 14625967, 16252726, 18013409, 3882229, 3991242, 4076557, 4174366, 4225310, 4318673, 4413368, 4484310, 4494013, 4444595, 4481020, 4493312, 6007797, 6640752, 7254373, 8139332, 8831348, 9537988, 9789224, 10239839, 10723260, 10983007, 11226999, 11416987, 9125183, 9513758, 9620282, 9835109, 9862158, 10161915, 10303704, 10311597, 10315702, 10300707, 10256295, 10228744, 4334000, 4487831, 4646899, 4838800, 4991596, 5088419, 5117810, 5127024, 5171393, 5283663, 5374693, 5468120, 63149, 71851, 89898, 127617, 178848, 228694, 305991, 311025, 384156, 417908, 447416, 496374, 2491346, 2923186, 3453434, 4049146, 4671329, 5302800, 5968349, 6655297, 7351181, 7992357, 8650322, 9319622, 3548753, 4058385, 4681707, 5432424, 6298651, 7278866, 8365850, 9545158, 10748394, 11911819, 12921234, 13755680, 22223309, 25009741, 28173309, 31681188, 34807417, 38783863, 45681811, 52799062, 59402198, 66134291, 73312559, 80264543, 2042865, 2355805, 2747687, 3232927, 3790903, 4282586, 4474873, 4842194, 5274649, 5783439, 6353681, 6939688, 216964, 232922, 249220, 259864, 277603, 192675, 285483, 341244, 387838, 439971, 495627, 551201, 1438760, 1542611, 1666618, 1820319, 2260187, 2512642, 2637297, 2915959, 3668440, 4058319, 4414865, 4906585, 20860941, 22815614, 25145372, 27860297, 30770372, 34617799, 38111756, 42999530, 52088559, 59861301, 67946797, 76511887, 4090500, 4324000, 4491443, 4605744, 4639657, 4738902, 4826933, 4931729, 5041039, 5134406, 5193039, 5238460, 42459667, 44310863, 47124000, 49569000, 51732000, 53165019, 54433565, 55630100, 57374179, 58623428, 59925035, 61083916, 420702, 434904, 455661, 489004, 537977, 706367, 753874, 880397, 985739, 1126189, 1299304, 1454867, 284320, 323150, 374020, 439593, 517101, 608274, 715523, 848406, 1025384, 1235767, 1457766, 1688359, 69145952, 71019069, 73739117, 76368453, 78717088, 78160773, 78335266, 77718298, 80597764, 82011073, 82350671, 82400996, 5581001, 6391288, 7355248, 8490213, 9354120, 10538093, 11400338, 14168101, 16278738, 18418288, 20550751, 22873338, 7733250, 8096218, 8448233, 8716441, 8888628, 9308479, 9786480, 9974490, 10325429, 10502372, 10603863, 10706290, 3146381, 3640876, 4208858, 4690773, 5149581, 5703430, 6395630, 7326406, 8486949, 9803875, 11178650, 12572928, 2664249, 2876726, 3140003, 3451418, 3811387, 4227026, 4710497, 5650262, 6990574, 8048834, 8807818, 9947814, 580653, 601095, 627820, 601287, 625361, 745228, 825987, 927524, 1050938, 1193708, 1332459, 1472041, 3201488, 3507701, 3880130, 4318137, 4698301, 4908554, 5198399, 5756203, 6326682, 6913545, 7607651, 8502814, 1517453, 1770390, 2090162, 2500689, 2965146, 3055235, 3669448, 4372203, 5077347, 5867957, 6677328, 7483763, 2125900, 2736300, 3305200, 3722800, 4115700, 4583700, 5264500, 5584510, 5829696, 6495918, 6762476, 6980412, 9504000, 9839000, 10063000, 10223422, 10394091, 10637171, 10705535, 10612740, 10348684, 10244684, 10083313, 9956108, 147962, 165110, 182053, 198676, 209275, 221823, 233997, 244676, 259012, 271192, 288030, 301931, 372000000, 409000000, 454000000, 506000000, 567000000, 634000000, 708000000, 788000000, 872000000, 959000000, 1034172547, 1110396331, 82052000, 90124000, 99028000, 109343000, 121282000, 136725000, 153343000, 169276000, 184816000, 199278000, 211060000, 223547000, 17272000, 19792000, 22874000, 26538000, 30614000, 35480679, 43072751, 51889696, 60397973, 63327987, 66907826, 69453570, 5441766, 6248643, 7240260, 8519282, 10061506, 11882916, 14173318, 16543189, 17861905, 20775703, 24001816, 27499638, 2952156, 2878220, 2830000, 2900100, 3024400, 3271900, 3480000, 3539900, 3557761, 3667233, 3879155, 4109086, 1620914, 1944401, 2310904, 2693585, 3095893, 3495918, 3858421, 4203148, 4936550, 5531387, 6029529, 6426679, 47666000, 49182000, 50843200, 52667100, 54365564, 56059245, 56535636, 56729703, 56840847, 57479469, 57926999, 58147733, 1426095, 1535090, 1665128, 1861096, 1997616, 2156814, 2298309, 2326606, 2378618, 2531311, 2664659, 2780132, 86459025, 91563009, 95831757, 100825279, 107188273, 113872473, 118454974, 122091325, 124329269, 125956499, 127065841, 127467972, 607914, 746559, 933559, 1255058, 1613551, 1937652, 2347031, 2820042, 3867409, 4526235, 5307470, 6053193, 6464046, 7454779, 8678557, 10191512, 12044785, 14500404, 17661452, 21198082, 25020539, 28263827, 31386842, 35610177, 8865488, 9411381, 10917494, 12617009, 14781241, 16325320, 17647518, 19067554, 20711375, 21585105, 22215365, 23301725, 20947571, 22611552, 26420307, 30131000, 33505000, 36436000, 39326000, 41622000, 43805450, 46173816, 47969150, 49044790, 160000, 212846, 358266, 575003, 841934, 1140357, 1497494, 1891487, 1418095, 1765345, 2111561, 2505559, 1439529, 1647412, 1886848, 2186894, 2680018, 3115787, 3086876, 3089353, 3219994, 3430388, 3677780, 3921278, 748747, 813338, 893143, 996380, 1116779, 1251524, 1411807, 1599200, 1803195, 1982823, 2046772, 2012649, 863308, 975950, 1112796, 1279406, 1482628, 1703617, 1956875, 2269414, 1912974, 2200725, 2814651, 3193942, 1019729, 1201578, 1441863, 1759224, 2183877, 2721783, 3344074, 3799845, 4364501, 4759670, 5368585, 6036914, 4762912, 5181679, 5703324, 6334556, 7082430, 8007166, 9171477, 10568642, 12210395, 14165114, 16473477, 19167654, 2917802, 3221238, 3628608, 4147252, 4730997, 5637246, 6502825, 7824747, 10014249, 10419991, 11824495, 13327079, 6748378, 7739235, 8906385, 10154878, 11441462, 12845381, 14441916, 16331785, 18319502, 20476091, 22662365, 24821286, 3838168, 4241884, 4690372, 5212416, 5828158, 6491649, 6998256, 7634008, 8416215, 9384984, 10580176, 12031795, 1022556, 1076852, 1146757, 1230542, 1332786, 1456688, 1622136, 1841240, 2119465, 2444741, 2828858, 3270065, 516556, 609816, 701016, 789309, 851334, 913025, 992040, 1042663, 1096202, 1149818, 1200206, 1250882, 30144317, 35015548, 41121485, 47995559, 55984294, 63759976, 71640904, 80122492, 88111030, 95895146, 102479927, 108700891, 800663, 882134, 1010280, 1149500, 1320500, 1528000, 1756032, 2015133, 2312802, 2494803, 2674234, 2874127, 413834, 442829, 474528, 501035, 527678, 560073, 562548, 569473, 621621, 692651, 720230, 684736, 9939217, 11406350, 13056604, 14770296, 16660670, 18396941, 20198730, 22987397, 25798239, 28529501, 31167783, 33757175, 6446316, 7038035, 7788944, 8680909, 9809596, 11127868, 12587223, 12891952, 13160731, 16603334, 18473780, 19951656, 20092996, 21731844, 23634436, 25870271, 28466390, 31528087, 34680442, 38028578, 40546538, 43247867, 45598081, 47761980, 485831, 548080, 621392, 706640, 821782, 977026, 1099010, 1278184, 1554253, 1774766, 1972153, 2055080, 9182536, 9682338, 10332057, 11261690, 12412593, 13933198, 15796314, 17917180, 20326209, 23001113, 25873917, 28901790, 10381988, 11026383, 11805689, 12596822, 13329874, 13852989, 14310401, 14665278, 15174244, 15604464, 16122830, 16570613, 1994794, 2229407, 2488550, 2728150, 2929100, 3164900, 3210650, 3317166, 3437674, 3676187, 3908037, 4115771, 1165790, 1358828, 1590597, 1865490, 2182908, 2554598, 2979423, 3344353, 4017939, 4609572, 5146848, 5675356, 3379468, 3692184, 4076008, 4534062, 5060262, 5682086, 6437188, 7332638, 8392818, 9666252, 11140655, 12894865, 33119096, 37173340, 41871351, 47287752, 53740085, 62209173, 73039376, 81551520, 93364244, 106207839, 119901274, 135031164, 3327728, 3491938, 3638919, 3786019, 3933004, 4043205, 4114787, 4186147, 4286357, 4405672, 4535591, 4627926, 507833, 561977, 628164, 714775, 829050, 1004533, 1301048, 1593882, 1915208, 2283635, 2713462, 3204897, 41346560, 46679944, 53100671, 60641899, 69325921, 78152686, 91462088, 105186881, 120065004, 135564834, 153403524, 169270617, 940080, 1063506, 1215725, 1405486, 1616384, 1839782, 2036305, 2253639, 2484997, 2734531, 2990875, 3242173, 1555876, 1770902, 2009813, 2287985, 2614104, 2984494, 3366439, 3886512, 4483945, 5154123, 5884491, 6667147, 8025700, 9146100, 10516500, 12132200, 13954700, 15990099, 18125129, 20195924, 22430449, 24748122, 26769436, 28674757, 22438691, 26072194, 30325264, 35356600, 40850141, 46850962, 53456774, 60017788, 67185766, 75012988, 82995088, 91077287, 25730551, 28235346, 30329617, 31785378, 33039545, 34621254, 36227381, 37740710, 38370697, 38654957, 38625976, 38518241, 8526050, 8817650, 9019800, 9103000, 8970450, 9662600, 9859650, 9915289, 9927680, 10156415, 10433867, 10642836, 2227000, 2260000, 2448046, 2648961, 2847132, 3080828, 3279001, 3444468, 3585176, 3759430, 3859606, 3942491, 257700, 308700, 358900, 414024, 461633, 492095, 517810, 562035, 622191, 684810, 743981, 798094, 16630000, 17829327, 18680721, 19284814, 20662648, 21658597, 22356726, 22686371, 22797027, 22562458, 22404337, 22276056, 2534927, 2822082, 3051242, 3451079, 3992121, 4657072, 5507565, 6349365, 7290203, 7212583, 7852401, 8860588, 60011, 61325, 65345, 70787, 76595, 86796, 98593, 110812, 125911, 145608, 170372, 199579, 4005677, 4419650, 4943029, 5618198, 6472756, 8128505, 11254672, 14619745, 16945857, 21229759, 24501530, 27601038, 2755589, 3054547, 3430243, 3965841, 4588696, 5260855, 6147783, 7171347, 8307920, 9535314, 10870037, 12267493, 6860147, 7271135, 7616060, 7971222, 8313288, 8686367, 9032824, 9230783, 9826397, 10336594, 10111559, 10150265, 2143249, 2295678, 2467895, 2662190, 2879013, 3140897, 3464522, 3868905, 4260884, 4578212, 5359092, 6144562, 1127000, 1445929, 1750200, 1977600, 2152400, 2325300, 2651869, 2794552, 3235865, 3802309, 4197776, 4553009, 3558137, 3844277, 4237384, 4442238, 4593433, 4827803, 5048043, 5199318, 5302888, 5383010, 5410052, 5447502, 1489518, 1533070, 1582962, 1646912, 1694510, 1746919, 1861252, 1945870, 1999210, 2011612, 2011497, 2009245, 2526994, 2780415, 3080153, 3428839, 3840161, 4353666, 5828892, 6921858, 6099799, 6633514, 7753310, 9118773, 14264935, 16151549, 18356657, 20997321, 23935810, 27129932, 31140029, 35933379, 39964159, 42835005, 44433622, 43997828, 28549870, 29841614, 31158061, 32850275, 34513161, 36439000, 37983310, 38880702, 39549438, 39855442, 40152517, 40448191, 7982342, 9128546, 10421936, 11737396, 13016733, 14116836, 15410151, 16495304, 17587060, 18698655, 19576783, 20378239, 8504667, 9753392, 11183227, 12716129, 14597019, 17104986, 20367053, 24725960, 28227588, 32160729, 37090298, 42292929, 290243, 326741, 370006, 420690, 480105, 551425, 649901, 779348, 962344, 1054486, 1130269, 1133066, 7124673, 7363802, 7561588, 7867931, 8122293, 8251648, 8325260, 8421403, 8718867, 8897619, 8954175, 9031088, 4815000, 5126000, 5666000, 6063000, 6401400, 6316424, 6468126, 6649942, 6995447, 7193761, 7361757, 7554661, 3661549, 4149908, 4834621, 5680812, 6701172, 7932503, 9410494, 11242847, 13219062, 15081016, 17155814, 19314747, 8550362, 10164215, 11918938, 13648692, 15226039, 16785196, 18501390, 19757799, 20686918, 21628605, 22454239, 23174294, 8322925, 9452826, 10863958, 12607312, 14706593, 17129565, 19844382, 23040630, 26605473, 30686889, 34593779, 38139640, 21289402, 25041917, 29263397, 34024249, 39276153, 44148285, 48827160, 52910342, 56667095, 60216677, 62806748, 65068149, 1219113, 1357445, 1528098, 1735550, 2056351, 2308582, 2644765, 3154264, 3747553, 4320890, 4977378, 5701579, 662850, 764900, 887498, 960155, 975199, 1039009, 1116479, 1191336, 1183669, 1138101, 1101832, 1056608, 3647735, 3950849, 4286552, 4786986, 5303507, 6005061, 6734098, 7724976, 8523077, 9231669, 9770575, 10276158, 22235677, 25670939, 29788695, 33411317, 37492953, 42404033, 47328791, 52881328, 58179144, 63047647, 67308928, 71158647, 5824797, 6675501, 7688797, 8900294, 10190285, 11457758, 12939400, 15283050, 18252190, 21210254, 24739869, 29170398, 50430000, 51430000, 53292000, 54959000, 56079000, 56179000, 56339704, 56981620, 57866349, 58808266, 59912431, 60776238, 157553000, 171984000, 186538000, 198712000, 209896000, 220239000, 232187835, 242803533, 256894189, 272911760, 287675526, 301139947, 2252965, 2424959, 2598466, 2748579, 2829526, 2873520, 2953997, 3045153, 3149262, 3262838, 3363085, 3447496, 5439568, 6702668, 8143375, 9709552, 11515649, 13503563, 15620766, 17910182, 20265563, 22374398, 24287670, 26084662, 26246839, 28998543, 33796140, 39463910, 44655014, 50533506, 56142181, 62826491, 69940728, 76048996, 80908147, 85262356, 1030585, 1070439, 1133134, 1142636, 1089572, 1261091, 1425876, 1691210, 2104779, 2826046, 3389578, 4018332, 4963829, 5498090, 6120081, 6740785, 7407075, 8403990, 9657618, 11219340, 13367997, 15826497, 18701257, 22211743, 2672000, 3016000, 3421000, 3900000, 4506497, 5216550, 6100407, 7272406, 8381163, 9417789, 10595811, 11746035, 3080907, 3646340, 4277736, 4995432, 5861135, 6642107, 7636524, 9216418, 10704340, 11404948, 11926563, 12311143], \"yaxis\": \"y\"}],                        {\"legend\": {\"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"xaxis\": {\"anchor\": \"y\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"year\"}}, \"yaxis\": {\"anchor\": \"x\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"pop\"}}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('f6fe94e4-cc31-4865-b5bd-abf8281e8f47');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 75,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:08:27.619Z",
          "iopub.execute_input": "2020-11-05T15:08:27.628Z",
          "iopub.status.idle": "2020-11-05T15:08:27.674Z",
          "shell.execute_reply": "2020-11-05T15:08:27.685Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "outputs": [
        {
          "output_type": "execute_result",
          "execution_count": 73,
          "data": {
            "text/plain": "          country continent  year  lifeExp       pop   gdpPercap iso_alpha  \\\n0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG   \n1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG   \n2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG   \n3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG   \n4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG   \n...           ...       ...   ...      ...       ...         ...       ...   \n1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE   \n1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE   \n1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE   \n1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE   \n1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE   \n\n      iso_num  \n0           4  \n1           4  \n2           4  \n3           4  \n4           4  \n...       ...  \n1699      716  \n1700      716  \n1701      716  \n1702      716  \n1703      716  \n\n[1704 rows x 8 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>country</th>\n      <th>continent</th>\n      <th>year</th>\n      <th>lifeExp</th>\n      <th>pop</th>\n      <th>gdpPercap</th>\n      <th>iso_alpha</th>\n      <th>iso_num</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Afghanistan</td>\n      <td>Asia</td>\n      <td>1952</td>\n      <td>28.801</td>\n      <td>8425333</td>\n      <td>779.445314</td>\n      <td>AFG</td>\n      <td>4</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Afghanistan</td>\n      <td>Asia</td>\n      <td>1957</td>\n      <td>30.332</td>\n      <td>9240934</td>\n      <td>820.853030</td>\n      <td>AFG</td>\n      <td>4</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Afghanistan</td>\n      <td>Asia</td>\n      <td>1962</td>\n      <td>31.997</td>\n      <td>10267083</td>\n      <td>853.100710</td>\n      <td>AFG</td>\n      <td>4</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Afghanistan</td>\n      <td>Asia</td>\n      <td>1967</td>\n      <td>34.020</td>\n      <td>11537966</td>\n      <td>836.197138</td>\n      <td>AFG</td>\n      <td>4</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Afghanistan</td>\n      <td>Asia</td>\n      <td>1972</td>\n      <td>36.088</td>\n      <td>13079460</td>\n      <td>739.981106</td>\n      <td>AFG</td>\n      <td>4</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>1699</th>\n      <td>Zimbabwe</td>\n      <td>Africa</td>\n      <td>1987</td>\n      <td>62.351</td>\n      <td>9216418</td>\n      <td>706.157306</td>\n      <td>ZWE</td>\n      <td>716</td>\n    </tr>\n    <tr>\n      <th>1700</th>\n      <td>Zimbabwe</td>\n      <td>Africa</td>\n      <td>1992</td>\n      <td>60.377</td>\n      <td>10704340</td>\n      <td>693.420786</td>\n      <td>ZWE</td>\n      <td>716</td>\n    </tr>\n    <tr>\n      <th>1701</th>\n      <td>Zimbabwe</td>\n      <td>Africa</td>\n      <td>1997</td>\n      <td>46.809</td>\n      <td>11404948</td>\n      <td>792.449960</td>\n      <td>ZWE</td>\n      <td>716</td>\n    </tr>\n    <tr>\n      <th>1702</th>\n      <td>Zimbabwe</td>\n      <td>Africa</td>\n      <td>2002</td>\n      <td>39.989</td>\n      <td>11926563</td>\n      <td>672.038623</td>\n      <td>ZWE</td>\n      <td>716</td>\n    </tr>\n    <tr>\n      <th>1703</th>\n      <td>Zimbabwe</td>\n      <td>Africa</td>\n      <td>2007</td>\n      <td>43.487</td>\n      <td>12311143</td>\n      <td>469.709298</td>\n      <td>ZWE</td>\n      <td>716</td>\n    </tr>\n  </tbody>\n</table>\n<p>1704 rows × 8 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 73,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T15:00:55.250Z",
          "iopub.execute_input": "2020-11-05T15:00:55.257Z",
          "iopub.status.idle": "2020-11-05T15:00:55.272Z",
          "shell.execute_reply": "2020-11-05T15:00:55.279Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ax = plt.gca()  # gca stands for 'get current axis'\n",
        "plot_kind = 'line'\n",
        "tmpdf1 = df[df['pe'].isin(['PrgEnv-gnu'])]\n",
        "for cubeside in (tmpdf1['cubeside'].unique()):\n",
        "    tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]\n",
        "    tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x',\n",
        "                label=f'cubeside={cubeside} GNU/9', ax=ax) #, logy=True, secondary_y=True)\n",
        "\n",
        "tmpdf1 = df[df['pe'].isin(['PrgEnv-cray'])]\n",
        "for cubeside in (tmpdf1['cubeside'].unique()):\n",
        "    tmpdf2 = tmpdf1.loc[(tmpdf1['cubeside'] == cubeside)]\n",
        "    tmpdf2.plot(kind=plot_kind, x='mpi', y='elapsed', marker='x',\n",
        "                label=f'cubeside={cubeside} CCE/10', ax=ax) #, logy=True, secondary_y=True)\n",
        "\n",
        "# plt.xticks(tmpdf2['mpi'], tmpdf2['mpi'])\n",
        "ax.grid(True)\n",
        "plt.title(f'Walltime (PrgEnv-gnu)')\n",
        "ax.yaxis.set_label('Elapsed / s')\n"
      ],
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<Figure size 432x288 with 1 Axes>",
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "execution_count": 3,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T13:40:02.265Z",
          "iopub.execute_input": "2020-11-05T13:40:02.271Z",
          "iopub.status.idle": "2020-11-05T13:40:02.630Z",
          "shell.execute_reply": "2020-11-05T13:40:02.680Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "outputs": [],
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# plt.show()\n",
        "# plt.savefig('eff.png')\n",
        "print(f'cubeside={cubeside}')\n",
        "tmpdf2"
      ],
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cubeside=2698\n"
          ]
        },
        {
          "output_type": "execute_result",
          "execution_count": 13,
          "data": {
            "text/plain": "     mpi  openmp  cubeside  steps gitcommit           pe  elapsed  \\\n8  32768       1      2698      1   f982fde  PrgEnv-cray  162.804   \n\n   domain_distribute  mpi_synchronizeHalos  BuildTree  FindNeighbors  Density  \\\n8            10.3754               90.0528     4.1116         5.4494   2.5907   \n\n   EquationOfState     IAD  MomentumEnergyIAD  Timestep  UpdateQuantities  \\\n8           0.0087  3.0592             5.0892   41.4034            0.1247   \n\n   EnergyConservation  SmoothingLength  \n8              0.2202           0.0364  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>mpi</th>\n      <th>openmp</th>\n      <th>cubeside</th>\n      <th>steps</th>\n      <th>gitcommit</th>\n      <th>pe</th>\n      <th>elapsed</th>\n      <th>domain_distribute</th>\n      <th>mpi_synchronizeHalos</th>\n      <th>BuildTree</th>\n      <th>FindNeighbors</th>\n      <th>Density</th>\n      <th>EquationOfState</th>\n      <th>IAD</th>\n      <th>MomentumEnergyIAD</th>\n      <th>Timestep</th>\n      <th>UpdateQuantities</th>\n      <th>EnergyConservation</th>\n      <th>SmoothingLength</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>8</th>\n      <td>32768</td>\n      <td>1</td>\n      <td>2698</td>\n      <td>1</td>\n      <td>f982fde</td>\n      <td>PrgEnv-cray</td>\n      <td>162.804</td>\n      <td>10.3754</td>\n      <td>90.0528</td>\n      <td>4.1116</td>\n      <td>5.4494</td>\n      <td>2.5907</td>\n      <td>0.0087</td>\n      <td>3.0592</td>\n      <td>5.0892</td>\n      <td>41.4034</td>\n      <td>0.1247</td>\n      <td>0.2202</td>\n      <td>0.0364</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 13,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T14:03:07.114Z",
          "iopub.execute_input": "2020-11-05T14:03:07.118Z",
          "iopub.status.idle": "2020-11-05T14:03:07.132Z",
          "shell.execute_reply": "2020-11-05T14:03:07.138Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [
        "    plt.close('all')"
      ],
      "outputs": [],
      "execution_count": 8,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        },
        "execution": {
          "iopub.status.busy": "2020-11-05T13:53:31.372Z",
          "iopub.execute_input": "2020-11-05T13:53:31.377Z",
          "iopub.status.idle": "2020-11-05T13:53:31.383Z",
          "shell.execute_reply": "2020-11-05T13:53:31.387Z"
        }
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "outputs": [],
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "jupyter": {
          "source_hidden": false,
          "outputs_hidden": false
        },
        "nteract": {
          "transient": {
            "deleting": false
          }
        }
      }
    }
  ],
  "metadata": {
    "kernel_info": {
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.8.5",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "kernelspec": {
      "argv": [
        "python",
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}"
      ],
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "nteract": {
      "version": "0.26.0"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
# John Vogel 10/22/2024 john.vogel123@gmail.com

# to activate the virtual environment
# type this in your shell
#source .venv/bin/activate
#cd work

# put this in .bashrc to tell python where to look for source
#PYTHONPATH=/home/jvogel/Documents/aiWorkrepo/dataScienceWork/scripts
#export PYTHONPATH

import os
import argparse
from argparse import RawTextHelpFormatter # needed to support backslash n
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import scipy
import math

import my_functions as mf

# setup the project descriptor and usage how-to
parser = argparse.ArgumentParser(
   formatter_class=RawTextHelpFormatter,
   usage='\n --no additional arguments are needed',
   description='Program to show python basic plotting capabilities \
   \n--REPORT 1: calc mean median and mode \
   \n--PLOT 1: ??? \
   ',
   epilog='send feedback to john.vogel123@gmail.com \
')
parser.parse_args()

print("JPV: Creating some random floating point data")
X_Fdata = np.random.random(50) * 100
Y_Fdata = np.random.random(50) * 100
X_Ndata = np.random.normal(loc=0, scale=1, size=1000)
Y_Ndata = np.random.normal(loc=0, scale=1, size=1000)

print("JPV: Creating some random integer data")
X_Idata = []; Y_Idata=[]
for val in (np.random.random(50) * 100) : X_Idata.append(int(val))
for val in (np.random.random(50) * 100) : Y_Idata.append(int(val))
#print(X_Idata); print(Y_Idata); print(X_Fdata); print(Y_Fdata)
#print(X_Ndata); print(Y_Ndata);

#plt.scatter(X_Idata , Y_Idata, c="red", marker="*", s=150, alpha=0.3)
#plt.scatter(X_Fdata , Y_Fdata, c="blue", marker="*", s=150, alpha=0.3)
#plt.scatter(X_data , Y_data, c="#000000")
#plt.scatter(X_data , Y_data, c="#0f0") # using rgb format
plt.boxplot(X_Ndata)
plt.show()


#fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(10, 8))
#fig.supxlabel("Box and Violin Plots", fontsize=20, color='blue') # add labels to the canvas

#axes[0].boxplot(plotDataNormal)
#axes[0].set_title('Normal')
#axes[1].violinplot(plotDataNormal)
#axes[1].set_title('Normal')
#axes[2].boxplot(plotDataOutlierLow)
#axes[2].set_title('Outlier Low')


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
   prog='plotSamples.py',
   description='Program to show python basic plotting capabilities \
   \n--REPORT 1: calc mean median and mode \
   \n--PLOT 1: ??? \
   ',
   epilog='send feedback to john.vogel123@gmail.com \
   \nNOTE: Alt F4 will close the plot if it fills the screen! \
   \nNOTE: PYTHONPATH needs to be defined if running outside scripts folder \
')
parser.parse_args()

print("JPV: Creating data for mean, median, and mode analysis")
print("JPV: Calculating mean, median, and mode")
print("JPV: Reporting stats to terminal")
print("JPV: Plotting using box and violin plots")
##################################################
# Sample data 
plotDataNormal = np.array([1,2,3,4,5,6,7,8,9])
plotDataOutlierHigh = np.array([1,2,3,4,5,6,7,8,9,14.51])
plotDataOutlierLow= np.array([-4.51,1,2,3,4,5,6,7,8,9])
plotDataTest= np.array([-4.51,1,2,3,4,5,6,7,8,9])

meanResult = np.mean(plotDataNormal)
medianResult = scipy.ndimage.median(plotDataNormal)
modeResult = stats.mode(plotDataNormal)
dataLength = len(plotDataNormal)
iqrResult = stats.iqr(plotDataNormal)
q1Result = np.quantile(plotDataNormal,0.25)
q3Result = np.quantile(plotDataNormal,0.75)
print("JPV: Mean, median, mode source data: ", plotDataNormal)
print("JPV: Data has",dataLength, "elements.\n MEAN: ", meanResult,
"\n MEDIAN: ",medianResult,"\n MODE: ", modeResult[0],
"\n Q1: ", q1Result, "\n Q3: ", q3Result, "\n IQR: ",iqrResult
)

fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(10, 8))
fig.supxlabel("Box and Violin Plots", fontsize=20, color='blue') # add labels to the canvas

axes[0].boxplot(plotDataNormal)
axes[0].set_title('Normal')
axes[1].violinplot(plotDataNormal)
axes[1].set_title('Normal')
axes[2].boxplot(plotDataOutlierLow)
axes[2].set_title('Outlier Low')
axes[3].boxplot(plotDataOutlierHigh)
axes[3].set_title('Outlier High')
axes[4].violinplot(plotDataOutlierHigh)
axes[4].set_title('Outlier High')
axes[5].boxplot(plotDataTest)
axes[5].set_title('TEST')
axes[6].violinplot(plotDataTest)
axes[6].set_title('TEST')

#plt.boxplot(plotDataNormal)
#plt.violinplot(plotDataNormal)
plt.show()


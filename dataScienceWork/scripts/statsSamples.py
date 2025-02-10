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
   \n--PLOT 1: a csv file is loaded and a scatter plot is made \
   \n--PLOT 2: random data is created and a scatter plot is made \
   \n--PLOTS 3-6: plotting using trig and log and squared function \
   \n--PLOT 7: plot a single trig function \
   ',
   epilog='send feedback to john.vogel123@gmail.com \
   \nNOTE: Alt F4 will close the plot if it fills the screen! \
   \nNOTE: PYTHONPATH needs to be defined if running outside scripts folder \
')
parser.parse_args()

print("JPV: Creating data for mean, median, and mode analysis")
print("JPV: Calculating mean, median, and mode")
print("JPV: Reporting stats to terminal")
##################################################
# Sample data for mean, median, and mode calculation
rawData = np.array([1,1,2,2,2,3,4,4])
meanResult = np.mean(rawData)
medianResult = scipy.ndimage.median(rawData)
modeResult = stats.mode(rawData)
dataLength = len(rawData)
print("JPV: Mean, median, mode source data: ", rawData)
print("JPV: Data has",dataLength, "elements, a mean of", meanResult,
", a median of",medianResult,", and a mode of", modeResult[0])
plt.scatter(rawData, rawData, c="#000000")
plt.show()


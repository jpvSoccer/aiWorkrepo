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
   description='Program to analyze real estate data \
   ',
   epilog='send feedback to john.vogel123@gmail.com \
')
parser.parse_args()

csvFile = "../data/raw-house-data.csv"
print("JPV: Loading csv",csvFile,"into dataframe")
#  1  2     3     4        5        6            7
# id,date,price,bedrooms,bathrooms,sqft_living,sqft_lot,
#  8         9       10     11       12     13
# floors,waterfront,view,condition,grade,sqft_above,
#  14             15        16          17     18  19     20            21
# sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15

##################################################
# Read csv into a dataframe and setup plot
df = pd.read_csv(csvFile)
#df = pd.read_csv(csvFile, nrows=2)
#mf.printCsvStats(df) # homegrown function to print some stats

#print("JPV: the average sqft: $",df.sqft_living.mean())
#print("JPV: median sqft: $",df.sqft_living.median())
#print("JPV: the average sqft_lot: $",df.sqft_lot.mean())
#print("JPV: median sqft_lot: $",df.sqft_lot.median())
#print("JPV: the average price: $",f"{int(df.price.mean()):,}")
#print("JPV: median price: $",f"{int(df.price.median()):,}")

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 10))
fig.supxlabel("Real Estate Data Analysis", fontsize=20, color='blue')
plt.subplots_adjust(hspace=0.6)

axes[0,0].boxplot(df.sqft_living, vert=False)
axes[0,0].set_title('sqft_living',color='r', fontweight='bold', fontsize=25)
axes[1,0].boxplot(df.sqft_lot, vert=False)
axes[1,0].set_title('sqft_lot',color='r', fontweight='bold', fontsize=25)
axes[2,0].boxplot(df.sqft_basement, vert=False)
axes[2,0].set_title('sqft_basement',color='r', fontweight='bold', fontsize=25)
axes[3,0].boxplot(df.sqft_above, vert=False)
axes[3,0].set_title('sqft_above',color='r', fontweight='bold', fontsize=25)
axes[0,1].boxplot(df.price, vert=False)
axes[0,1].set_title('price',color='b', fontweight='bold', fontsize=25)
axes[1,1].boxplot(df.yr_built, vert=False)
axes[1,1].set_title('yr_built',color='b', fontweight='bold', fontsize=25)
axes[2,1].boxplot(df.floors, vert=False)
axes[2,1].set_title('floors',color='b', fontweight='bold', fontsize=25)
axes[3,1].boxplot(df.sqft_living15, vert=False)
axes[3,1].set_title('sqft_living15',color='b', fontweight='bold', fontsize=25)

plt.show()

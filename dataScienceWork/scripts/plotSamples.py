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

print("JPV: Loading csv into dataframe")
print("JPV: Creating scatter plot from dataframe")
##################################################
# Read csv into a dataframe and setup plot
df = pd.read_csv("../data/raw-house-data.csv")
#df = pd.read_csv("../data/raw-house-data.csv", nrows=2)
#mf.printCsvStats(df) # homegrown function to print some stats
plt.scatter(df.id, df.price, c="#000000")
plt.scatter(df.price, df.bedrooms, c="red")
#plt.show()

print("JPV: Creating random data scatter plot")
print("JPV: Make scatter plot from random")
##################################################
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100
plt.scatter(X_data , Y_data, c="red", marker="*", s=150, alpha=0.3)
# alpha is for transparency if you have overlapping data points
#plt.scatter(X_data , Y_data, c="#000000")
#plt.scatter(X_data , Y_data, c="#0f0") # using rgb format
#print(X_data)
#plt.show()

print("JPV: Creating data for a multiple plot sheet")
print("JPV: Creating 4 plots on one sheet")
##################################################
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
with np.errstate(divide='ignore'):
    y4 = np.log10(x) # temp ignore warning about divide by zero

# Create a figure canvas (fig) and an array pointing to subplots (with axes)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle("Main Title", fontsize=20, color='red')
fig.supxlabel("My Horizontal label", fontsize=20, color='blue') # add labels to the canvas
fig.supylabel("My Vertical label", fontsize=20, color='blue') # add labels to the canvas

# Plot data on each subplot
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Sine Wave')
axes[0, 0].set_xlabel('Degrees in Radians', fontsize=20, color='red')
axes[0, 0].set_ylabel('Sine of X', fontsize=20, color='red')
axes[0, 1].plot(x, y2, color='red')
axes[0, 1].set_title('Cosine Wave')
axes[1, 0].plot(x, y3, linestyle='dashed')
axes[1, 0].set_title('X Squared')
axes[1, 1].plot(x, y4, linestyle='dashed')
axes[1, 1].set_title('Log10 X')
#axes[1, 1].remove() # Remove the last subplot

# Adjust layout
plt.tight_layout()
#plt.show()

print("JPV: Creating a single plot")
##################################################
#create a single plot
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)
fig2, ax = plt.subplots() # only creates one plot
fig2.suptitle("Secondary Title")
ax.plot(x, y)
ax.set_title('A single plot')

print("JPV: Drawing plots")
##################################################
# Show the plots
plt.show()


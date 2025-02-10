# to activate the virtual environment
# type this in your shell
#source .venv/bin/activate
#cd work

# put this in .bashrc to tell python where to look for source
#PYTHONPATH=/home/jvogel/Documents/aiWorkrepo/dataScienceWork/scripts
#export PYTHONPATH

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import my_functions as mf

# read csv into a dataframe and print some stats
df = pd.read_csv("../data/raw-house-data.csv")
#df = pd.read_csv("../data/raw-house-data.csv", nrows=2)

mf.printCsvStats(df) #function to print some stats
plt.scatter(df.id, df.price, c="#000000")
plt.scatter(df.price, df.bedrooms, c="red")
plt.show()


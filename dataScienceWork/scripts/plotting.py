import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100
plt.scatter(X_data , Y_data, c="red", marker="*", s=150, alpha=0.3)
# alpha is for transparency if you have overlapping data points
#plt.scatter(X_data , Y_data, c="#000000")
#plt.scatter(X_data , Y_data, c="#0f0") # using rgb format
#print(X_data)
plt.show()
#plt.close('all')  #does not work

# Alt F4 will close the plot if it fills the screen

# read csv into a dataframe
'''
df = pd.read_csv("data/raw-house-data.csv")
print(df.shape)
rows , columns = df.shape
print(rows)

print("\nprint summary of dataframe\n",df)
print("\nprint dataframe header\n",df.head()) 
print("\nprint just two rows\n",df.head(2))
print("\nprint 4 rows: starting at row 2\n",df[2:6])
'''


import pandas as pd

# read csv into a dataframe
df = pd.read_csv("data/raw-house-data.csv")
print(df.shape)
rows , columns = df.shape
print(rows)

print("\nprint summary of dataframe\n",df)
print("\nprint dataframe header\n",df.head()) 
print("\nprint just two rows\n",df.head(2))
print("\nprint 4 rows: starting at row 2\n",df[2:6])


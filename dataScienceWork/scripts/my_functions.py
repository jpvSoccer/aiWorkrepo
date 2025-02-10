
# function that takes a dataFrame pointer and prints basic stats
# nothing is returned
def printCsvStats(dataFrame):
   rows , columns = dataFrame.shape # make a tupple from the shape
   print("Data shape:", dataFrame.shape)
   print("CSV number of rows:",rows)
   print("CSV number of columns:",columns)
   print("\nCSV column names:",dataFrame.columns)
   print("\nprint dataframe header\n",dataFrame.head)
   print("\nprint 3 rows: starting at row 2\n",dataFrame[3:6])
   print("\nprint summary of dataframe\n",df)
   print("\nprint dataframe header\n",df.head())
   print("\nprint just two rows\n",df.head(2))
   return


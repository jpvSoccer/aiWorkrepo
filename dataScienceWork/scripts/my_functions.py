
# function that takes a dataFrame pointer and prints basic stats
# nothing is returned
def printCsvStats(dataFrame):
   rows , columns = dataFrame.shape # make a tupple from the shape
   print("JPV: Printing some stats on the dataframe:")
   print("JPV: Data shape:", dataFrame.shape)
   print("JPV: Number of rows:",rows)
   print("JPV: Number of columns:",columns)
   print("\nJPV: Column names:\n",dataFrame.columns)
   print("\nJPV: print dataframe header\n",dataFrame.head)
   print("\nJPV: print 3 rows: starting at row 3\n",dataFrame[3:6])
   print("\nJPV: print summary of dataframe\n",dataFrame)
   print("\nJPV: print dataframe header\n",dataFrame.head())
   print("\nJPV: print first three rows\n",dataFrame.head(2))
   return


# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=1, names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=[0], skiprows=1, names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

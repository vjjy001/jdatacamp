# Load a sheet into a DataFrame by name: df1
#print(type())
df1 = xl.parse(xl.sheet_names[1]) #by name '2004'

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

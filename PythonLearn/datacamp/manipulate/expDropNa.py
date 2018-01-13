# Select the 'age' and 'cabin' columns: df
df = titanic.loc[:,['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info())

'''
Drop columns from the titanic DataFrame that have more than 1000 missing values by specifying the thresh and axis keyword arguments. Print the output of .info() from this.
'''
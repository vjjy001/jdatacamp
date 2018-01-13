# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather.loc[:,['Min TemperatureF','Mean TemperatureF','Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = 5/9*(temps_f-32)

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F','C')

# Print first 5 rows of temps_c
print(temps_c.head())
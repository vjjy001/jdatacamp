# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s,g1900s,g2000s],axis=1)

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())

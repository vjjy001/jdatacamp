# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)
#percentile means th position of data 50 means median of data

# Print the result
print(ptiles_vers)

#[ 3.3     4.      4.35    4.9775]
# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')  #index_col use specific column as index
election2 = pd.read_csv(filename)
# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]
#results2 = election.loc[:,['winner', 'total', 'voters']]
# Print the output of results.head()
print(results.head())

# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue','Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.winner.map(red_vs_blue)
#Seriers use map dataframe use apply for each element

# Print the output of election.head()
print(election.head())

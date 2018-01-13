for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    #evaluates as a string with the value of medal replacing %s in the format string.
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name,names=columns,header=0,index_col='Country')

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals,axis='columns')

# Print medals
print(medals)

'''
bronze  silver   gold  bronze  silver   gold
France           475.0   461.0    NaN   475.0   461.0    NaN
Germany          454.0     NaN  407.0   454.0     NaN  407.0
Italy              NaN   394.0  460.0     NaN   394.0  460.0
Soviet Union     584.0   627.0  838.0   584.0   627.0  838.0
United Kingdom   505.0   591.0  498.0   505.0   591.0  498.0
'''
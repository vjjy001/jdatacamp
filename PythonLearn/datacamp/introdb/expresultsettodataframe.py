# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)

'''
[('California', 36609002),
 ('Texas', 24214127),
 ('New York', 19465159),
 ('Florida', 18257662),
 ('Illinois', 12867077)]
 
 state  population
0  California    36609002
1       Texas    24214127
2    New York    19465159
3     Florida    18257662
4    Illinois    12867077
'''
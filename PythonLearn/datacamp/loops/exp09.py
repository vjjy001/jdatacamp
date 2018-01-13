# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for l,r in cars.iterrows():
    cars.loc[l,'COUNTRY']=str.upper(r['country'])

# Print cars
print(cars)
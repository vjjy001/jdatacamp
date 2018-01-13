# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])
#print(type(cars.loc[['JAP']]))
# Print out observations for Australia and Egypt
#print(cars)
print(cars.iloc[[1,6]])
print(cars.loc[['AUS','EG']])
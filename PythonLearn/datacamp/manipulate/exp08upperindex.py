# Create the list of new indexes: new_idx
new_idx = [ idx.upper() for idx in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
'''
 eggs  salt  spam
JAN    47  12.0    17
FEB   110  50.0    31
MAR   221  89.0    72
APR    77  87.0    20
MAY   132   NaN    52
JUN   205  60.0    55

cubes = []
for i in range(10):
    cubes.append(i**3)
	
[ i**3 for i in range(10)]
'''
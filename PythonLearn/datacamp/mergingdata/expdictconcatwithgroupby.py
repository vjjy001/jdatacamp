# Make the list of tuples: month_list
month_list = [('january',jan),('february',feb),('march',mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])
'''
                         Units
         Company               
february Acme Coporation     34
         Hooli               30
         Initech             30
         Mediacore           45
         Streeplex           37
january  Acme Coporation     76
         Hooli               70
         Initech             37
         Mediacore           15
         Streeplex           50
march    Acme Coporation      5
         Hooli               37
         Initech             68
         Mediacore           68
         Streeplex           40

<script.py> output:
                              Units
             Company               
    february Acme Coporation     34
             Hooli               30
             Initech             30
             Mediacore           45
             Streeplex           37
    january  Acme Coporation     76
             Hooli               70
             Initech             37
             Mediacore           15
             Streeplex           50
    march    Acme Coporation      5
             Hooli               37
             Initech             68
             Mediacore           68
             Streeplex           40
                        Units
             Company         
    february Mediacore     45
    january  Mediacore     15
    march    Mediacore     68

'''
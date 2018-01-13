# Concatenate dataframes: february
february = pd.concat(dataframes,keys=['Hardware', 'Software', 'Service'],axis=1) 

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
#slice_2_8 = february.loc['____':'____', ____[:, '____']]
slice_2_8 = february.loc['2015-02-02':'2015-02-08',idx[:,'Company']]
# Print slice_2_8
print(slice_2_8)


'''
                          Hardware         Software Service
                                 Company          Company Company
    Date                                                         
    2015-02-02 08:33:01              NaN            Hooli     NaN
    2015-02-02 20:54:49        Mediacore              NaN     NaN
    2015-02-03 14:14:18              NaN          Initech     NaN
    2015-02-04 15:36:29              NaN        Streeplex     NaN
    2015-02-04 21:52:45  Acme Coporation              NaN     NaN
    2015-02-05 01:53:06              NaN  Acme Coporation     NaN
    2015-02-05 22:05:03              NaN              NaN   Hooli
    2015-02-07 22:58:10  Acme Coporation              NaN     NaN

'''
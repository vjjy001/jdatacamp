# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals,axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())


'''
NOC           VIE       YUG       ZAM       ZIM  ZZX  
Edition                                               
1992          NaN       NaN       NaN       NaN  NaN  
1996          NaN  0.013986  0.000538       NaN  NaN  
2000     0.000496  0.012903       NaN       NaN  NaN  
2004          NaN       NaN       NaN  0.001502  NaN  
2008     0.000490       NaN       NaN  0.001959  NaN  

'''
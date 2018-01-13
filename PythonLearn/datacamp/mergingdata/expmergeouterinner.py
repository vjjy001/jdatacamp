# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers,revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers,revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers,revenue_and_sales,how='outer',on=['city','state'])

# Print merge_outer_on
print(merge_outer_on)

#compare with join
#revenue_and_sales.set_index('city')
#revenue_and_sales.join
'''

   city state  units     branch  branch_id   manager  revenue
0  Mendocino    CA      1  Mendocino       47.0     Brett    200.0
1     Denver    CO      4     Denver       20.0      Joel     83.0
2     Austin    TX      2     Austin       10.0  Charlers    100.0
          city state  units       branch  branch_id   manager  revenue
0    Mendocino    CA      1    Mendocino       47.0     Brett    200.0
1       Denver    CO      4       Denver       20.0      Joel     83.0
2       Austin    TX      2       Austin       10.0  Charlers    100.0
3  Springfield    MO      5  Springfield       31.0     Sally      NaN
4  Springfield    IL      1          NaN        NaN       NaN      NaN
5  Springfield    IL      1          NaN       30.0       NaN      4.0
6  Springfield    MO      5          NaN        NaN       NaN      NaN
          city state  units_x       branch  branch_id_x   manager  \
0    Mendocino    CA        1    Mendocino         47.0     Brett   
1       Denver    CO        4       Denver         20.0      Joel   
2       Austin    TX        2       Austin         10.0  Charlers   
3  Springfield    MO        5  Springfield         31.0     Sally   
4  Springfield    IL        1          NaN          NaN       NaN   

   branch_id_y  revenue  units_y  
0         47.0    200.0        1  
1         20.0     83.0        4  
2         10.0    100.0        2  
3          NaN      NaN        5  
4         30.0      4.0        1

'''
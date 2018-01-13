# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue,sales,on=['city','state'],how='right')

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales,managers,left_on=['city','state'],right_on=['branch','state'],how='left')

# Print sales_and_managers
print(sales_and_managers)

''' 
branch_id         city  revenue state  units
0       10.0       Austin    100.0    TX      2
1       20.0       Denver     83.0    CO      4
2       30.0  Springfield      4.0    IL      1
3       47.0    Mendocino    200.0    CA      1
4        NaN  Springfield      NaN    MO      5
          city state  units       branch  branch_id   manager
0    Mendocino    CA      1    Mendocino       47.0     Brett
1       Denver    CO      4       Denver       20.0      Joel
2       Austin    TX      2       Austin       10.0  Charlers
3  Springfield    MO      5  Springfield       31.0     Sally
4  Springfield    IL      1          NaN        NaN       NaN
'''
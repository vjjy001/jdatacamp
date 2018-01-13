# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index="weekday",columns="city",values="visitors")

# Print the pivoted DataFrame
print(visitors_pivot)

'''
weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5
'''
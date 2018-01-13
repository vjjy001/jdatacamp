# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers,on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers,on='branch_id')

# Print merge_by_id
print(merge_by_id)

'''
 branch_id_x         city  revenue  branch_id_y   manager
    0           10       Austin      100           10  Charlers
    1           20       Denver       83           20      Joel
    2           30  Springfield        4           31     Sally
    3           47    Mendocino      200           47     Brett
  
  branch_id     city_x  revenue     city_y   manager
    0         10     Austin      100     Austin  Charlers
    1         20     Denver       83     Denver      Joel
    2         47  Mendocino      200  Mendocino     Brett
	
	'''
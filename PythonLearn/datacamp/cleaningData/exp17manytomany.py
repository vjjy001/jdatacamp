# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))

'''
 name    lat    long  ident   site       dated  taken person quant  \
0    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   rad   
1    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   sal   
2    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   rad   
3    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   sal   
4    DR-1 -49.85 -128.57    844   DR-1  1932-03-22    844    roe   rad   

'''
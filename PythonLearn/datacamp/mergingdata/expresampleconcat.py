# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],axis=1,join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())

'''
               China        US
Year                          
1971-12-31  0.988860  1.073188
1981-12-31  0.972048  1.749631
1991-12-31  0.962528  0.922811
2001-12-31  2.492511  0.720398
2011-12-31  4.623958  0.460947
2021-12-31  3.789936  0.377506

'''
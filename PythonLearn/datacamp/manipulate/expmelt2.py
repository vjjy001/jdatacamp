# Melt users: skinny
skinny = pd.melt(users,id_vars=['weekday','city'])
#id_vars means which column not to melt
#value_vars means which cols melt

# Print skinny
print(skinny)


'''
weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5
'''
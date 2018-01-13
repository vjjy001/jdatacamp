# Create the Boolean Series: under10
under10 = (titanic.age<10).map({True:'under 10',False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10,'pclass'])['survived'].mean()
print(survived_mean_2)


def filter_over_10(g):
    return g['age']-g['age'].mean() <10
    
ut = titanic.groupby(['pclass']).apply(filter_over_10)
#ut = titanic.groupby(['pclass']).filter(filter_over_10)
print(ut)

sf = pd.Series([1, 1, 2, 3, 3, 3])

def map_sf(s):
    if s > 2:
        return 'high'
    else:
        return 'low'

sf.map(map_sf)
#sf.groupby(sf).apply(map_sf)   
# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index='Edition',columns='NOC',values='Athlete',aggfunc='count')

# Slice medals_won_by_country: cold_war_usa_usr_medals
cold_war_usa_usr_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]

# Create most_medals 
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')
#sums = cold_war_usa_usr_medals.sum(axis='columns')
#cold_war_usa_usr_medals['total'] =sums
# Print most_medals.value_counts()
print(most_medals.value_counts())

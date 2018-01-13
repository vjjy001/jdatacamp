# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival and print the result
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)
'''
def filter_c_deck(gp):
    c_list = gp['cabin'].str.contains('C')
    return c_list.values[0]
    
by_sex.filter(filter_c_deck)
'''
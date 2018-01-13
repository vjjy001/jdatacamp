# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = pd.pivot_table(users,index='weekday',aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = pd.pivot_table(users,index='weekday',aggfunc=sum,margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)

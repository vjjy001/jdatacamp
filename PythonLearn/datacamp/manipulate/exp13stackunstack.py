# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level="weekday")

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level="weekday"))


'''

               visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12
'''
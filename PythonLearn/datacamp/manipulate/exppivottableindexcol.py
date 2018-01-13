# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = pd.pivot_table(users,index='weekday',columns='city')

# Print by_city_day
print(by_city_day)

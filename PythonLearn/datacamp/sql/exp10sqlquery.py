# Execute query and store records in DataFrame: df
df = pd.read_sql_query('select * from playlisttrack inner join track on playlisttrack.trackid=track.trackid WHERE Milliseconds < 250000',engine)

# Print head of DataFrame
print(df.head())

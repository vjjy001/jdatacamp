# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']
print(tweet_time)
# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[12:20] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

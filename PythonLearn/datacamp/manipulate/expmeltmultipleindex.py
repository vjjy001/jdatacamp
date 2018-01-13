# Set the new index: users_idx
users_idx = users.set_index(['weekday','city'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx,col_level=0)
#use col_level to melt

# Print the key-value pairs
print(kv_pairs)

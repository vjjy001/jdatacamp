# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
#stmt = stmt.select_from(
#    ____(____, census.columns.____ == state_fact.columns.____))
stmt = stmt.select_from(census.join(state_fact,census.columns.state==state_fact.columns.name))
# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

#print(result)
# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))

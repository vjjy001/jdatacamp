# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
#stmt = update(state_fact).values(____ == ____)
stmt = update(state_fact).values(fips_state=36)
# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())

'''
[('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '0', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
1
[('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '36', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]

'''

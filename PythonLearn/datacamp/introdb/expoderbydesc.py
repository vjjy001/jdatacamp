# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])


'''
[('Wyoming', 'M', 0, 3236, 4066), ('Wyoming', 'M', 1, 3245, 4159), ('Wyoming', 'M', 2, 3102, 4058), ('Wyoming', 'M', 3, 3103, 3745), ('Wyoming', 'M', 4, 3166, 3633), ('Wyoming', 'M', 5, 3157, 3647), ('Wyoming', 'M', 6, 3421, 3667), ('Wyoming', 'M', 7, 3503, 3498), ('Wyoming', 'M', 8, 3577, 3479), ('Wyoming', 'M', 9, 3744, 3512)]
'''

# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
'''
stmt = select([____,
               (func.sum(____ * ____) /
                func.sum(____)).label(____)
               ])
'''
stmt = select([census.columns.sex,
        (func.sum(census.columns.pop2000 * census.columns.age) / func.sum(census.columns.pop2000)).label('average_age')
        ])
# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for result in results:
    print(result.sex, result.average_age)

	
	'''
	F 37
M 34
'''
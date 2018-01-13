# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt

stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

'''
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female'),
     func.sum(case([
         (census.columns.sex=='F',census.columns.pop2000),
         ],else_=0)
         ).label('grouppopbystate'),
     (cast(func.sum(census.columns.pop2000), Float) * 100    ).label('totalbystate')
])

'''
# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)

#print(results)


'''
 Alabama 51.8324077702
    Alaska 49.3014978935
    Arizona 50.2236130306
    Arkansas 51.2699284622
    California 50.3523321490
    Colorado 49.8476706030
	
	'''
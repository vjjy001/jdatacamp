# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select managers and counts of their employees: stmt
stmt = select([managers.columns.name,managers.columns.id,employees.columns.id, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
#stmt = stmt.where(managers.columns.id==employees.columns.mgr)
stmt = stmt.select_from(employees.join(managers,employees.columns.mgr == managers.columns.id))
# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)

'''
    ('FILLMORE', 10, 13, 3)
('GARFIELD', 6, 12, 4)
('HARDING', 2, 4, 2)
('JACKSON', 9, 14, 4)

'''
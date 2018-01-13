# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
'''
female_pop2000 = func.sum(
    ____([
        (____ == ____, ____)
    ], else_=____))
'''
female_pop2000=func.sum(
    case(
        [
            (census.columns.sex =='F',census.columns.pop2000)
        ],    
            else_=0
    
    )
)
# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000: stmt
#stmt = select([female_pop2000 / total_pop2000* 100])
stmt = select([census.columns.state,female_pop2000 / total_pop2000* 100]).group_by(census.columns.state)
# Execute the query and store the scalar result: percent_female
#percent_female = connection.execute(stmt).scalar()
percent_female = connection.execute(stmt).fetchall()
# Print the percentage
print(percent_female)

'''
[('Alabama', Decimal('51.8324077702')), ('Alaska', Decimal('49.3014978935')), ('Arizona', Decimal('50.2236130306')), ('Arkansas', Decimal('51.2699284622')), ('California', Decimal('50.3523321490')), ('Colorado', Decimal('49.8476706030')), ('Connecticut', Decimal('51.6681650713')), ('Delaware', Decimal('51.6110973356')), ('District of Columbia', Decimal('53.1296261417')), ('Florida', Decimal('51.3648800117')), ('Georgia', Decimal('51.1140835034')), ('Hawaii', Decimal('51.1180118369')), ('Idaho', Decimal('49.9897262390')), ('Illinois', Decimal('51.1122423480')), ('Indiana', Decimal('50.9548031330')), ('Iowa', Decimal('50.9503983425')), ('Kansas', Decimal('50.8218641078')), ('Kentucky', Decimal('51.3268703693')), ('Louisiana', Decimal('51.7535159655')), ('Maine', Decimal('51.5057081342')), ('Maryland', Decimal('51.9357554997')), ('Massachusetts', Decimal('51.8430235713')), ('Michigan', Decimal('50.9724651832')), ('Minnesota', Decimal('50.4933294430')), ('Mississippi', Decimal('51.9222948179')), ('Missouri', Decimal('51.4688860264')), ('Montana', Decimal('50.3220269073')), ('Nebraska', Decimal('50.8584549336')), ('Nevada', Decimal('49.3673636138')), ('New Hampshire', Decimal('50.8580198450')), ('New Jersey', Decimal('51.5171395613')), ('New Mexico', Decimal('51.0471720798')), ('New York', Decimal('51.8345386515')), ('North Carolina', Decimal('51.4822623221')), ('North Dakota', Decimal('50.5006936323')), ('Ohio', Decimal('51.4655035002')), ('Oklahoma', Decimal('51.1136245708')), ('Oregon', Decimal('50.4294670362')), ('Pennsylvania', Decimal('51.7404347305')), ('Rhode Island', Decimal('52.0734339190')), ('South Carolina', Decimal('51.7307212977')), ('South Dakota', Decimal('50.5258358137')), ('Tennessee', Decimal('51.4306896994')), ('Texas', Decimal('50.5157216642')), ('Utah', Decimal('49.9729527511')), ('Vermont', Decimal('51.0185732099')), ('Virginia', Decimal('51.6572524472')), ('Washington', Decimal('50.5185650872')), ('West Virginia', Decimal('51.4004231809')), ('Wisconsin', Decimal('50.6148645265')), ('Wyoming', Decimal('49.9459554265'))]

'''

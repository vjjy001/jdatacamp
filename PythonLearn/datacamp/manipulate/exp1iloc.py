# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])

'''
 state   total      Obama     Romney  winner  voters
county                                                       
Adams        PA   41973  35.482334  63.112001  Romney   61156
Allegheny    PA  614671  56.640219  42.185820   Obama  924351
Armstrong    PA   28322  30.696985  67.901278  Romney   42147
Beaver       PA   80015  46.032619  52.637630  Romney  115157
Bedford      PA   21444  22.057452  76.986570  Romney   32189
'''
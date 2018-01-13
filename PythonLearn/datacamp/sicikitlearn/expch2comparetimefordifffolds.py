
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg,X,y,cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg,X,y,cv=10)
print(np.mean(cvscores_10))

'''
In [2]: %timeit cvscores_3
The slowest run took 158.95 times longer than the fastest. This could mean that an intermediate result is being cached.
10000000 loops, best of 3: 48.4 ns per loop

In [3]: %timeit cvscores_10
The slowest run took 294.58 times longer than the fastest. This could mean that an intermediate result is being cached.

'''
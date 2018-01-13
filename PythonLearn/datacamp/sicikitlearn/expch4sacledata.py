# Import scale
from sklearn.preprocessing import scale
# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X))) 
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled))) 
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))

'''
ean of Unscaled Features: [[  7.     0.27   0.36 ...,   3.     0.45   8.8 ]
 [  6.3    0.3    0.34 ...,   3.3    0.49   9.5 ]
 [  8.1    0.28   0.4  ...,   3.26   0.44  10.1 ]
 ..., 
 [  6.5    0.24   0.19 ...,   2.99   0.46   9.4 ]
 [  5.5    0.29   0.3  ...,   3.34   0.38  12.8 ]
 [  6.     0.21   0.38 ...,   3.26   0.32  11.8 ]]
Standard Deviation of Unscaled Features: [[  1.72096961e-01  -8.17699008e-02   2.13280202e-01 ...,  -1.24692128e+00
   -3.49184257e-01  -1.39315246e+00]
 [ -6.57501128e-01   2.15895632e-01   4.80011213e-02 ...,   7.40028640e-01
    1.34184656e-03  -8.24275678e-01]
 [  1.47575110e+00   1.74519434e-02   5.43838363e-01 ...,   4.75101984e-01
   -4.36815783e-01  -3.36667007e-01]
 ..., 
 [ -4.20473102e-01  -3.79435433e-01  -1.19159198e+00 ...,  -1.31315295e+00
   -2.61552731e-01  -9.05543789e-01]
 [ -1.60561323e+00   1.16673788e-01  -2.82557040e-01 ...,   1.00495530e+00
   -9.62604939e-01   1.85757201e+00]
 [ -1.01304317e+00  -6.77100966e-01   3.78559282e-01 ...,   4.75101984e-01
   -1.48839409e+00   1.04489089e+00]]
Mean of Scaled Features: 2.7314972981668206e-15
Standard Deviation of Scaled Features: 0.9999999999999999

Mean of Unscaled Features: 18.432687072460002
Standard Deviation of Unscaled Features: 41.54494764094571
Mean of Scaled Features: 2.7314972981668206e-15
Standard Deviation of Scaled Features: 0.9999999999999999

'''
from mystatlib import ecdf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot


lc = pd.read_csv('LC.csv')
#lc.info()

vol = lc['Volume']
price = lc['Close']

#analyse the lc stock data
print(type(vol))
#type(price)
#first check price correlcted with volume
pvcor = np.cov(price,vol)
print(pvcor)

#check volume and price ecdf
x_vol,y_vol = ecdf(vol)

#check normal
#np.random.normal()

plt.subplot(4,1,1)
plt.plot(x_vol,y_vol,marker='.',linestyle='none')
#plt.
plt.xlabel('volume')
plt.ylabel('ecdf')

plt.subplot(4,1,2)
x_price,y_price = ecdf(price)
plt.plot(x_price,y_price,marker='.',linestyle='none')
plt.xlabel('price')
plt.ylabel('ecdf')

subplot(4,1,3)
plt.hist(vol,normed=True)
plt.xlabel('vol')
plt.ylabel('hist')

subplot(4,1,4)
plt.hist(price,normed=True)
plt.xlabel('price')
plt.ylabel('hist')

plt.show()
'''
testData = [ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1]
x, y = ecdf(testData)

print(x,y)
'''       


        

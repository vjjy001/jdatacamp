# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
#df.fraction.plot(ax=axes[0], kind='hist', bins=30, ____=____, range=(0,.3))
df.fraction.plot(ax=axes[0],kind='hist',bins=30,normed=True,range=(0,0.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1],kind='hist',bins=30,range=(0,0.3),cumulative=True,normed=True)
plt.show()



'''
 total_bill   tip     sex smoker  day    time  size  fraction
0       16.99  1.01  Female     No  Sun  Dinner     2  0.059447
1       10.34  1.66    Male     No  Sun  Dinner     3  0.160542
2       21.01  3.50    Male     No  Sun  Dinner     3  0.166587
3       23.68  3.31    Male     No  Sun  Dinner     2  0.139780
4       24.59  3.61  Female     No  Sun  Dinner     4  0.146808

'''

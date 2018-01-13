# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
#sns.lmplot(x='weight',y='hp',data=auto,col='origin')
sns.lmplot(x='weight',y='hp',data=auto,row='origin')
# Display the plot
plt.show()

#draw seperate figure
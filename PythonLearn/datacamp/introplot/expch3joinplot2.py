# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp',y='mpg',data=auto,kind='hex')

# Display the plot
plt.show()

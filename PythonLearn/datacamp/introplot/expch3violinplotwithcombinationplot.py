# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl',y='hp',data=auto,inner=None,color='lightgray')

# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl',y='hp',data=auto,jitter=True,size=1.5)

# Display the plot
plt.show()
#stripplot is used to view univarate for distribution
# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl',y='hp',data=auto,jitter=True,size=3)


#Overlapping points can be difficult to distinguish in strip plots. The argument jitter=True helps spread out overlapping point
# Display the plot
plt.show()

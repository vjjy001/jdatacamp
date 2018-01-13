# Generate a scatter plot
#df.plot(____=____, ____='hp', ____='mpg', ____=sizes)
df.plot(x='hp',y='mpg',kind='scatter',s=sizes)
#df.plot(x='hp',y='mpg',kind='line')
# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()

'''
# Generate a scatter plot
#df.plot(____=____, ____='hp', ____='mpg', ____=sizes)
df.plot(x='hp',y='mpg',kind='scatter',s=sizes)
#df.plot(x='hp',y='mpg',kind='line')
# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()
'''
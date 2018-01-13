# Make a scatter plot
plt.plot(versicolor_petal_length,versicolor_petal_width,marker='.',linestyle='none')
#plt.plot(versicolor_petal_length,versicolor_petal_width,kind='scatter')

# Set margins
plt.margins(0.02)

# Label the axes
plt.xlabel('versicolor_petal_length')
plt.ylabel('versicolor_petal_width')


# Show the result
plt.show()

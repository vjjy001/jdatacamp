# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp,mpg,gridsize=(100,100),extent=(40,235,8,48))

           
# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()

# Import matplotlib.pyplot
import matplotlib.pyplot

df['Existing Zoning Sqft'].describe()
# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plot.show()

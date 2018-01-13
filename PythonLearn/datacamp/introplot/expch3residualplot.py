
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')
#sns.lmplot(x='mpg', y='cyl', ____=auto, ____='green')

# Display the plot
plt.show()

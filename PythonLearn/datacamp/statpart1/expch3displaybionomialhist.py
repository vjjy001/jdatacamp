# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults,normed=True,bins=bins)

# Set margins
plt.margins(0.02)

# Label axes
plt.xlabel('bins')
plt.ylabel('num')


# Show the plot
plt.show()

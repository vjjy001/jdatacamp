# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc['2010-08','Temperature'].max()
print(august_max)

# Resample the August 2011 temperatures in df_clean by day and aggregate the maximum value: august_2011
august_2011 = df_clean.loc['2011-08','dry_bulb_faren'].resample('D').max()

# Filter out days in august_2011 where the value exceeded august_max: august_2011_high
august_2011_high =august_2011[august_2011>august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(bins=25,kind='hist',normed=True,cumulative=True)

# Display the plot
plt.show()

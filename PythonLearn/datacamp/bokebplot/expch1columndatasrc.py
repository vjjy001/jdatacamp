# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle(x='Year',y='Time',source=source,color='color')

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)


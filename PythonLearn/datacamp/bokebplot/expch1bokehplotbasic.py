# Import figure from bokeh.plotting
#from bokeh.plotting import ____

# Import output_file and show from bokeh.io
#from bokeh.io import , ____
from bokeh.io import output_file, show
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(female_literacy,fertility)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)

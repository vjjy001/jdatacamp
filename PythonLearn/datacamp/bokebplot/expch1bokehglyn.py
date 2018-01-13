# Create the figure: p
#p = ____(____='fertility', ____='female_literacy (% population)')
p = figure(x_axis_label='fetility',y_axis_label='female_literacy (% population)')
# Add a circle glyph to the figure p
p.circle(fertility_latinamerica,female_literacy_latinamerica) #circle means marker

# Add an x glyph to the figure p
p.x(fertility_africa,female_literacy_africa) #x means marker

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)

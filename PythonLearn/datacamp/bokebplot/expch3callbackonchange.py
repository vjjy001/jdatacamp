# Define a callback function: callback
'''
____ ____(____, ____, ____):

    # Read the current value of the slider: scale
    scale = ____

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = ____

    # Update source with the new data values
    source.data = {'x': ____, 'y': ____}
'''
def callback(attr,old,new):
    #scale=slider.value#read current value
    new_y=np.sin(scale/x)
    #print(old)
    #print(new)
    source.data={'x':x,'y':new_y}
    
# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)
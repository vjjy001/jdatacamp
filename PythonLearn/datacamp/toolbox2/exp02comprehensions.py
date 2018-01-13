# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [f if len(f)>=7 else '' for f in fellowship]

# Print the new list
print(new_fellowship)

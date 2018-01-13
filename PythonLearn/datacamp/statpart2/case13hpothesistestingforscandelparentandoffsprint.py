# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted,bd_offspring_scandens)


# Compute p-value: p
p = np.sum(perm_replicates >= heritability(bd_parent_scandens,bd_offspring_scandens)) / len(perm_replicates)

# Print the p-value
print('p-val =', p)


'''
You get a p-value of zero, which means that none of the 10,000 
permutation pairs replicates you drew had a heritability high enough to match that which was observed. This strongly suggests that beak depth is heritable in G. scandens, just not as much as in G. fortis. If you like, you can plot a 
histogram of the heritability replicates to get a feel for how extreme of a value of heritability you might expect by chance.
 p-val = 0.0
'''
'''
A bootstrap test for identical distributions

In the video, we looked at a one-sample test, but we can do two sample tests. 
We can even test the same hypothesis that we tested with a permutation test: that 
the Frog A and Frog B have identically distributed impact forces. To do this test on 
two arrays with n1 and n2 entries, we do a very similar procedure as a permutation test. W
e concatenate the arrays, generate a bootstrap sample from it, and take the first n1 
entries of the bootstrap sample as belonging to the first data set and the last n2 as 
belonging to the second. We then compute the test statistic, e.g., the difference of means, 
to get a bootstrap replicate. The p-value is the number of bootstrap replicates for which 
the test statistic is less than what was observed.
Now, you will perform a bootstrap test of the hypothesis that Frog A and Frog B 
have identical distributions of impact forces using the difference of means test statistic.

The two arrays are available to you as force_a and force_b
'''


# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a,force_b)

# Concatenate forces: forces_concat
forces_concat = np.concatenate([force_a,force_b])

# Initialize bootstrap replicates: bs_replicates
bs_replicates = np.empty(10000)

for i in range(10000):
    # Generate bootstrap sample
    bs_sample = np.random.choice(forces_concat, size=len(forces_concat))
    
    # Compute replicate
    bs_replicates[i] = diff_of_means(bs_sample[:len(force_a)],
                                     bs_sample[len(force_b):])

# Compute and print p-value: p
p = np.sum(bs_replicates>=empirical_diff_means) / 10000
print('p-value =', p)


'''
data
[ 1.612,  0.605,  0.327,  0.946,  0.541,  1.539,  0.529,  0.628,
        1.453,  0.297,  0.703,  0.269,  0.751,  0.245,  1.182,  0.515,
        0.435,  0.383,  0.457,  0.73 ]

[ 0.172,  0.142,  0.037,  0.453,  0.355,  0.022,  0.502,  0.273,
        0.72 ,  0.582,  0.198,  0.198,  0.597,  0.516,  0.815,  0.402,
        0.605,  0.711,  0.614,  0.468]
'''

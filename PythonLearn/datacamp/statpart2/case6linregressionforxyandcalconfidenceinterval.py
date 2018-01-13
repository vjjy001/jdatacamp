# Compute the linear regressions
slope_1975, intercept_1975 = np.polyfit(bl_1975,bd_1975,deg=1)
slope_2012, intercept_2012 = np.polyfit(bl_2012,bd_2012,deg=1)

# Perform pairs bootstrap for the linear regressions
bs_slope_reps_1975, bs_intercept_reps_1975 = \
        draw_bs_pairs_linreg(bl_1975,bd_1975,size=10000)
bs_slope_reps_2012, bs_intercept_reps_2012 = \
        draw_bs_pairs_linreg(bl_2012,bd_2012,size=10000)

# Compute confidence intervals of slopes
slope_conf_int_1975 = np.percentile(bs_slope_reps_1975,[2.5,97.5])
slope_conf_int_2012 = np.percentile(bs_slope_reps_2012,[2.5,97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975,[2.5,97.5])

intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012,[2.5,97.5])


# Print the results
print('1975: slope =', slope_1975,
      'conf int =', slope_conf_int_1975)
print('1975: intercept =', intercept_1975,
      'conf int =', intercept_conf_int_1975)
print('2012: slope =', slope_2012,
      'conf int =', slope_conf_int_2012)
print('2012: intercept =', intercept_2012,
      'conf int =', intercept_conf_int_2012)


'''
1975: slope = 0.465205169161 conf int = [ 0.33560342  0.59306474]
1975: intercept = 2.39087523658 conf int = [ 0.6006951   4.20941893]
2012: slope = 0.462630358835 conf int = [ 0.33248119  0.60168161]
2012: intercept = 2.97724749824 conf int = [ 1.14783629  4.72748212]
'''
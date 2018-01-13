'''
Permutation test on frog data

The average strike force of Frog A was 0.71 Newtons (N), and that of Frog B was 0.42 N for a difference of 0.29 N. It is possible the frogs strike with the same force and this observed difference was by chance. You will compute the probability of getting at least a 0.29 N difference in mean strike force under the hypothesis that the distributions of strike forces for the two frogs are identical. We use a permutation test with a test statistic of the difference of means to test this hypothesis.

For your convenience, the data has been stored in the arrays force_a and force_b.

'''

#这个实验的目的是想知道a青蛙和b青蛙是不是一样的
#所以我们需要做hypothesis test 来验证
#这里的null hypothesis 假设他们是一样的
#alternative hypothesis 他们不一样
#现在我们测试出a青蛙平均弹跳力是0.71, b青蛙0.42  ma-mb =0.29
#所以我们要了解如果假设两种娃是一样的 0.29 的差别出现这个概率是是多少

#因为a和b 我们假设他们是一样 所以我们可以使用permutation testing。 注意permutation test 
#就是用于验证当两组数据一样的时候 把他们打乱重新分配，然后多次实验得出分布图。 然后统计
#pvalue（x=0.29）的概率是多少
#如果这个概率是 < 0.05 说明是小概率事件 从而null hypothesis 不成立

import numpy as np
force_a = np.array([ 1.612,  0.605,  0.327,  0.946,  0.541,  1.539,  0.529,  0.628,
        1.453,  0.297,  0.703,  0.269,  0.751,  0.245,  1.182,  0.515,
        0.435,  0.383,  0.457,  0.73 ])

force_b = np.array([ 0.172,  0.142,  0.037,  0.453,  0.355,  0.022,  0.502,  0.273,
        0.72 ,  0.582,  0.198,  0.198,  0.597,  0.516,  0.815,  0.402,
        0.605,  0.711,  0.614,  0.468])

def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) -np.mean(data_2)

    return diff

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a,force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = draw_perm_reps(force_a, force_b,
                                 diff_of_means, size=10000)

# Compute p-value: p
#注意这里perm-relicates 实际上就是通过大量实验得出这个实验的概率分布图
#然后p(x=0.29) 说明这个概率在这个分布图里面出现的概率是多少
p = np.sum(perm_replicates >= 0.29) / len(perm_replicates)

# Print the result
print('p-value =', p)
'''
p-value = 0.0063 这个概率说明了
The p-value tells you that there is about a 0.6% chance that you would get the difference 
of means observed in the experiment if frogs were exactly the same
中文翻译就是 这说明了如果是相同的弹跳力的青蛙，出现0.29牛顿不一样的概率只有0.6%. 从而推翻了我
们的假设 。说明青蛙不相等的。
''''

#这里我们使用z statistic 来统计这个事件
meanexp = np.mean(perm_replicates)
sigm = np.sqrt(np.std(perm_replicates))
ps = (meanexp-empirical_diff_means) / sigm
# h0 means diff is 0.29
#  0.84 std of sample distribution so the h0 is true so we accept the a and b is  different

'''
The p-value tells you that there is about a 0.6% chance that you would get the 
difference of means observed in the experiment if frogs were exactly the same. 
A p-value below 0.01 is typically said to be "statistically significant,", but: warning! 
warning! warning! You have computed a p-value; it is a number. I encourage you not to 
distill it to a yes-or-no phrase. p = 0.006 and p = 0.000000006 are both said to be 
"statistically significant," but they are definitely not the same!

'''

'''
array([ 1.612,  0.605,  0.327,  0.946,  0.541,  1.539,  0.529,  0.628,
        1.453,  0.297,  0.703,  0.269,  0.751,  0.245,  1.182,  0.515,
        0.435,  0.383,  0.457,  0.73 ])

array([ 1.612,  0.605,  0.327,  0.946,  0.541,  1.539,  0.529,  0.628,
        1.453,  0.297,  0.703,  0.269,  0.751,  0.245,  1.182,  0.515,
        0.435,  0.383,  0.457,  0.73 ])

'''

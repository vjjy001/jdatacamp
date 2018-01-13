'''
Permutation test on frog data

The average strike force of Frog A was 0.71 Newtons (N), and that of Frog B was 0.42 N for a difference of 0.29 N. It is possible the frogs strike with the same force and this observed difference was by chance. You will compute the probability of getting at least a 0.29 N difference in mean strike force under the hypothesis that the distributions of strike forces for the two frogs are identical. We use a permutation test with a test statistic of the difference of means to test this hypothesis.

For your convenience, the data has been stored in the arrays force_a and force_b.

'''

#���ʵ���Ŀ������֪��a���ܺ�b�����ǲ���һ����
#����������Ҫ��hypothesis test ����֤
#�����null hypothesis ����������һ����
#alternative hypothesis ���ǲ�һ��
#�������ǲ��Գ�a����ƽ����������0.71, b����0.42  ma-mb =0.29
#��������Ҫ�˽����������������һ���� 0.29 �Ĳ���������������Ƕ���

#��Ϊa��b ���Ǽ���������һ�� �������ǿ���ʹ��permutation testing�� ע��permutation test 
#����������֤����������һ����ʱ�� �����Ǵ������·��䣬Ȼ����ʵ��ó��ֲ�ͼ�� Ȼ��ͳ��
#pvalue��x=0.29���ĸ����Ƕ���
#������������ < 0.05 ˵����С�����¼� �Ӷ�null hypothesis ������

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
#ע������perm-relicates ʵ���Ͼ���ͨ������ʵ��ó����ʵ��ĸ��ʷֲ�ͼ
#Ȼ��p(x=0.29) ˵���������������ֲ�ͼ������ֵĸ����Ƕ���
p = np.sum(perm_replicates >= 0.29) / len(perm_replicates)

# Print the result
print('p-value =', p)
'''
p-value = 0.0063 �������˵����
The p-value tells you that there is about a 0.6% chance that you would get the difference 
of means observed in the experiment if frogs were exactly the same
���ķ������ ��˵�����������ͬ�ĵ����������ܣ�����0.29ţ�ٲ�һ���ĸ���ֻ��0.6%. �Ӷ��Ʒ�����
�ǵļ��� ��˵�����ܲ���ȵġ�
''''

#��������ʹ��z statistic ��ͳ������¼�
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

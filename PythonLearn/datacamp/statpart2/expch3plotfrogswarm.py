# Make bee swarm plot
_ = sns.swarmplot(x= 'ID',y= 'impact_force',data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()

'''
 ID  impact_force
20  A         1.612
21  A         0.605
22  A         0.327
23  A         0.946
24  A         0.541
25  A         1.539
26  A         0.529
27  A         0.628
28  A         1.453
29  A         0.297
30  A         0.703
31  A         0.269
32  A         0.751
33  A         0.245
34  A         1.182
35  A         0.515
36  A         0.435
37  A         0.383
38  A         0.457
39  A         0.730
60  B         0.172
61  B         0.142
62  B         0.037
63  B         0.453
64  B         0.355
65  B         0.022
66  B         0.502
67  B         0.273
68  B         0.720
69  B         0.582
70  B         0.198
71  B         0.198
72  B         0.597
73  B         0.516
74  B         0.815
75  B         0.402
76  B         0.605
77  B         0.711
78  B         0.614
79  B         0.468

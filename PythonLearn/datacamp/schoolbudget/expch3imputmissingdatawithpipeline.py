# Import the Imputer object
from sklearn.preprocessing import Imputer

# Create training and test sets using only numeric data
#this time with 2 feature, one feature with missing data
X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing']],
                                                    pd.get_dummies(sample_df['label']), 
                                                    random_state=456)

# Insantiate Pipeline object: pl
pl = Pipeline([
        ('imp', Imputer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit the pipeline to the training data
pl.fit(X_train,y_train)

# Compute and print accuracy
accuracy = pl.score(X_test,y_test)
print("\nAccuracy on sample data - all numeric, incl nans: ", accuracy)

'''
Accuracy on sample data - all numeric, incl nans:  0.636
  numeric     text  with_missing label
0   -10.856306               4.433240     b
1     9.973454      foo      4.310229     b
2     2.829785  foo bar      2.469828     a
3   -15.062947               2.852981     b
4    -5.786003  foo bar      1.826475     a
5    16.514365               2.764315     b
6   -24.266792  foo bar      3.024317     b
7    -4.289126      foo      2.596040     b
8    12.659363               2.496415     a
9    -8.667404      bar      4.032080     a
10   -6.788862  foo bar      3.907483     b
11   -0.947090      bar      3.399122     a
12   14.913896               1.722489     a
13   -6.389020  bar foo      3.200931     a
14   -4.439820                    NaN     b

'''

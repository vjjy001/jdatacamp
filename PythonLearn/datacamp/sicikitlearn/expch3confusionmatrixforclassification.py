#using confusion_matrix easier to identifier for unbalance data. to reflect the accuracy of the data
# Import necessary modules
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the training data
knn.fit(X_train,y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


'''
#The support gives the number of samples of the true response that lie in that class
         precision    recall  f1-score   support

          0       0.77      0.85      0.81       206    #no diablet
          1       0.62      0.49      0.55       102   #for dialbet

avg / total       0.72      0.73      0.72       308

'''
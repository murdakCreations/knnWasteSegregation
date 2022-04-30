def checkAccuracy(dataset):
    print('check')
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix

    X_train, X_test, y_train, y_test = train_test_split(dataset['features'], dataset['category'], random_state=0)
    lr = LogisticRegression().fit(X_train, y_train)
    pred = lr.predict(X_test)
    print("Accuracy: {:.3f}".format(accuracy_score(y_test, pred)))
    print("Confusion matrix:\n{}".format(confusion_matrix(y_test, pred)))
def trainKnn():
    #print("model is trained")
    import csv
    import numpy as np

    categoriesDisplay = ["paper","plastic","glass","metal","cardboard"]
    file = open('colorGlossFeaturesUPDATED10-10-22.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    intDataRows = []


    for row in csvreader:
        #rows.append(row)
        for rowData in range(len(row)):
            intDataRows.append(int(row[rowData]))
        rows.append(intDataRows)
        intDataRows = []

    categories = []
    dataset = {}
    features = []
    allFeatures = []

    for index in range(len(rows)):
        for featuresIndx in range(5):
            if featuresIndx == 4:
                categories.append(rows[index][featuresIndx])
            else:
                features.append(rows[index][featuresIndx])
        allFeatures += [features]
        features = []
    dataset['category'] = np.array(categories)
    dataset['features'] = np.array(allFeatures)

    from sklearn.model_selection import train_test_split 
    X_train, X_test, y_train, y_test = train_test_split(    
        dataset['features'], dataset['category'], test_size=0.2, train_size = 0.8, random_state=0)

    from sklearn.neighbors import KNeighborsClassifier 
    knn = KNeighborsClassifier(n_neighbors=1)

    knn.fit(X_train, y_train)

    # take data from image
    import colorGlossFeatures
    data = colorGlossFeatures.takeFeatures()

    # make prediction
    prediction = knn.predict(data)
    #print(type(prediction))
    print("Prediction: {}".format(prediction))
    print(categoriesDisplay[prediction.item(0)])
    
    
    # send category to i2c aarduino
    import i2c_master
    i2c_master.i2cComm(prediction)
    #print("prediction made")
    
    # evaluate accuracy
    import confusionMatrix
    confusionMatrix.checkAccuracy(dataset)

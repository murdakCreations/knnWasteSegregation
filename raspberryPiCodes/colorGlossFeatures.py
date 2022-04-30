def takeFeatures():
    file_dir = "/home/pi/Desktop/raspberryPiCodes/dataset-resized/trash/trash111.jpg"     #"/home/pi/Desktop/thesis/test_photo.jpg"
    features = []
    featureCategory = []
    dataset = {}
    whiteVal = []
    rgb = ""
    indxArr = []
    indxArrAll = []
    countOfWhite = 0
    indxArrColor = []
    intStr = ""
    arr = []

    import numpy as np
    from skimage.io import imread, imshow
    import matplotlib.pyplot as plt
    import cv2
    from skimage.filters import threshold_otsu
    from scipy.stats import mode
    
    file = file_dir

    image = imread(file, as_gray=True)

    resizedImg = cv2.resize(image,(30,30))

    threshold_value = threshold_otsu(resizedImg)
    img_threshold = resizedImg > threshold_value

    imageColored = imread(file)

    resizedImgColor = cv2.resize(imageColored,(30,30))

    # get index value of False values
    for indx0 in range(img_threshold.shape[0]):
        for indx1 in range(img_threshold.shape[1]):
            if img_threshold[indx0][indx1] == False:
                if indx1 < 29:
                    if img_threshold[indx0][indx1 + 1] == True:
                        indxArr.append(indx1 + 1)
        indxArrAll.append(indxArr)    
        indxArr = []
            
            #get white values
    for first in range(len(indxArrAll)):
        for second in range(len(indxArrAll[first])):
            for rgbIndx in range(3):
                rgb += str(resizedImgColor[first][indxArrAll[first][second]][rgbIndx])
            # convert rgb to int
            whiteVal.append(int(rgb))
            rgb = ""
    indxArrAll = []

    # get the brightest color within the area
    whiteValWhitest = np.max(whiteVal)
        
    # number of values above 200200200
    for values in range(len(whiteVal)):
        if whiteVal[values] > 200200200:
            countOfWhite += 1

    # color values within the area with similar values
    for indx0 in range(img_threshold.shape[0]):
        for indx1 in range(img_threshold.shape[1]):
            if img_threshold[indx0][indx1] == False:
                for indx2 in range(3):
                    intStr += str(resizedImgColor[indx0][indx1][indx2])
                indxArrColor.append(int(intStr))
                intStr = ""

    # total number of colors without similar values
    def combRGB(indxArrColor):
        for indx in range(0, len(indxArrColor)):
            if stackRGB(indxArrColor[indx], arr) == False:
                arr.append(indxArrColor[indx])

    def stackRGB(colorArr, arr):
        for indx in range(len(arr)):
            if arr[indx] == colorArr:
                return True
        return False

    combRGB(indxArrColor)
    numOfColors = len(arr)

    # color that appears the most within the area
    modeColor = int(mode(indxArrColor).mode)

    features = [[countOfWhite,  whiteValWhitest, modeColor, numOfColors]]
    return features
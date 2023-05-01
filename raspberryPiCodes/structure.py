while 1:

    # library for delay
    import time

    # take picture
    import takePic
    takePic.takePic()

    # train algorithm
    import trainAlgo
    trainAlgo.trainKnn()

    # 10 seconds delay
    time.sleep(10)

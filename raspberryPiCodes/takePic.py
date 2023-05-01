def takePic():
    from time import sleep
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()

    sleep(5)
    camera.capture('test_photo.jpg')
    #print("shot taken")
    sleep(5)
    camera.stop_preview()
    camera.close()

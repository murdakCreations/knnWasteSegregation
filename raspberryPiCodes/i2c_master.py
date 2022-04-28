def i2cComm(prediction):
    from smbus import SMBus
    categories = ["paper","plastic",  "glass", "metal", "cardboard"]
    addr = 0x8 # bus address
    bus = SMBus(1) # indicates /dev/ic2-1
    value = prediction.item(0)
    print(type(value))
    bus.write_byte(addr, value)
    #print(hex(int(prediction)))
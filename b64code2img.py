class B64code2Img:
    def __init__(self, b64code):
        imgdata = b64code
        img = open('qr.png', 'wb')
        img.write(imgdata)
        img.close()

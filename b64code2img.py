import base64

class B64code2Img:
    def __init__(self, b64code):
        imgdata = base64.b64decode(b64code)
        img = open('qr.png', 'wb')
        img.write(imgdata)
        img.close()

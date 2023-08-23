import sys
import requests
from time import sleep
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QPixmap
from b64code2img import B64code2Img
from const import Const
from ui_cloudmusic import Ui_CloudMusic

const = Const()

class CloudMusic(QMainWindow, Ui_CloudMusic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setup()

    def setup(self):
        if const.is_login:
            self.loginButton.setEnabled(False)
        self.loginButton.clicked.connect(self.to_login)

    def to_login(self):
        key = requests.get(const.api_url+const.key_generate, headers=const.headers).json()['data']['unikey']
        print(key)
        qr = requests.get(const.api_url+const.qr_generate+f'?key={key}&qrimg="base64"', headers=const.headers).json()
        # print(qr)
        qr_base64 = qr['data']['qrimg'].split(',')[1]
        B64code2Img(qr_base64)
        qr_pixmap = QPixmap('qr.png')
        QApplication.processEvents()
        self.qrcode.setPixmap(qr_pixmap)
        scan_status = requests.get(const.api_url+const.qr_scan_status+f'?key={key}').json()
        print(scan_status)
        while scan_status['code'] != 803:
            if scan_status['code'] == 800:
                self.qrcode.setText('二维码过期了捏，重新登录吧')
            elif scan_status['code'] == 802:
                self.qrcode.setText('扫码成功！')
            scan_status = requests.get(const.api_url + const.qr_scan_status + f'key={key}').json()
            sleep(3)
        cookie = open('cookie', 'w', encoding='utf-8')
        cookie.write(scan_status['cookie'])
        cookie.close()
        self.loginStatus.setText('登陆成功啦')
        const.is_login = True
        self.loginButton.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CloudMusic()
    sys.exit(app.exec())

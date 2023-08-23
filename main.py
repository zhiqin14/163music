import sys
import requests
from PySide6.QtWidgets import QMainWindow, QApplication
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
        key = requests.get(const.api_url+const.key_generate).json()['data']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CloudMusic()
    sys.exit(app.exec())

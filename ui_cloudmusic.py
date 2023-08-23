# *-* coding = 'utf-8' *-*

################################################################################
## Form generated from reading UI file 'cloudmusic.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QMetaObject, QObject, QPoint, QRect,QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QFont, QFontDatabase, QGradient, QIcon,QImage, QKeySequence, QLinearGradient, QPainter,QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,QSizePolicy, QTabWidget, QWidget)

class Ui_CloudMusic(object):
    def setupUi(self, CloudMusic):
        if not CloudMusic.objectName():
            CloudMusic.setObjectName(u"CloudMusic")
        CloudMusic.resize(1280, 768)
        font = QFont()
        font.setFamilies([u"\u62fe\u9646\u5b57\u6fd1\u62372.0-1"])
        font.setPointSize(12)
        CloudMusic.setFont(font)
        self.centralwidget = QWidget(CloudMusic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1281, 771))
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.loginStatus = QLabel(self.login)
        self.loginStatus.setObjectName(u"loginStatus")
        self.loginStatus.setGeometry(QRect(20, 20, 1231, 81))
        self.loginStatus.setAlignment(Qt.AlignCenter)
        self.loginButton = QPushButton(self.login)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(50, 150, 1171, 71))
        self.qrcode = QLabel(self.login)
        self.qrcode.setObjectName(u"qrcode")
        self.qrcode.setGeometry(QRect(540, 300, 180, 180))
        self.tabWidget.addTab(self.login, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.playlist = QWidget()
        self.playlist.setObjectName(u"playlist")
        self.tabWidget.addTab(self.playlist, "")
        CloudMusic.setCentralWidget(self.centralwidget)
        self.retranslateUi(CloudMusic)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(CloudMusic)
    # setupUi

    def retranslateUi(self, CloudMusic):
        CloudMusic.setWindowTitle(QCoreApplication.translate("CloudMusic", u"CloudMusic", None))
        self.loginStatus.setText(QCoreApplication.translate("CloudMusic", u"\u4f60\u8fd8\u6ca1\u6709\u767b\u5f55\u90a3\uff01\u8d76\u5feb\u53bb\u767b\u5f55\u53ed\uff01", None))
        self.loginButton.setText(QCoreApplication.translate("CloudMusic", u"\u767b\u5f55\uff01", None))
        self.qrcode.setText(QCoreApplication.translate("CloudMusic", u"Waiting...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("CloudMusic", u"\u767b\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("CloudMusic", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlist), QCoreApplication.translate("CloudMusic", u"\u6b4c\u5355", None))
    # retranslateUi


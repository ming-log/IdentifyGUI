# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainIdentify.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1186, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(20, 80, 800, 450))
        font = QFont()
        font.setFamilies([u"Adobe \u5b8b\u4f53 Std L"])
        font.setPointSize(19)
        self.input.setFont(font)
        self.input.setAutoFillBackground(False)
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, -30, 1181, 141))
        font1 = QFont()
        font1.setFamilies([u"Alibaba Sans Heavy"])
        font1.setPointSize(28)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)
        self.detect_image = QPushButton(self.centralwidget)
        self.detect_image.setObjectName(u"detect_image")
        self.detect_image.setGeometry(QRect(10, 540, 250, 61))
        font2 = QFont()
        font2.setFamilies([u"Adobe \u6977\u4f53 Std R"])
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.detect_image.setFont(font2)
        self.detect_image.setCursor(QCursor(Qt.ArrowCursor))
        self.detect_camera = QPushButton(self.centralwidget)
        self.detect_camera.setObjectName(u"detect_camera")
        self.detect_camera.setGeometry(QRect(290, 540, 250, 61))
        font3 = QFont()
        font3.setFamilies([u"Adobe \u6977\u4f53 Std R"])
        font3.setPointSize(19)
        font3.setBold(True)
        self.detect_camera.setFont(font3)
        self.detect_camera_2 = QPushButton(self.centralwidget)
        self.detect_camera_2.setObjectName(u"detect_camera_2")
        self.detect_camera_2.setGeometry(QRect(570, 540, 250, 61))
        self.detect_camera_2.setFont(font3)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(920, 200, 161, 41))
        font4 = QFont()
        font4.setFamilies([u"Adobe \u9ed1\u4f53 Std R"])
        font4.setPointSize(30)
        self.label.setFont(font4)
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(850, 230, 301, 131))
        font5 = QFont()
        font5.setFamilies([u"Alibaba Sans Heavy"])
        font5.setPointSize(25)
        font5.setBold(True)
        self.result.setFont(font5)
        self.result.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u68c0\u6d4b\u56fe\u7247", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u8fc1\u79fb\u5b66\u4e60\u7684\u4e2d\u533b\u836f\u6750\u8bc6\u522b", None))
        self.detect_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.detect_camera.setText(QCoreApplication.translate("MainWindow", u"\u672c\u673a\u6444\u50cf\u5934\u68c0\u6d4b", None))
        self.detect_camera_2.setText(QCoreApplication.translate("MainWindow", u"\u5c40\u57df\u7f51\u6444\u50cf\u5934\u68c0\u6d4b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"Result", None))
    # retranslateUi


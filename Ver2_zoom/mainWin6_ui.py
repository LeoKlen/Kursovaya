# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWin6.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"border: 1px solid #42A697;\n"
"padding: 4px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_gamma = QLineEdit(self.frame)
        self.lineEdit_gamma.setObjectName(u"lineEdit_gamma")
        self.lineEdit_gamma.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_gamma.setFont(font)
        self.lineEdit_gamma.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_gamma, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(230, 0))
        self.label_8.setMaximumSize(QSize(230, 16777215))
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(230, 0))
        self.label_11.setMaximumSize(QSize(230, 16777215))
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.lineEdit_L = QLineEdit(self.frame)
        self.lineEdit_L.setObjectName(u"lineEdit_L")
        self.lineEdit_L.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_L.setFont(font)
        self.lineEdit_L.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_L, 5, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(230, 0))
        self.label_9.setMaximumSize(QSize(230, 16777215))
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 0))
        self.label_7.setMaximumSize(QSize(60, 16777215))
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 5, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 17, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(230, 0))
        self.label_5.setMaximumSize(QSize(230, 16777215))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout.addWidget(self.label_19, 11, 3, 1, 1)

        self.label_A = QLabel(self.frame)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setMaximumSize(QSize(200, 16777215))
        self.label_A.setFont(font)
        self.label_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_A, 9, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(230, 0))
        self.label.setMaximumSize(QSize(230, 16777215))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setMaximumSize(QSize(60, 16777215))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(40, 0))
        self.label_10.setMaximumSize(QSize(60, 16777215))
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)

        self.btn_work = QPushButton(self.frame)
        self.btn_work.setObjectName(u"btn_work")
        self.btn_work.setFont(font)
        self.btn_work.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	border: 2px solid #36887c;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid #36887c;\n"
"	background : rgb(211, 254, 248);\n"
"	color: #36887c;\n"
"}")

        self.gridLayout.addWidget(self.btn_work, 14, 1, 1, 3)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 13, 0, 1, 4)

        self.label_K = QLabel(self.frame)
        self.label_K.setObjectName(u"label_K")
        self.label_K.setMaximumSize(QSize(200, 16777215))
        self.label_K.setFont(font)
        self.label_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_K, 11, 1, 1, 1)

        self.label_Rv = QLabel(self.frame)
        self.label_Rv.setObjectName(u"label_Rv")
        self.label_Rv.setMaximumSize(QSize(200, 16777215))
        self.label_Rv.setFont(font)
        self.label_Rv.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_Rv, 10, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 0))
        self.label_6.setMaximumSize(QSize(60, 16777215))
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_15, 1, 4, 1, 2)

        self.btn_zoom_plus = QPushButton(self.frame_3)
        self.btn_zoom_plus.setObjectName(u"btn_zoom_plus")
        self.btn_zoom_plus.setMinimumSize(QSize(30, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_zoom_plus.setFont(font1)
        self.btn_zoom_plus.setStyleSheet(u"QPushButton{\n"
"	color:#42A697;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid #36887c;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid #36887c;\n"
"	background : rgb(211, 254, 248);\n"
"	color: #36887c;\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons8-zoom-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zoom_plus.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_zoom_plus, 3, 5, 1, 1)

        self.btn_zoom_minus = QPushButton(self.frame_3)
        self.btn_zoom_minus.setObjectName(u"btn_zoom_minus")
        self.btn_zoom_minus.setMinimumSize(QSize(30, 0))
        self.btn_zoom_minus.setFont(font1)
        self.btn_zoom_minus.setStyleSheet(u"QPushButton{\n"
"	color:#42A697;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid #36887c;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid #36887c;\n"
"	background : rgb(211, 254, 248);\n"
"	color: #36887c;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons8-zoom-out-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zoom_minus.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_zoom_minus, 3, 4, 1, 1)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 2)

        self.btn_rotate_minus = QPushButton(self.frame_3)
        self.btn_rotate_minus.setObjectName(u"btn_rotate_minus")
        self.btn_rotate_minus.setMinimumSize(QSize(30, 0))
        self.btn_rotate_minus.setFont(font1)
        self.btn_rotate_minus.setStyleSheet(u"QPushButton{\n"
"	color:#42A697;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid #36887c;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid #36887c;\n"
"	background : rgb(211, 254, 248);\n"
"	color: #36887c;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons8-rotate-left-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rotate_minus.setIcon(icon2)

        self.gridLayout_2.addWidget(self.btn_rotate_minus, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.btn_rotate_plus = QPushButton(self.frame_3)
        self.btn_rotate_plus.setObjectName(u"btn_rotate_plus")
        self.btn_rotate_plus.setMinimumSize(QSize(30, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setKerning(True)
        self.btn_rotate_plus.setFont(font2)
        self.btn_rotate_plus.setAutoFillBackground(False)
        self.btn_rotate_plus.setStyleSheet(u"QPushButton{\n"
"	color:#42A697;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid #36887c;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid #36887c;\n"
"	background : rgb(211, 254, 248);\n"
"	color: #36887c;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons8-rotate-right-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rotate_plus.setIcon(icon3)

        self.gridLayout_2.addWidget(self.btn_rotate_plus, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 18, 0, 1, 4)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(40, 0))
        self.label_12.setMaximumSize(QSize(60, 16777215))
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 10, 3, 1, 1)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(230, 16777215))
        self.label_18.setFont(font)

        self.gridLayout.addWidget(self.label_18, 9, 0, 1, 1)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout.addWidget(self.label_21, 9, 3, 1, 1)

        self.lineEdit_D = QLineEdit(self.frame)
        self.lineEdit_D.setObjectName(u"lineEdit_D")
        self.lineEdit_D.setMinimumSize(QSize(100, 0))
        self.lineEdit_D.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_D.setFont(font)
        self.lineEdit_D.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_D, 4, 1, 1, 1)

        self.lineEdit_V = QLineEdit(self.frame)
        self.lineEdit_V.setObjectName(u"lineEdit_V")
        self.lineEdit_V.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_V.setFont(font)
        self.lineEdit_V.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_V, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(230, 16777215))
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 11, 0, 1, 1)

        self.lineEdit_H = QLineEdit(self.frame)
        self.lineEdit_H.setObjectName(u"lineEdit_H")
        self.lineEdit_H.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_H.setFont(font)
        self.lineEdit_H.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_H, 1, 1, 1, 1)

        self.label_err = QLabel(self.frame)
        self.label_err.setObjectName(u"label_err")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_err.sizePolicy().hasHeightForWidth())
        self.label_err.setSizePolicy(sizePolicy1)
        self.label_err.setFont(font)
        self.label_err.setStyleSheet(u"color:red;\n"
"border:none;")

        self.gridLayout.addWidget(self.label_err, 16, 0, 1, 4)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 4)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(230, 0))
        self.label_4.setMaximumSize(QSize(230, 16777215))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(230, 16777215))
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.label_Ny = QLabel(self.frame)
        self.label_Ny.setObjectName(u"label_Ny")
        self.label_Ny.setMaximumSize(QSize(200, 16777215))
        self.label_Ny.setFont(font)
        self.label_Ny.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_Ny, 12, 1, 1, 1)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(40, 0))
        self.label_20.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_20, 12, 3, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"border: 1px solid #42A697;\n"
"padding: 4px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_gamma.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0441\u0435\u0440\u0438\u0438, L", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u0432\u0438\u0440\u0430\u0436\u0430, R", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.lineEdit_L.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435  \u043c\u0435\u0436\u0434\u0443 \u0446\u0435\u043b\u044f\u043c\u0438, D", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b, \u0263", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0433\u0440\u0430\u0434", None))
        self.label_A.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c, V", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043c/\u0441", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.btn_work.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_K.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_Rv.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0433\u0440\u0430\u0434", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.btn_zoom_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_zoom_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0435\u043d\u0438\u0435", None))
        self.btn_rotate_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_rotate_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0434\u043e \u0446\u0435\u043b\u0438 1, \u0410", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u043c", None))
        self.lineEdit_D.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        self.lineEdit_V.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043a\u043e\u043d\u0443\u0441\u0430", None))
        self.lineEdit_H.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_err.setText(QCoreApplication.translate("MainWindow", u"Err", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430, H", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.label_Ny.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText("")
    # retranslateUi


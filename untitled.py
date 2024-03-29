# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {background-color: #1581e6; color: white; font-family: \"Days\";}\n"
"QPushButton:hover {border-style: solid; border-width: 3px; border-color: white;} QPushButton:pressed {border-style: solid; border-width: 3px; border-color: rgb(14, 80, 158);} QPushButton {background-color: rgb(255, 230, 31); color: rgb(14, 80, 158); border-radius: 10px;}\n"
"QTextEdit:hover {border-style: solid; border-width: 1px; border-color: white;} QTextEdit:pressed {border-style: solid; border-width: 1px; border-color: rgb(14, 80, 158);} QTextEdit {background-color: #42aaff; color: white; border-radius: 10px;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lang_from = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lang_from.sizePolicy().hasHeightForWidth())
        self.lang_from.setSizePolicy(sizePolicy)
        self.lang_from.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(14)
        self.lang_from.setFont(font)
        self.lang_from.setFrame(True)
        self.lang_from.setObjectName("lang_from")
        self.verticalLayout_2.addWidget(self.lang_from)
        self.text_from = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(14)
        self.text_from.setFont(font)
        self.text_from.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_from.setStyleSheet("background-color: #42aaff;\n"
"\n"
"")
        self.text_from.setReadOnly(False)
        self.text_from.setObjectName("text_from")
        self.verticalLayout_2.addWidget(self.text_from)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lang_to = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lang_to.sizePolicy().hasHeightForWidth())
        self.lang_to.setSizePolicy(sizePolicy)
        self.lang_to.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(14)
        self.lang_to.setFont(font)
        self.lang_to.setFrame(True)
        self.lang_to.setObjectName("lang_to")
        self.verticalLayout.addWidget(self.lang_to)
        self.text_to = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(14)
        self.text_to.setFont(font)
        self.text_to.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_to.setStyleSheet("background-color: #42aaff;")
        self.text_to.setReadOnly(True)
        self.text_to.setObjectName("text_to")
        self.verticalLayout.addWidget(self.text_to)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy)
        self.btn_copy.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_copy.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy.setIcon(icon1)
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout_3.addWidget(self.btn_copy)
        self.btn_play_over = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_play_over.sizePolicy().hasHeightForWidth())
        self.btn_play_over.setSizePolicy(sizePolicy)
        self.btn_play_over.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_play_over.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play_over.setIcon(icon2)
        self.btn_play_over.setObjectName("btn_play_over")
        self.horizontalLayout_3.addWidget(self.btn_play_over)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_translate.sizePolicy().hasHeightForWidth())
        self.btn_translate.setSizePolicy(sizePolicy)
        self.btn_translate.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(16)
        self.btn_translate.setFont(font)
        self.btn_translate.setObjectName("btn_translate")
        self.verticalLayout_3.addWidget(self.btn_translate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        self.text_from.setPlaceholderText(_translate("MainWindow", "Введите текст, который нужно перевести"))
        self.text_to.setPlaceholderText(_translate("MainWindow", "Здесь будет перевод"))
        self.btn_translate.setText(_translate("MainWindow", "Перевеcти"))

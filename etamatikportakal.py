# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'etamatikportakal.ui'
#
# Created: Thu Apr 14 15:50:32 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(422, 225)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Masaüstü/work/website/images/pardus-kafa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtUsername = QtGui.QLineEdit(self.centralwidget)
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))
        self.verticalLayout.addWidget(self.txtUsername)
        self.txtPassword = QtGui.QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.verticalLayout.addWidget(self.txtPassword)
        self.txtEBAUsername = QtGui.QLineEdit(self.centralwidget)
        self.txtEBAUsername.setObjectName(_fromUtf8("txtEBAUsername"))
        self.verticalLayout.addWidget(self.txtEBAUsername)
        self.txtEBAPassword = QtGui.QLineEdit(self.centralwidget)
        self.txtEBAPassword.setObjectName(_fromUtf8("txtEBAPassword"))
        self.verticalLayout.addWidget(self.txtEBAPassword)
        self.comboUSB = QtGui.QComboBox(self.centralwidget)
        self.comboUSB.setObjectName(_fromUtf8("comboUSB"))
        self.verticalLayout.addWidget(self.comboUSB)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout_6.addWidget(self.btnClear)
        self.btnSubmit = QtGui.QPushButton(self.centralwidget)
        self.btnSubmit.setObjectName(_fromUtf8("btnSubmit"))
        self.horizontalLayout_6.addWidget(self.btnSubmit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ETAmatik Portakal", None))
        self.label_6.setText(_translate("MainWindow", "Pardus ETAP Otomatik Giriş USB Diski Oluşturma Aracı", None))
        self.label_2.setText(_translate("MainWindow", "Kullanıcı Adı:", None))
        self.label_3.setText(_translate("MainWindow", "Parola:", None))
        self.label_4.setText(_translate("MainWindow", "EBA Kullanıcı Adı:", None))
        self.label_5.setText(_translate("MainWindow", "EBA Parola:", None))
        self.label.setText(_translate("MainWindow", "USB Disk:", None))
        self.btnClear.setText(_translate("MainWindow", "Alanları Temizle", None))
        self.btnSubmit.setText(_translate("MainWindow", "Bilgileri USB Diske Kaydet", None))


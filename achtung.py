# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'achtung.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(260, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(260, 120))
        Dialog.setMaximumSize(QtCore.QSize(260, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setKerning(False)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.label_achtung = QtWidgets.QLabel(Dialog)
        self.label_achtung.setGeometry(QtCore.QRect(10, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_achtung.setFont(font)
        self.label_achtung.setAutoFillBackground(False)
        self.label_achtung.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_achtung.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_achtung.setLineWidth(0)
        self.label_achtung.setMidLineWidth(0)
        self.label_achtung.setAlignment(QtCore.Qt.AlignCenter)
        self.label_achtung.setObjectName("label_achtung")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Achtung!"))
        self.label_achtung.setText(_translate("Dialog", "Das geht nicht!!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


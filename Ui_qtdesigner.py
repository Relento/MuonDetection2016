# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NUC\Documents\Gui\Test2\qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mplMainWindow(object):
    def setupUi(self, mplMainWindow):
        mplMainWindow.setObjectName("mplMainWindow")
        mplMainWindow.resize(1242, 879)
        self.centralWidget = QtWidgets.QWidget(mplMainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1211, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.mplpushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mplpushButton.setObjectName("mplpushButton")
        self.horizontalLayout.addWidget(self.mplpushButton)
        self.mpl = MplWidget(self.centralWidget)
        self.mpl.setGeometry(QtCore.QRect(10, 60, 751, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(770, 90, 281, 24))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.thresholdSlider = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSlider.sizePolicy().hasHeightForWidth())
        self.thresholdSlider.setSizePolicy(sizePolicy)
        self.thresholdSlider.setMaximum(30)
        self.thresholdSlider.setSliderPosition(15)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setObjectName("thresholdSlider")
        self.horizontalLayout_2.addWidget(self.thresholdSlider)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_2.setReadOnly(True)
        mplMainWindow.setCentralWidget(self.centralWidget)
        self.mplmenuBar = QtWidgets.QMenuBar(mplMainWindow)
        self.mplmenuBar.setGeometry(QtCore.QRect(0, 0, 1242, 23))
        self.mplmenuBar.setObjectName("mplmenuBar")
        self.mplmenuFile = QtWidgets.QMenu(self.mplmenuBar)
        self.mplmenuFile.setObjectName("mplmenuFile")
        mplMainWindow.setMenuBar(self.mplmenuBar)
        self.mplaactionOpen = QtWidgets.QAction(mplMainWindow)
        self.mplaactionOpen.setObjectName("mplaactionOpen")
        self.mplactionQuit = QtWidgets.QAction(mplMainWindow)
        self.mplactionQuit.setObjectName("mplactionQuit")
        self.mplmenuFile.addAction(self.mplaactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.mplmenuBar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(mplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(mplMainWindow)

    def retranslateUi(self, mplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        mplMainWindow.setWindowTitle(_translate("mplMainWindow", "MuonDetection"))
        self.mplpushButton.setText(_translate("mplMainWindow", "Update"))
        self.label.setText(_translate("mplMainWindow", "滤波阈值"))
        self.lineEdit_2.setText(_translate("mplMainWindow", "15"))
        self.mplmenuFile.setTitle(_translate("mplMainWindow", "File"))
        self.mplaactionOpen.setText(_translate("mplMainWindow", "Open"))
        self.mplactionQuit.setText(_translate("mplMainWindow", "Quit"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mplMainWindow = QtWidgets.QMainWindow()
    ui = Ui_mplMainWindow()
    ui.setupUi(mplMainWindow)
    mplMainWindow.show()
    sys.exit(app.exec_())


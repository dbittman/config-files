# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sun Mar 14 16:02:02 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 315)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.connectionGroupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionGroupBox.sizePolicy().hasHeightForWidth())
        self.connectionGroupBox.setSizePolicy(sizePolicy)
        self.connectionGroupBox.setObjectName("connectionGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.connectionGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hostLabel = QtGui.QLabel(self.connectionGroupBox)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout.addWidget(self.hostLabel, 0, 0, 1, 1)
        self.hostLineEdit = QtGui.QLineEdit(self.connectionGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostLineEdit.sizePolicy().hasHeightForWidth())
        self.hostLineEdit.setSizePolicy(sizePolicy)
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.gridLayout.addWidget(self.hostLineEdit, 0, 1, 1, 1)
        self.portLabel = QtGui.QLabel(self.connectionGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLabel.sizePolicy().hasHeightForWidth())
        self.portLabel.setSizePolicy(sizePolicy)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)
        self.portLineEdit = QtGui.QLineEdit(self.connectionGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setObjectName("portLineEdit")
        self.gridLayout.addWidget(self.portLineEdit, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4.addWidget(self.connectionGroupBox)
        self.orientationGroupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orientationGroupBox.sizePolicy().hasHeightForWidth())
        self.orientationGroupBox.setSizePolicy(sizePolicy)
        self.orientationGroupBox.setObjectName("orientationGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.orientationGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalRadioButton = QtGui.QRadioButton(self.orientationGroupBox)
        self.horizontalRadioButton.setChecked(True)
        self.horizontalRadioButton.setObjectName("horizontalRadioButton")
        self.verticalLayout_3.addWidget(self.horizontalRadioButton)
        self.verticalRadioButton = QtGui.QRadioButton(self.orientationGroupBox)
        self.verticalRadioButton.setObjectName("verticalRadioButton")
        self.verticalLayout_3.addWidget(self.verticalRadioButton)
        self.verticalLayout_4.addWidget(self.orientationGroupBox)
        self.iconsGroupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconsGroupBox.sizePolicy().hasHeightForWidth())
        self.iconsGroupBox.setSizePolicy(sizePolicy)
        self.iconsGroupBox.setObjectName("iconsGroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.iconsGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.systemIconsRadioButton = QtGui.QRadioButton(self.iconsGroupBox)
        self.systemIconsRadioButton.setChecked(True)
        self.systemIconsRadioButton.setObjectName("systemIconsRadioButton")
        self.verticalLayout_2.addWidget(self.systemIconsRadioButton)
        self.userIconsRadioButton = QtGui.QRadioButton(self.iconsGroupBox)
        self.userIconsRadioButton.setObjectName("userIconsRadioButton")
        self.verticalLayout_2.addWidget(self.userIconsRadioButton)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.stopCheckBox = QtGui.QCheckBox(self.iconsGroupBox)
        self.stopCheckBox.setObjectName("stopCheckBox")
        self.verticalLayout_2.addWidget(self.stopCheckBox)
        self.verticalLayout_4.addWidget(self.iconsGroupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.connectionGroupBox.setTitle(QtGui.QApplication.translate("Dialog", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel.setText(QtGui.QApplication.translate("Dialog", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("Dialog", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.orientationGroupBox.setTitle(QtGui.QApplication.translate("Dialog", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalRadioButton.setText(QtGui.QApplication.translate("Dialog", "Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalRadioButton.setText(QtGui.QApplication.translate("Dialog", "Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.iconsGroupBox.setTitle(QtGui.QApplication.translate("Dialog", "Icons", None, QtGui.QApplication.UnicodeUTF8))
        self.systemIconsRadioButton.setText(QtGui.QApplication.translate("Dialog", "System theme", None, QtGui.QApplication.UnicodeUTF8))
        self.userIconsRadioButton.setText(QtGui.QApplication.translate("Dialog", "From \"icons\" directory in package", None, QtGui.QApplication.UnicodeUTF8))
        self.stopCheckBox.setText(QtGui.QApplication.translate("Dialog", "Show \"stop\" button", None, QtGui.QApplication.UnicodeUTF8))

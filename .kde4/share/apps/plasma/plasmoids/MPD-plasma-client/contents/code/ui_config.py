# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Sun Apr 25 03:41:30 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(255, 366)
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
        self.gridLayout = QtGui.QGridLayout(self.connectionGroupBox)
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
        self.verticalLayout_4.addWidget(self.connectionGroupBox)
        self.orientationGroupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orientationGroupBox.sizePolicy().hasHeightForWidth())
        self.orientationGroupBox.setSizePolicy(sizePolicy)
        self.orientationGroupBox.setObjectName("orientationGroupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.orientationGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalRadioButton = QtGui.QRadioButton(self.orientationGroupBox)
        self.horizontalRadioButton.setChecked(True)
        self.horizontalRadioButton.setObjectName("horizontalRadioButton")
        self.horizontalLayout.addWidget(self.horizontalRadioButton)
        self.verticalRadioButton = QtGui.QRadioButton(self.orientationGroupBox)
        self.verticalRadioButton.setObjectName("verticalRadioButton")
        self.horizontalLayout.addWidget(self.verticalRadioButton)
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
        spacerItem = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.stopCheckBox = QtGui.QCheckBox(self.iconsGroupBox)
        self.stopCheckBox.setObjectName("stopCheckBox")
        self.verticalLayout_2.addWidget(self.stopCheckBox)
        self.verticalLayout_4.addWidget(self.iconsGroupBox)
        self.popupGroupBox = QtGui.QGroupBox(Dialog)
        self.popupGroupBox.setObjectName("popupGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.popupGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.showPopupDialogCheckBox = QtGui.QCheckBox(self.popupGroupBox)
        self.showPopupDialogCheckBox.setChecked(False)
        self.showPopupDialogCheckBox.setObjectName("showPopupDialogCheckBox")
        self.verticalLayout_3.addWidget(self.showPopupDialogCheckBox)
        self.widget = QtGui.QWidget(self.popupGroupBox)
        self.widget.setEnabled(False)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showCoverImageCheckBox = QtGui.QCheckBox(self.widget)
        self.showCoverImageCheckBox.setObjectName("showCoverImageCheckBox")
        self.verticalLayout.addWidget(self.showCoverImageCheckBox)
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout_4.addWidget(self.popupGroupBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.showPopupDialogCheckBox, QtCore.SIGNAL("toggled(bool)"), self.widget.setEnabled)
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
        self.userIconsRadioButton.setText(QtGui.QApplication.translate("Dialog", "Custom (use if system icons don\'t work)", None, QtGui.QApplication.UnicodeUTF8))
        self.stopCheckBox.setText(QtGui.QApplication.translate("Dialog", "Show \"stop\" button", None, QtGui.QApplication.UnicodeUTF8))
        self.popupGroupBox.setTitle(QtGui.QApplication.translate("Dialog", "Popup Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.showPopupDialogCheckBox.setText(QtGui.QApplication.translate("Dialog", "Show popup dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.showCoverImageCheckBox.setToolTip(QtGui.QApplication.translate("Dialog", "NOTE: plasmoid look you covers folder (~/.covers/)", None, QtGui.QApplication.UnicodeUTF8))
        self.showCoverImageCheckBox.setText(QtGui.QApplication.translate("Dialog", "Show cover image", None, QtGui.QApplication.UnicodeUTF8))


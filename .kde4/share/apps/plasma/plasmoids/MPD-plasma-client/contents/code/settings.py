# -*- coding: utf-8 -*-
#
#   This file is part of MPD-plasma-client
#   MPD-plasma-client it simply mpd-server client written on python
#
#   Copyright (C) 2010 Vladimir Krylov <memnek@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License version 2,
#   or (at your option) any later version, as published by the Free
#   Software Foundation
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdecore import *
from PyKDE4.kdeui import *
from PyKDE4.kio import *

from ui_config import Ui_Dialog

class Settings(QWidget, Ui_Dialog):

	def __init__(self, parent, defaultSettings = None):

		QWidget.__init__(self)
		self.parent = parent
		self.setupUi(self)
		if defaultSettings:
			self.hostLineEdit.setText(defaultSettings['host'])
			self.portLineEdit.setText(str(defaultSettings['port']))
			
			if defaultSettings['orientation'] == 'v':
				self.verticalRadioButton.setChecked(True)
			else:
				self.horizontalRadioButton.setChecked(True)
				
			if defaultSettings['icons'] == 'u':
				self.userIconsRadioButton.setChecked(True)
			else:
				self.systemIconsRadioButton.setChecked(True)

			if defaultSettings['stop']:
				self.stopCheckBox.setChecked(True)
			else:
				self.stopCheckBox.setChecked(False)

			if defaultSettings['popup']:
				self.showPopupDialogCheckBox.setChecked(True)
			else:
				self.showPopupDialogCheckBox.setChecked(False)

			if defaultSettings['cover']:
				self.showCoverImageCheckBox.setChecked(True)
			else:
				self.showCoverImageCheckBox.setChecked(False)

	def getSettings(self):
		host = str.strip(str(self.hostLineEdit.text()))
		port = int(str.strip(str(self.portLineEdit.text())))
		
		if self.horizontalRadioButton.isChecked():
			orientation = 'h'
		else:
			orientation = 'v'
			
		if self.systemIconsRadioButton.isChecked():
			iconTheme = 's'
		else:
			iconTheme = 'u'
			
		if self.stopCheckBox.isChecked():
			stopButton = True
		else:
			stopButton = False

		if self.showPopupDialogCheckBox.isChecked():
			popup = True
		else:
			popup = False

		if self.showCoverImageCheckBox.isChecked():
			cover = True
		else:
			cover = False
		
		return {'host': host, \
				'port': port, \
				'orientation': orientation, \
				'icons': iconTheme, \
				'stop': stopButton, \
				'popup': popup, \
				'cover': cover}


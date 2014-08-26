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
from PyKDE4.plasma import *

class PopupDialog(Plasma.Dialog):
	def init(self):
		self.setWindowFlags(Qt.FramelessWindowHint \
							| Qt.WindowStaysOnTopHint \
							| Qt.X11BypassWindowManagerHint)
		self.setStyleSheet("padding-left:0;color: %s;" %
			Plasma.Theme.defaultTheme().color(Plasma.Theme.TextColor).name())

		self.layout = QHBoxLayout(self)
		self.glayout = QGraphicsLinearLayout(Qt.Horizontal)
		self.cover = Plasma.IconWidget()
		self.body = QLabel()
		self.scene = QGraphicsScene(self)
		self.scene.addItem(self.cover)
		self.view = QGraphicsView()
		self.rect = QRectF(0, 0, 80, 80)
		self.view.setSceneRect(self.rect)
		self.view.setScene(self.scene)
		self.view.setStyleSheet("background: qRgba(0, 0, 0, 0);" + \
								"border: qRgba(0, 0, 0, 0)")
		self.view.show()
		self.layout.addWidget(self.view)
		self.layout.addWidget(self.body)
		self.setLayout(self.layout)

	def fill(self, title, artist, album, cover):
		self.body.setText(QString.fromUtf8("<table><tr align=\"center\">" + \
											"<td>" + \
											"</td><td><font size=\"5\"><b>" + \
											title + "</font></b><br>" + \
											"<i>by</i> " + \
											artist + " <i>from</i>  " + \
											album + "</td></tr></table>"))

		self.cover.setIcon(QIcon(cover))
		self.cover.resize(80, 80)
#		self.cover.setMaximumSize(80, 80)



	def showDialog(self):
		if self.body.text() == "":
			pass
		else:
			self.adjustSize()
			self.animatedShow(Plasma.Up)
#			self.show()



#<img src=\"" + cover + \
#"\" + width=\"80\" " + \
#"height=\"80\">"

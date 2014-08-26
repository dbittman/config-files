# -*- coding: utf-8 -*-

from PyQt4.QtCore import QUrl, QSize
from PyQt4.QtGui import QDialog, QVBoxLayout, QPushButton
from PyQt4.QtWebKit import QWebView

import urllib2 as urllib

class FullCamWidget(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setWindowTitle(u'Povečana slika kamere')

	def show(self, url, width=None, height=None):
		self.layout = QVBoxLayout()
		self.view = QWebView()
		self.button = QPushButton("&Zapri")
		
		self.layout.addWidget(self.view)
		self.layout.addWidget(self.button)

		self.button.released.connect(self.close)

		self.view.setUrl(QUrl(url))
		
		self.setLayout(self.layout)
		if width == None or height == None:
			self.resize(640,480)
		else:
			self.resize(width, height)
			
		self.exec_()
		

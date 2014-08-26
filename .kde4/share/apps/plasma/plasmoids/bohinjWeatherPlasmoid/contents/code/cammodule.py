# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QTimer, QUrl
from PyQt4.QtGui import QGraphicsLinearLayout, QSizePolicy
from PyQt4.QtWebKit import QGraphicsWebView
from PyKDE4.plasma import Plasma

from fullcamwidget import FullCamWidget
from updatetimeselector import UpdateTimeSelector

import urllib2 as urllib
import time, socket


class CamModule:
	def __init__(self):
		self.name = "Kamere"
		#Cam urls
		self.camUrls = {u"Ribčev Laz (v živo)": "http://firma.sportnet.si:8080/dvs2000/r1.jpg",\
						u"Ribčev Laz": "http://www.bohinj.si/cam/slika3.jpg",\
						u"Vogel - 1" : "http://www.snezni-telefon.si/Images/Kamere/6_a.jpg",\
						u"Vogel - 2" : "http://www.snezni-telefon.si/Images/Kamere/6_b.jpg",\
						u"Vogel - 3" : "http://www.snezni-telefon.si/Images/Kamere/6_c.jpg",\
						u"Vogel - 4" : "http://www.snezni-telefon.si/Images/Kamere/6_d.jpg",\
						u"Bohinjska Češnjica" : "http://www2.arnes.si/~smisma1/canon.jpg",\
						u"Bohinjska Bistrica" : "http://www.drsc.si/kamere/kamslike/bohinjska/slike/boh1_0001.jpg",\
						u"Orožnova koča": "http://www.bohinj.si/cam/lisc/slika1.jpg"}

		self.camSizes ={u"Ribčev Laz (v živo)": "352x228", \
						u"Ribčev Laz": "2048x1536",\
						u"Vogel - 1" : "1280x1024",\
						u"Vogel - 2" : "640x480",\
						u"Vogel - 3" : "1280x1024",\
						u"Vogel - 4" : "640x480",\
						u"Bohinjska Češnjica" : "800x600",\
						u"Bohinjska Bistrica" : "352x228",\
						u"Orožnova koča": "1280x1024"}
						
		self.updateTimer = QTimer()
		self.updateTimer.timeout.connect(self.update)
		
	
	def makeLayout(self):
		self.layout = QGraphicsLinearLayout(Qt.Vertical)
		self.topCamLayout = QGraphicsLinearLayout(Qt.Horizontal)
		
		# Cam layout
		self.camRefreshButton = Plasma.IconWidget()
		self.camRefreshButton.setIcon("view-refresh")
		self.camRefreshButton.clicked.connect(self.update)
		
		self.camTimeLabel = Plasma.Label()
		self.camTimeLabel.setText(u"ob")

		self.camEnlargeButton = Plasma.IconWidget()
		self.camEnlargeButton.setIcon("zoom-in")
		self.camEnlargeButton.clicked.connect(self.showFullCamWidget)

		self.camSelectorCombo = Plasma.ComboBox()
		for source in sorted(self.camUrls.keys()):
			self.camSelectorCombo.addItem(source)
		self.camSelectorCombo.setMinimumWidth(125)
		self.camSelectorCombo.textChanged.connect(self.camChanged)

		self.camView = QGraphicsWebView()
		self.camView.setEnabled(False)

		self.camTimeDataLabel = Plasma.Label()

		self.camUpdateTimeSelector = UpdateTimeSelector()
		self.camUpdateTimeSelector.setDefaultTime(30)
		self.camUpdateTimeSelector.setDefaultInterval('min')
		self.camUpdateTimeSelector.updateTimeSpin.valueChanged.connect(self.camTimeChanged)
		self.camUpdateTimeSelector.updateCheckBox.toggled.connect(self.camTimerToggle)

		self.topCamLayout.addItem(self.camSelectorCombo)
		self.topCamLayout.addItem(self.camTimeLabel)
		self.topCamLayout.addItem(self.camTimeDataLabel)
		self.topCamLayout.addStretch()
		self.topCamLayout.addItem(self.camEnlargeButton)
		self.topCamLayout.addItem(self.camRefreshButton)

		self.layout.addItem(self.topCamLayout)
		self.layout.addItem(self.camView)
		self.layout.addItem(self.camUpdateTimeSelector.layout)
		self.layout.itemAt(0).setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, QSizePolicy.DefaultType)
		self.layout.itemAt(2).setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, QSizePolicy.DefaultType)
	
	def update(self, text=None):
		try:
			urllib.urlopen('http://www.google.com', timeout=2)
		except:
			self.offlineMode()
			return
		if not self.camUpdateTimeSelector.updateCheckBox.isChecked():
			self.updateTimer.stop()
		self.camChanged(self.camSelectorCombo.text())
		self.setCamTimeLabel()
		
	def offlineMode(self):
		self.camView.setUrl(QUrl("weather-none-available.png"))
		self.camTimeDataLabel.setText(" ni na voljo.")
		
	def setCamTimeLabel(self):
		hour = time.localtime().tm_hour if not time.localtime().tm_hour in range(10) else '0' + str(time.localtime().tm_hour)
		minute = time.localtime().tm_min if not time.localtime().tm_min in range(10) else '0' + str(time.localtime().tm_min)
		second = time.localtime().tm_sec if not time.localtime().tm_sec in range(10) else '0' + str(time.localtime().tm_sec)
		self.camTimeDataLabel.setText(u'<b>%s:%s:%s</b>' % (str(hour), str(minute), str(second)) )
    
	def camTimerToggle(self, toggled):
		if toggled:
			multiplier = 1
			if self.camUpdateTimeSelector.getInterval() == 'min':
				multiplier = 60
			if self.camUpdateTimeSelector.getInterval() == 'h':
				multiplier = 60 * 60
			self.updateTimer.start(self.camUpdateTimeSelector.getTime() * 1000 * multiplier)
			self.update()
		else:
			self.updateTimer.stop()
	
	def camChanged(self, text):
		self.camView.setUrl( QUrl( self.camUrls[unicode(text)] ) )
		self.setCamTimeLabel()
		
	def camTimeChanged(self, value):
		if self.camUpdateTimeSelector.isChecked():
			self.updateTimer.stop()
		self.camTimerToggle(self.camUpdateTimeSelector.isChecked())
	
	def showFullCamWidget(self):
		fullcamwidget = FullCamWidget()
		size = self.camSizes[unicode(self.camSelectorCombo.text())]
		size = [ int(i) for i in size.split('x')]
		if size[0] < 640 and size[1] < 480:
			fullcamwidget.show(self.camView.url(), size[0] + 25, size[1] + 125)
		else:
			fullcamwidget.show(self.camView.url(), 645, 505)
	
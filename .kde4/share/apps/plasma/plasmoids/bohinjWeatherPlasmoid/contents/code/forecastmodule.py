# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QTimer, QUrl
from PyQt4.QtGui import QGraphicsLinearLayout
from PyQt4.QtWebKit import QGraphicsWebView
from PyKDE4.plasma import Plasma

from updatetimeselector import UpdateTimeSelector
from forecast import BohinjForecast, NoForecast

import urllib2 as urllib


class ForecastModule:
	def __init__(self):
		self.name = "Napoved"
		self.updateTimer = QTimer()
		self.updateTimer.timeout.connect(self.update)
	
	def makeLayout(self):
		self.layout = QGraphicsLinearLayout(Qt.Vertical)
		self.forecastTopLayout = QGraphicsLinearLayout(Qt.Horizontal)
		
		#Forecast Layout
		self.forecastIcons = [QGraphicsWebView() for i in range(4)]
		[v.setEnabled(False) for v in self.forecastIcons]
		[v.setMaximumSize(40,40) for v in self.forecastIcons]
		[v.setMinimumSize(40,40) for v in self.forecastIcons]
		[v.page().mainFrame().setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff) for v in self.forecastIcons]
		[v.page().mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff) for v in self.forecastIcons]

		self.forecastDays = [Plasma.Label() for i in range(4)]
		[l.setAlignment(Qt.AlignCenter) for l in self.forecastDays]

		self.forecastTemperatures = [Plasma.Label() for i in range(4)]
		[l.setAlignment(Qt.AlignCenter) for l in self.forecastTemperatures]
		
		
		self.forecastIconFrames = [QGraphicsLinearLayout(Qt.Horizontal) for i in range(4)]
		[self.forecastIconFrames[i].addStretch() for i in range(4)]
		[self.forecastIconFrames[i].addItem(self.forecastIcons[i]) for i in range(4)]
		[self.forecastIconFrames[i].addStretch() for i in range(4)]
		
		self.forecastFrames = [QGraphicsLinearLayout(Qt.Vertical) for i in range(4)]
		[self.forecastFrames[i].addStretch() for i in range(4)]
		[self.forecastFrames[i].addItem(self.forecastDays[i]) for i in range(4)]
		[self.forecastFrames[i].addItem(self.forecastIconFrames[i]) for i in range(4)]
		[self.forecastFrames[i].addItem(self.forecastTemperatures[i]) for i in range(4)]
		[self.forecastFrames[i].addStretch() for i in range(4)]

		self.forecastTopFrame = QGraphicsLinearLayout(Qt.Horizontal)
		self.forecastTopFrame.addStretch()
		self.forecastTopFrame.addItem(self.forecastFrames[0])
		self.forecastTopFrame.addStretch()
		
		self.forecastBottomFrames = QGraphicsLinearLayout(Qt.Horizontal)
		self.forecastBottomFrames.addStretch()
		[self.forecastBottomFrames.addItem(self.forecastFrames[i]) for i in range(1,4)]
		self.forecastBottomFrames.addStretch()

		self.forecastRefreshButton = Plasma.IconWidget()
		self.forecastRefreshButton.setIcon("view-refresh")
		self.forecastRefreshButton.clicked.connect(self.update)

		self.forecastStatusLabel = Plasma.Label()

		self.forecastTopLayout.addItem(self.forecastStatusLabel)
		self.forecastTopLayout.addItem(self.forecastRefreshButton)
		self.forecastTopLayout.setMaximumHeight(32)
		
		self.forecastUpdateTimeSelector = UpdateTimeSelector()
		self.forecastUpdateTimeSelector.setDefaultTime(4)
		self.forecastUpdateTimeSelector.setDefaultInterval('h')
		self.forecastUpdateTimeSelector.updateTimeSpin.valueChanged.connect(self.forecastTimeChanged)
		self.forecastUpdateTimeSelector.updateCheckBox.toggled.connect(self.forecastTimerToggle)
		
		
		self.layout.addItem(self.forecastTopLayout)
		self.layout.addStretch()
		self.layout.addItem(self.forecastTopFrame)
		self.layout.addItem(self.forecastBottomFrames)
		self.layout.addStretch()
		self.layout.addItem(self.forecastUpdateTimeSelector.layout)
	
	def forecastTimerToggle(self, toggled):
		if toggled:
			multiplier = 1
			if self.forecastUpdateTimeSelector.getInterval() == 'min':
				multiplier = 60
			if self.forecastUpdateTimeSelector.getInterval() == 'h':
				multiplier = 60 * 60
			self.updateTimer.start(self.forecastUpdateTimeSelector.getTime() * 1000 * multiplier)
			self.update()
		else:
			self.updateTimer.stop()
			
	def forecastTimeChanged(self, value):
		if self.forecastUpdateTimeSelector.isChecked():
			self.updateTimer.stop()
		self.forecastTimerToggle(self.forecastUpdateTimeSelector.isChecked())
	
	def update(self):
		forecast = NoForecast()
		forecastData = forecast.getData()
		date = forecast.getForecastDate()
		try:
			urllib.urlopen('http://www.google.com', timeout=2)
			forecast = BohinjForecast()
			forecastData = forecast.getData()
			date = forecast.getForecastDate()
		except:
			self.offlineMode()
			return
		date = date.split('-')
		try:
			self.forecastStatusLabel.setText(u"Bohinj, napoved dne <b>%s.%s.%s</b>" % (date[2], date[1], date[0]))
		except:
			pass
		
		for i in range(4):
			self.forecastDays[i].setText(u'<b>' + forecastData[i].day + u'</b>')
			self.forecastIcons[i].setUrl(QUrl(forecastData[i].icon))
			self.forecastTemperatures[i].setText(u"<b>%s</b> | <b>%s</b>" % (forecastData[i].low, forecastData[i].high))
	
	def offlineMode(self):
		self.forecastStatusLabel.setText(u"Bohinj, napoved ni na voljo.")
		[a.setUrl(QUrl("weather-none-available.png")) for a in self.forecastIcons]
		for i in range(4):
			self.forecastTemperatures[i].setText(u"<b>N/A</b>")
			self.forecastDays[i].setText(u'<b>N/A</b>')
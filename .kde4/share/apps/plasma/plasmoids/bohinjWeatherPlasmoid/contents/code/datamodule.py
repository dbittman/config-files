# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QTimer
from PyQt4.QtGui import QGraphicsGridLayout, QGraphicsLinearLayout
from PyKDE4.plasma import Plasma

from data import Jezero, Bistrica, Cesnjica, Vogel
from updatetimeselector import UpdateTimeSelector

import urllib2 as urllib

class DataModule:
	def __init__(self):
		self.name = "Podatki"
		self.data = None
		self.labels = ["" for i in range(6)]
		self.dataLabels = ["" for i in range(6)]
		self.uiLabels = [Plasma.Label() for i in range(6)]
		self.uiDataLabels = [Plasma.Label() for i in range(6)]
		[l.setAlignment(Qt.AlignRight | Qt.AlignVCenter) for l in self.uiLabels]
		[l.setAlignment(Qt.AlignLeft | Qt.AlignVCenter) for l in self.uiDataLabels]

		self.updateTimer = QTimer()
		self.updateTimer.timeout.connect(self.update)
	
	def makeLayout(self):
		self.layout = QGraphicsLinearLayout(Qt.Vertical)
		self.topDataLayout = QGraphicsLinearLayout(Qt.Horizontal)
		self.dataLayout = QGraphicsGridLayout()
		
		# Data Layout
		self.refreshButton = Plasma.IconWidget()
		self.refreshButton.setIcon("view-refresh")
		self.refreshButton.clicked.connect(self.update)

		##Data labels
		self.timeDataLabel = Plasma.Label()
		self.timeLabel = Plasma.Label()
		self.timeLabel.setText(u"ob")

		#Weather source selector
		self.sourceSelectorCombo = Plasma.ComboBox()
		self.sourceSelectorCombo.addItem(u"Ribčev Laz")
		self.sourceSelectorCombo.addItem(u"Bohinjska Bistrica")
		self.sourceSelectorCombo.addItem(u"Bohinjska Češnjica")
		self.sourceSelectorCombo.addItem(u"Vogel")
		self.sourceSelectorCombo.setMinimumWidth(125)
		self.sourceSelectorCombo.textChanged.connect(self.sourceChanged)

		self.topDataLayout.addItem(self.sourceSelectorCombo)
		self.topDataLayout.addItem(self.timeLabel)
		self.topDataLayout.addItem(self.timeDataLabel)
		self.topDataLayout.addStretch()
		self.topDataLayout.addItem(self.refreshButton)
		
		self.dataUpdateTimeSelector = UpdateTimeSelector()
		self.dataUpdateTimeSelector.setDefaultTime(30)
		self.dataUpdateTimeSelector.setDefaultInterval('min')
		self.dataUpdateTimeSelector.updateTimeSpin.valueChanged.connect(self.dataTimeChanged)
		self.dataUpdateTimeSelector.updateCheckBox.toggled.connect(self.dataTimerToggle)
		
		for i in range(6):
			self.dataLayout.addItem(self.uiLabels[i],i,0)
			self.dataLayout.addItem(self.uiDataLabels[i],i,1)

		self.layout.addItem(self.topDataLayout)
		self.layout.addStretch()
		self.layout.addItem(self.dataLayout)
		self.layout.addStretch()
		self.layout.addItem(self.dataUpdateTimeSelector.layout)
		
	def update(self):
		self.selectDataSource()
		try:
			urllib.urlopen('http://www.google.com', timeout=2)
			self.data.fetchData()
			self.dataLabels = self.data.dataLabels
			self.timeDataLabel.setText(u"<b>%s</b>" % self.data.time)
		except:
			self.offlineMode()
			return
		finally:
			self.updateLabels()
	
	def offlineMode(self):
		self.selectDataSource()
		self.dataLabels = ["Ni na voljo." for i in range(6)]
		self.updateLabels()
		self.timeDataLabel.setText(" ni na voljo.")


	def selectDataSource(self):
		currentSource = self.sourceSelectorCombo.text()

		if currentSource == u"Ribčev Laz":
			self.data = Jezero()
		if currentSource == u"Bohinjska Bistrica":
			self.data = Bistrica()
		if currentSource == u"Bohinjska Češnjica":
			self.data = Cesnjica()
		if currentSource == u"Vogel":
			self.data = Vogel()
		self.labels = self.data.labels


	def updateLabels(self):
		for i in range(6):
				self.uiLabels[i].setText(u"<b>%s</b>" % self.labels[i])
				self.uiDataLabels[i].setText(("%s" % self.dataLabels[i]) if not self.labels[i] == "" else "")
		
	
	def dataTimerToggle(self, toggled):
		if toggled:
			multiplier = 1
			if self.dataUpdateTimeSelector.getInterval() == 'min':
				multiplier = 60
			if self.dataUpdateTimeSelector.getInterval() == 'h':
				multiplier = 60 * 60
			self.updateTimer.start(self.dataUpdateTimeSelector.getTime() * 1000 * multiplier)
			self.update()
		else:
			self.updateTimer.stop()
	
	def sourceChanged(self, text):
		self.update()
	
	def dataTimeChanged(self, value):
		if self.dataUpdateTimeSelector.isChecked():
			self.updateTimer.stop()
		self.dataTimerToggle(self.dataUpdateTimeSelector.isChecked())
		
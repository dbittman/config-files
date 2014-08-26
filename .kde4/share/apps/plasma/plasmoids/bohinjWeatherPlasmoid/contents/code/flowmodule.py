# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt, QTimer, QUrl
from PyQt4.QtGui import QGraphicsGridLayout, QGraphicsLinearLayout, QSizePolicy
from PyQt4.QtWebKit import QGraphicsWebView
from PyKDE4.plasma import Plasma

from fullcamwidget import FullCamWidget
from updatetimeselector import UpdateTimeSelector

from flow import SvJanez, Soteska

import urllib2 as urllib

class FlowModule:
	def __init__(self):
		self.name = "Pretok"
		self.updateTimer = QTimer()
		self.updateTimer.timeout.connect(self.update)
	
	def makeLayout(self):
		self.layout = QGraphicsLinearLayout(Qt.Vertical)
		self.flowComboLayout = QGraphicsLinearLayout(Qt.Horizontal)
		self.flowLabelLayout = QGraphicsGridLayout()
		
		#Flow Layout
		self.flowData = SvJanez()
		self.flowView = QGraphicsWebView()
		self.flowView.setUrl( QUrl(self.flowData.flowImageUrl) )
		self.flowView.setEnabled(False)

		self.flowSelectorCombo = Plasma.ComboBox()
		self.flowSelectorCombo.addItem(u"Sveti Janez")
		self.flowSelectorCombo.addItem(u"Soteska")
		self.flowSelectorCombo.setMinimumWidth(125)
		self.flowSelectorCombo.textChanged.connect(self.flowSourceChanged)

		self.flowRefresh = Plasma.IconWidget()
		self.flowRefresh.setIcon("view-refresh")
		self.flowRefresh.clicked.connect(self.update)

		self.flowEnlargeButton = Plasma.IconWidget()
		self.flowEnlargeButton.setIcon("zoom-in")
		self.flowEnlargeButton.clicked.connect(self.showFullFlowWidget)

		self.flowLabel = Plasma.Label()
		self.flowLabel.setText(u"<b>Pretok:</b> ")
		self.flowDataLabel = Plasma.Label()
		self.flowLevelLabel = Plasma.Label()
		self.flowLevelLabel.setText(u"<b>Višina:</b> ")
		self.flowLevelDataLabel = Plasma.Label()
		self.flowTempLabel = Plasma.Label()
		self.flowTempLabel.setText(u"<b>Temperatura:</b> ")
		self.flowTempDataLabel = Plasma.Label()

		self.flowLabelLayout.addItem(self.flowLevelLabel,0,0)
		self.flowLabelLayout.addItem(self.flowLevelDataLabel,0,1)
		self.flowLabelLayout.addItem(self.flowLabel,1,0)
		self.flowLabelLayout.addItem(self.flowDataLabel,1,1)
		self.flowLabelLayout.addItem(self.flowTempLabel,2,0)
		self.flowLabelLayout.addItem(self.flowTempDataLabel,2,1)
		
		self.flowUpdateTimeSelector = UpdateTimeSelector()
		self.flowUpdateTimeSelector.setDefaultTime(4)
		self.flowUpdateTimeSelector.setDefaultInterval('h')
		self.flowUpdateTimeSelector.updateTimeSpin.valueChanged.connect(self.flowTimeChanged)
		self.flowUpdateTimeSelector.updateCheckBox.toggled.connect(self.flowTimerToggle)
		
		
		self.flowComboLayout.addItem(self.flowSelectorCombo)
		self.flowComboLayout.addStretch()
		self.flowComboLayout.addItem(self.flowEnlargeButton)
		self.flowComboLayout.addItem(self.flowRefresh)
		self.layout.addItem(self.flowComboLayout)
		self.layout.addItem(self.flowView)
		self.layout.addItem(self.flowLabelLayout)
		self.layout.addStretch()
		self.layout.addItem(self.flowUpdateTimeSelector.layout)
		self.layout.itemAt(0).setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, QSizePolicy.DefaultType)
		self.layout.itemAt(2).setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed, QSizePolicy.DefaultType)
	
	def flowTimerToggle(self, toggled):
		if toggled:
			multiplier = 1
			if self.flowUpdateTimeSelector.getInterval() == 'min':
				multiplier = 60
			if self.flowUpdateTimeSelector.getInterval() == 'h':
				multiplier = 60 * 60
			self.updateTimer.start(self.flowUpdateTimeSelector.getTime() * 1000 * multiplier)
			self.update()
		else:
			self.updateTimer.stop()
	
	def flowTimeChanged(self, value):
		if self.flowUpdateTimeSelector.isChecked():
			self.updateTimer.stop()
		self.flowTimerToggle(self.flowUpdateTimeSelector.isChecked())
		
	def flowSourceChanged(self, text):
		if text == "Sveti Janez":
			self.flowData = SvJanez()
		else:
			self.flowData = Soteska()
		self.flowView.setUrl(QUrl(self.flowData.flowImageUrl))
		self.updateFlowLabels()
	
	def updateFlowImage(self):
		self.flowSourceChanged(self.flowSelectorCombo.text())
	
	def updateFlowLabels(self):
		self.flowData.fetchData()
		self.flowDataLabel.setText(u"%s %s" % (self.flowData.currentFlow, u' m3/s'))
		self.flowTempDataLabel.setText(u"%s %s" % (self.flowData.temperature , u' °C'))
		self.flowLevelDataLabel.setText(u"%s %s" % (self.flowData.waterLevel , u' cm'))
	
	def update(self):
		try:
			urllib.urlopen('http://www.google.com', timeout=2)
		except:
			self.offlineMode()
			return
		self.updateFlowLabels()
		self.updateFlowImage()
		
	def offlineMode(self):
		self.flowView.setUrl(QUrl("weather-none-available.png"))
		self.flowDataLabel.setText(u"N/A")
		self.flowTempDataLabel.setText(u"N/A")
		self.flowLevelDataLabel.setText(u"N/A")
	
	def showFullFlowWidget(self):
		fullcamwidget = FullCamWidget()
		fullcamwidget.show(self.flowView.url(), 840, 400)
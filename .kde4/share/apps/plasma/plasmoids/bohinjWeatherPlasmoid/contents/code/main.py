# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsLinearLayout
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

from datamodule import DataModule
from forecastmodule import ForecastModule
from cammodule import CamModule
from flowmodule import FlowModule

import urllib2 as urllib
import re, time, socket


class BohinjWeatherPlasmoid(plasmascript.Applet):
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self)

	def init(self):
		self.setHasConfigurationInterface(False)
		self.theme = Plasma.Svg(self)
		self.theme.setImagePath("widgets/background")
		self.setBackgroundHints(Plasma.Applet.DefaultBackground)
		self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
		
		#Minimize network timeout to avoid clogging UI
		socket.setdefaulttimeout(5)
		
		self.layout = None
		self.makeLayout()
		self.applet.setLayout(self.layout)
		self.resize(350, 300)
		
		self.updateAll()
	
	def updateAll(self):
		try:
			urllib.urlopen('http://www.google.com', timeout=2)
			self.dataModule.update()
			self.forecastModule.update()
			self.camModule.update()
			self.flowModule.update()
		except:
			self.dataModule.offlineMode()
			self.forecastModule.offlineMode()
			self.camModule.offlineMode()
			self.flowModule.offlineMode()

	def makeLayout(self):
		#Layouts
		self.layout = QGraphicsLinearLayout(Qt.Vertical)
		
		self.dataModule = DataModule()
		self.forecastModule = ForecastModule()
		self.camModule = CamModule()
		self.flowModule = FlowModule()
		
		self.dataModule.makeLayout()
		self.forecastModule.makeLayout()
		self.camModule.makeLayout()
		self.flowModule.makeLayout()
		
		#Tabs
		self.tabBar = Plasma.TabBar()
		self.tabBar.addTab(self.dataModule.name, self.dataModule.layout)
		self.tabBar.addTab(self.forecastModule.name, self.forecastModule.layout)
		self.tabBar.addTab(self.camModule.name, self.camModule.layout)
		self.tabBar.addTab(self.flowModule.name, self.flowModule.layout)
		
		self.layout.addItem(self.tabBar)


def CreateApplet(parent):
	return BohinjWeatherPlasmoid(parent)

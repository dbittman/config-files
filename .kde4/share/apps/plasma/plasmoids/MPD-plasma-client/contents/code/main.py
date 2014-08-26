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

import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdecore import *
from PyKDE4.kdeui import *
from PyKDE4.kio import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4.kparts import KParts

from ConfigParser import ConfigParser

import mpd

from settings import Settings

client = mpd.MPDClient()

class MPDPlasmoidClient(plasmascript.Applet):
	def __init__(self, parent, args = None):
		plasmascript.Applet.__init__(self, parent)
		self.setApplet(Plasma.Applet(parent, []))
		self.parent = parent

	def init(self):
		'''Init plasmoid'''
		self.setHasConfigurationInterface(True)
		self.setAspectRatioMode(Plasma.IgnoreAspectRatio)

		## Set full filename
		self.configFilename = ".MPDPCrc"
		pathToFile = os.path.join(os.path.expanduser('~'), \
								  self.configFilename)
		## Trying to read settings from config file
		try:
			configParser = ConfigParser()
			configFile = open(pathToFile)
			configParser.readfp(configFile, pathToFile)
			host = configParser.get('general', 'host')
			port = configParser.get('general', 'port')
			orientation = configParser.get('general', 'orientation')
			icons = configParser.get('general', 'icons')
			stop = False if configParser.get('general', 'stop') == "False" \
				   else True
			popup = False if configParser.get('general', 'popup') == "False" \
					else True
			cover = False if configParser.get('general', 'cover') == "False" \
					else True
			configFile.close()
		## If it not successful then set default settings
		except:
			host = "localhost"
			port = 6600
			orientation = 'h'
			icons = 'u'
			stop = False
			popup = True
			cover = True
			
		self._host = host
		self._port = port
		self._orientation = orientation
		self._icons = icons
		self._stop = stop
		self._popup = popup
		self._cover = cover

		## Trying connect to server
		try:
			client.connect(self._host, self._port)
		except:
			pass

		## Setup user interface
		self.setupInterface(self._orientation, self._icons)

		self.timer = QTimer()

		## Add playback buttons
		self.addButtons()
		self.applet.setLayout(self.buttonsLayout)

		self.data = Plasma.ToolTipContent()
#		if self._popup:
#			Plasma.ToolTipManager.self().setContent(self.applet, self.data)
		
#		self.lastSong = -1
		
		## Every second check connect to server and icon for ppButton
		QObject.connect(self.timer, SIGNAL("timeout()"), self.checkConnect)
		QObject.connect(self.timer, SIGNAL("timeout()"), self.checkIcon)
#		QObject.connect(self.timer, SIGNAL("timeout()"), self.checkSong)

		
		self.timer.start(1000);

	def createConfigurationInterface(self, parent):
		'''Create config interface for config dialog'''
		
		## Create object, containing settings
		self.defaultSettings = {'host': self._host,\
								'port': self._port, \
								'orientation': self._orientation, \
								'icons': self._icons, \
								'stop': self._stop, \
								'popup': self._popup, \
								'cover': self._cover}
		## Create settings object
		## And send settings to constructor
		self.settings = Settings(self, self.defaultSettings)
		settingsPage = parent.addPage(self.settings, \
									  ki18n("Main Options").toString())
		settingsPage.setIcon(KIcon("applications-multimedia"))
		self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
		self.connect(parent, SIGNAL("cancelClicked()"), self.configDenied)

	def showConfigurationInterface(self):
		'''Show created config dialog'''
		dialog = KPageDialog()
		dialog.setFaceType(KPageDialog.List)
		dialog.setButtons(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel))
		self.createConfigurationInterface(dialog)
		dialog.resize(500, 500)
		dialog.exec_()

	def configDenied(self):
		pass

	def configAccepted(self):
		'''This slot called, when "Ok" button pressed'''
		## Load settings
		settingsObject = self.settings.getSettings()
		self._host = settingsObject['host']
		self._port = settingsObject['port']
		self._orientation = settingsObject['orientation']
		self._icons = settingsObject['icons']
		self._stop = settingsObject['stop']
		self._popup = settingsObject['popup']
		self._cover = settingsObject['cover']
		## Save settings to file
		configParser = ConfigParser()
		pathToFile = os.path.join(os.path.expanduser('~'), \
								  self.configFilename)
		configParser.read(pathToFile)
		if not configParser.has_section('general'):
			configParser.add_section('general')
		configParser.set('general', 'host', settingsObject['host'])
		configParser.set('general', 'port', settingsObject['port'])
		configParser.set('general', 'orientation', \
						 settingsObject['orientation'])
		configParser.set('general', 'icons', settingsObject['icons'])
		configParser.set('general', 'stop', settingsObject['stop'])
		configParser.set('general', 'popup', settingsObject['popup'])
		configParser.set('general', 'cover', settingsObject['cover'])

		pathToFile = os.path.join(os.path.expanduser('~'), \
								  self.configFilename)
		configFile = open(pathToFile, "w")
		configParser.write(configFile)
		configFile.close()

		## Reload plasmoid interface with new settings
		self.removeIntarface()
		self.setupInterface(self._orientation, self._icons)
		
	def hoverEnterEvent(self, event):
		'''When mouse over plasmoid, update tooltip content'''
		if self._popup:
			self.updateToolTipInfo()
		else:
			Plasma.ToolTipManager.self().hide(self.applet)

	def updateToolTipInfo(self):
		'''Show popup dialog with song info'''
		song = self.genInfo()
		if self._cover:
			self.data = Plasma.ToolTipContent()
			self.data.setMainText("<font size = +2>" + song['title'] + \
								  "</font>")
			self.data.setSubText('by <b>' + song['artist'] + \
								 '</b> from <b>' +  song['album'] + '<b>')
			self.cover = QPixmap(song['cover'])
			self.data.setImage(self.cover.scaled(80, 80, \
												 Qt.IgnoreAspectRatio, \
												 Qt.SmoothTransformation))
		else:
			self.data = Plasma.ToolTipContent()
			self.data.setMainText("<font size = +2>" + song['title'] + \
								  "</font>")
			self.data.setSubText('by <b>' + song['artist'] + \
								 '</b> from <b>' +  song['album'] + '<b>')
			
		Plasma.ToolTipManager.self().setContent(self.applet, self.data)


	def genInfo(self):
		'''Generate song info'''
		currentSong = client.currentsong()
		song = {'title': '', 'artist': '', 'album': '', 'cover': ''}

		## If tag "title" not exists, take file name
		try:
			song['title'] = currentSong['title']
		except:
			song['title'] = currentSong['file'].split("/")[-1]

		try:
			song['artist'] = currentSong['artist']
		except:
			song['artist'] = 'N/A'

		try:
			song['album'] = currentSong['album']
		except:
			song['album'] = 'N/A'

		pathToCover = unicode(os.path.expanduser('~')) + "/.covers/" + \
					  song['artist'] + "-" + song['album'] + ".jpg"
		
		if os.path.exists(pathToCover):
			song['cover'] = pathToCover
		else:
			song['cover'] = unicode(self.package().path()) + \
					"contents/icons/nocover.jpg"

		return song

	def reconnect(self):
		try:
			client.disconnect()
		except:
			pass
		try:
			client.connect(self._host, self._port)
			self.addButtons()
		except:
			self.removeButtons()
			pass

	def togglePlayback(self):
		if self.isConnected():
			if client.status()['state'] == 'play':
				client.pause()
			else:
				client.play()

	def previous(self):
		if self.isConnected():
			client.previous()

	def stop(self):
		if self.isConnected():
			client.stop()

	def next(self):
		if self.isConnected():
			client.next()

	def disconnect(self):
		client.disconnect()

	def changeIcon(self):
		if client.status()['state'] == 'play':
			self.ppButton.setIcon(self.pauseIcon)
		else:
			self.ppButton.setIcon(self.playIcon)

	def setupOrientation(self, orientation):
		if orientation == 'h':
			self.buttonsLayout = QGraphicsLinearLayout(Qt.Horizontal, \
													   self.applet)
		else:
			self.buttonsLayout = QGraphicsLinearLayout(Qt.Vertical, \
													   self.applet)

	def setupIcons(self, iconTheme):
		if iconTheme == 'u':
			self.prevIcon = QIcon(unicode(self.package().path()) \
								  + "contents/icons/prev.png")
			self.playIcon = QIcon(unicode(self.package().path()) \
								  + "contents/icons/play.png")
			self.pauseIcon = QIcon(unicode(self.package().path()) \
								   + "contents/icons/pause.png")
			self.stopIcon = QIcon(unicode(self.package().path()) \
								  + "contents/icons/stop.png")
			self.nextIcon = QIcon(unicode(self.package().path()) \
								  + "contents/icons/next.png")
			self.connectIcon = QIcon(unicode(self.package().path()) \
									 + "contents/icons/connect.png")
		else:
			self.prevIcon = QIcon(KIcon("media-skip-backward"))
			self.playIcon = QIcon(KIcon("media-playback-start"))
			self.pauseIcon = QIcon(KIcon("media-playback-pause"))
			self.nextIcon = QIcon(KIcon("media-skip-forward"))
			self.stopIcon = QIcon(KIcon("media-playback-stop"))
			self.connectIcon = QIcon(KIcon("media-record"))
			
	def removeIntarface(self):
		self.buttonsLayout.removeItem(self.prevButton)
		self.prevButton.hide()
		self.buttonsLayout.removeItem(self.ppButton)
		self.ppButton.hide()
		self.buttonsLayout.removeItem(self.stopButton)
		self.stopButton.hide()
		self.buttonsLayout.removeItem(self.nextButton)
		self.nextButton.hide()
		try:
			self.buttonsLayout.removeItem(self.connectButton)
			self.connectButton.hide()
		except:
			pass
		del self.prevButton
		del self.ppButton
		del self.stopButton
		del self.nextButton
		del self.connectButton


	def addButtons(self):
		self.buttonsLayout.removeItem(self.connectButton)
		self.connectButton.hide()
		self.buttonsLayout.addItem(self.prevButton)
		self.prevButton.show()
		self.buttonsLayout.addItem(self.ppButton)
		self.ppButton.show()
		self.buttonsLayout.addItem(self.stopButton)
		if self._stop:
			self.stopButton.show()
		else:
			self.stopButton.hide()
			self.buttonsLayout.removeItem(self.stopButton)
		self.buttonsLayout.addItem(self.nextButton)
		self.nextButton.show()
		self.applet.adjustSize()

	def removeButtons(self):
		self.buttonsLayout.removeItem(self.prevButton)
		self.prevButton.hide()
		self.buttonsLayout.removeItem(self.ppButton)
		self.ppButton.hide()
		self.buttonsLayout.removeItem(self.stopButton)
		self.stopButton.hide()
		self.buttonsLayout.removeItem(self.nextButton)
		self.nextButton.hide()
		self.buttonsLayout.addItem(self.connectButton)
		self.connectButton.show()
		self.applet.adjustSize()

	def setupInterface(self, o, i):
		self.setupOrientation(o)
		self.setupIcons(i)
		
	#=== Previous Button ===
		self.prevButton = Plasma.IconWidget(self.prevIcon, "", self.applet)
		self.prevButton.setMaximumWidth(36)
		self.prevButton.setMaximumHeight(36)
		self.prevButton.setContentsMargins(0, 0, 0, 0)

	#=== Play/Pause button ===
		self.ppButton = Plasma.IconWidget(self.pauseIcon \
										  if client.status()['state'] \
										  =='play' \
										  else self.playIcon, "", \
										  self.applet)
		self.ppButton.setMaximumWidth(36)
		self.ppButton.setMaximumHeight(36)
		self.ppButton.setContentsMargins(0, 0, 0, 0)

	#=== Stop Button ===
		self.stopButton = Plasma.IconWidget(self.stopIcon, "", self.applet)
		self.stopButton.setMaximumWidth(36)
		self.stopButton.setMaximumHeight(36)
		self.stopButton.setContentsMargins(0, 0, 0, 0)

	#=== Next Button ===
		self.nextButton = Plasma.IconWidget(self.nextIcon, "", self.applet)
		self.nextButton.setMaximumWidth(36)
		self.nextButton.setMaximumHeight(36)
		self.nextButton.setContentsMargins(0, 0, 0, 0)

	#=== ConnectButton ===
		self.connectButton = Plasma.IconWidget(self.connectIcon, "", \
							 self.applet)
		self.connectButton.setMaximumWidth(36)
		self.connectButton.setMaximumHeight(36)
		self.connectButton.setContentsMargins(0, 0, 0, 0)
		
		if self.isConnected():
			self.addButtons()
		else:
			self.removeButtons()
			
		QObject.connect(self.prevButton, SIGNAL("clicked()"), \
						self.previous)
		QObject.connect(self.ppButton, SIGNAL("clicked()"), \
						self.togglePlayback)
		QObject.connect(self.ppButton, SIGNAL("clicked()"), \
						self.changeIcon)
		QObject.connect(self.stopButton, SIGNAL("clicked()"), \
						self.stop)
		QObject.connect(self.stopButton, SIGNAL("clicked()"), \
						self.changeIcon)
		QObject.connect(self.nextButton, SIGNAL("clicked()"), \
						self.next)
		QObject.connect(self.connectButton, SIGNAL("clicked()"), \
						self.addButtons)
		QObject.connect(self.connectButton, SIGNAL("clicked()"), \
						self.reconnect)

	def isConnected(self):
		try:
			client.ping()
			return True
		except:
			return False

	def showVolumeDialog(self):
		self.volumeDialog.move(self.popupPosition(self.dialog.sizeHint()))
		if self.volumeDialog.isVisible():
			self.volumeDialog.hide()
		else:
			self.volumeDialog.show()

	def checkConnect(self):
		if not self.isConnected():
			try:
				self.reconnect()
			except:
				pass
	
	def checkIcon(self):
		try:
			if client.status()['state'] == 'play':
				self.ppButton.setIcon(self.pauseIcon)
			else:
				self.ppButton.setIcon(self.playIcon)
		except:
			pass

#	def checkSong(self):
#		if self.lastSong == -1:
#			self.lastSong = client.currentsong()['id']
#		self.newSong = client.currentsong()['id']
#		if not (self.newSong == self.lastSong):
#			Plasma.ToolTipManager.self().setState(0)
#			Plasma.ToolTipManager.self().show(self.applet)
#			self.lastSong = self.newSong
	
def CreateApplet(parent):
	return MPDPlasmoidClient(parent)

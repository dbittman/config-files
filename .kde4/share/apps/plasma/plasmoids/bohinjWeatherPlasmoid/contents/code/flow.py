# -*- coding: utf-8 -*-

import urllib2 as urllib, re

class SvJanez:
	def __init__(self):
		self.flowImageUrl = u"http://lab.fs.uni-lj.si/lasin/srek/~02.png"

	def fetchData(self):
		try:
			html = urllib.urlopen("http://www.arso.gov.si/vode/podatki/stanje_voda.html").read()
			start = html.index('Avtomatske opazovalne postaje')
			html = html[start:]
			start = html.index('<tr><td class="onlineimena">Sava Bohinjka - Sv.Janez</td>')
			html = html[start:]

			levelRe = re.compile('([1-9][0-9][0-9]|[1-9][0-9]|[0-9])')
			level = re.findall(levelRe,html)[0]
			start = html.index(level)
			html = html[start+len(level):]

			flowRe = re.compile('([1-9][0-9][0-9]|[1-9][0-9]|[0-9])(\.[0-9])*')
			flow = "".join(re.findall(flowRe, html)[0])
			start = html.index(flow)
			html = html[start+len(flow):]

			tempRe = re.compile('([-])*([1-9][0-9]|[0-9])(\.[0-9])*')
			temp = "".join(re.findall(tempRe, html)[0])

			self.waterLevel  = level
			self.currentFlow = flow
			self.temperature = temp
		except:
			self.waterLevel = 'N/A'
			self.currentFlow = 'N/A'
			self.temperature = 'N/A'

class Soteska:
	def __init__(self):
		self.flowImageUrl = u"http://lab.fs.uni-lj.si/lasin/srek/~03.png"
	def fetchData(self):
		self.currentFlow = 'N/A'
		self.waterLevel  = 'N/A'
		self.temperature = 'N/A'
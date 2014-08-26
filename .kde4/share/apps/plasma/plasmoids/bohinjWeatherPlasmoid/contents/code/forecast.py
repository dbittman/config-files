# -*- coding: utf-8 -*-

import urllib

from xml.dom.minidom import parseString

class BohinjForecast():
	def __init__(self):
		self.days = {'Mon':u'Pon', 'Tue':u'Tor', 'Wed':u'Sre', 'Thu':u'Čet', 'Fri':u'Pet', 'Sat':u'Sob', 'Sun': u'Ned'}

	def getData(self):
		data = urllib.urlopen("http://www.google.com/ig/api?weather=bohinj").read()
		self.dom = parseString(data)
		self.data = []

		for node in self.dom.getElementsByTagName("forecast_conditions"):
			for child in node.getElementsByTagName("day_of_week"):
				day = self.days[child.getAttribute("data")]
			for child in node.getElementsByTagName("high"):
				high = self.convertFromF(child.getAttribute("data"))
			for child in node.getElementsByTagName("low"):
				low = self.convertFromF(child.getAttribute("data"))
			for child in node.getElementsByTagName("icon"):
				icon = 'http://www.google.com' + child.getAttribute("data")
			for child in node.getElementsByTagName("condition"):
				condition = child.getAttribute("data")
			self.data.append(WeatherInfo(day,low,high,icon,condition))
		return self.data
		
	def getForecastDate(self):
		for node in self.dom.getElementsByTagName("forecast_information"):
			for child in node.getElementsByTagName("forecast_date"):
				return child.getAttribute("data")
				
	def convertFromF(self, f):
		f = float(f)
		return "%d" % int((f - 32) * 5/9)
		
class NoForecast():
	def getData(self):
		return [WeatherInfo('N/A','N/A','N/A','','N/A') for i in range(4)]
	
	def getForecastDate(self):
		return 'Ni na voljo.'

class WeatherInfo():
	def __init__(self, day, low, high, icon, condition):
		self.day = day
		self.low = low
		self.high = high
		self.icon = icon
		self.condition = condition
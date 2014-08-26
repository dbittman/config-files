# -*- coding: utf-8 -*-

import urllib2 as urllib
import re

#Podatki so uporabljeni s strani www.bohinj.si
#Data is used from webpage www.bohinj.si
class Jezero:
	def __init__(self):
		self.labels = [u"Zunanja temperatura:", u"Povprečna zunanja temperatura:", u"Temperatura jezera:", u"Vlažnost:", u"Zračni tlak:", u"Višina:"]

	def fetchData(self):
		weatherData = urllib.urlopen("http://www.bohinj.si/cam/weather.js").read().replace('\t','').replace('\r','').replace("var",'').replace(';','').split("\n")
		waterData = urllib.urlopen("http://www.bohinj.si/cam/thst2.js").read().replace('\t','').replace('\r','').replace("var",'').replace(' ','').replace(';','').split("\n")

		rex = re.compile('[0-2]*[0-9]+:[0-5][0-9]:[0-5][0-9]')
		self.time = re.findall(rex, weatherData[17])[0]
		weatherData = [a.replace(' ','') for a in weatherData]

		outTemp = weatherData[4][weatherData[4].index('"'):].replace('"','') + u"°C"
		outTempAvg = weatherData[5][weatherData[5].index('"'):].replace('"','') + u"°C"
		outHum = weatherData[6][weatherData[6].index('"'):].replace('"','') + u"%"
		pressure = weatherData[12][weatherData[12].index('"'):].replace('"','') + u" mbar" 
		elevation = weatherData[18][weatherData[18].index('"'):].replace('"','') + u"m"
		lakeTemp = waterData[0][waterData[0].index('"'):].replace('"','') + u"°C"
		self.dataLabels = [outTemp, outTempAvg, lakeTemp, outHum, pressure, elevation]

#Podatki so uporabljeni s strani http://bohinjska-bistrica.zevs.si/
#Data is used from webpage http://bohinjska-bistrica.zevs.si/
class Bistrica:
	def __init__(self):
		self.labels = [u"Zunanja Temperatura: ", u"Vlažnost: ", u"Tlak: ", u"Veter: ", u"Višina: ", u""]
		
	def fetchData(self):
		data = urllib.urlopen("http://bohinjska-bistrica.zevs.si/").read()
		rex = re.compile('[0-2]*[0-9]+:[0-5][0-9]')
		self.time = re.findall(rex, data)[0]
		
		rex = re.compile(r'<.*?>')
		data = rex.sub('',data).replace('\n','')
		try:
			tempIndex = data.index('Temperatura:') + len('Temperatura:')
			data = data[tempIndex:]
			outTemp = data[:data.index('C')-1].strip().replace(',','.')
		except:
			outTemp = 'N/A'
		try:
			humIndex = data.index('Vlaga:') + len('Vlaga:')
			data = data[humIndex:]
			outHum = data[:data.index('%')+1].strip().replace(' ','')
		except:
			outHum = 'N/A'
		
		try:
			pressIndex = data.index('ni tlak:') + len('ni tlak:')
			data = data[pressIndex:]
			pressure = data[:data.index('hPa') + len('hPa')]
		except:
			pressure = 'N/A'
		
		try:
			windIndex = data.index('Veter:') + len('Veter:')
			data = data[windIndex:]
			wind = data[:data.index('km/h') + len('km/h')].replace(',','.')
		except:
			wind = 'N/A'

		elevation = "509.4 m"
		self.dataLabels = [outTemp + u"°C", outHum, pressure, wind, elevation, u""]

#Podatki so uporabljeni s strani www2.arnes.si/~smisma1/bohinj.html
#Data is used from webpage www2.arnes.si/~smisma1/bohinj.html
class Cesnjica:
	def __init__(self):
		self.labels = [u"Zunanja Temperatura: ", u"Vlažnost: ", u"Tlak: ", u"Višina snega: ", u"Veter: ", u"Višina: "]

	def fetchData(self):
		data = urllib.urlopen("http://www2.arnes.si/~smisma1/bohinj.html").read()
		rex = re.compile(r'<.*?>')
		data = rex.sub('',data).replace('\n','')

		rex = re.compile('[0-2]*[0-9]+:[0-5][0-9]')
		self.time = re.findall(rex, data)[0]
		try:
			tempIndex = data.index('TEMPERATURA')
			data = data[tempIndex:]
			outTemp = data[ (data.index('trenutno') + len('trenutno')) : data.index('\xb0C') ].strip().replace(',','.') + u'°C'
		except:
			outTemp = 'N/A'

		try:
			tempIndex = data.index('ZUNANJA VLAGA')
			data = data[tempIndex:]
			outHum = data[ (data.index('trenutno') + len('trenutno')) : data.index('%') ].strip() + '%'
		except:
			outHum = 'N/A'
		
		try:
			tempIndex = data.index('TLAK')
			data = data[tempIndex:]
			pressure = data[ (data.index('trenutno') + len('trenutno')) : (data.index('hPa') + len('hPa')) ].strip().replace(',','.')
		except:
			pressure = 'N/A'
		
		try:
			tempIndex = data.index('VETER')
			data = data[tempIndex:]
			wind = data[ (data.index('trenutno') + len('trenutno')) : (data.index('km/h') + len('km/h')) ].strip().replace(',','.')
			tempIndex = data.index('SMER VETRA')
			data = data[tempIndex:]
			windDir = data[ : data.index('BAZA OBLAKOV')].split('/')[1].strip().split(' ')[0]
			wind = u"%s (%s)" %(wind, windDir)
		except:
			wind = 'N/A'
		
		try:
			tempIndex = data.index('ne razmere') + len(u'ne razmere')
			data = data[tempIndex:]
			snow = data[ : (data.index('cm') + len('cm')) ].strip().replace(',','.')
		except:
			snow = 'N/A'

		elevation  = '599 m'
		self.dataLabels = [outTemp, outHum, pressure, snow, wind , elevation]
		
#Podatki so uporabljeni s strani www.vogel.si
#Data is used from webpage www.vogel.si
class Vogel:
	def __init__(self):
		self.labels = [u"Temperatura (nihalka): ", u"Temperatura (Orlove glave): ", u"Veter (Nihalka): ", u"Veter (Orlove glave): ", u"Višina snega: ", ""]

	def fetchData(self):
		orlovedata = urllib.urlopen("http://www.snezni-telefon.si/images/vogel/weather.js").read().replace('\t','').replace('\r','').replace("var",'').replace(';','').split("\n")
		data = urllib.urlopen("http://www.vogel.si").read()
		rex = re.compile(r'<.*?>')
		data = rex.sub('',data).replace('\n','')

		rex = re.compile('[0-2]*[0-9]+:[0-5][0-9]')
		self.time = re.findall(rex, orlovedata[17])[0]

		orlovedata = [a.replace(' ','') for a in orlovedata]
		
		
		windSpeedOrlove = orlovedata[0][orlovedata[0].index('"'):].replace('"','')
		windDirOrlove = orlovedata[3][orlovedata[3].index('"'):].replace('"','')
		orloveWind = "%s m/s (%s)" % (windSpeedOrlove, windDirOrlove)
		orloveTemp = orlovedata[4][orlovedata[3].index('"'):].replace('"','')
		try:
			startIndex = data.index('Vi\xc5\xa1ina snega: ') + len('Vi\xc5\xa1ina snega: ')
			endIndex = data.index('<div style="position: absolute; width: 100px; height: 71px; z-index: 2; left: 8px; top: 44px" \r        id="layer18">')
			data = data[startIndex : endIndex]

			snowHeight = data[:data.index('\r')].strip()
		except:
			snowHeight = 'N/A'
		
		try:
			startIndex = data.index('Temp. (nihalka zg.): ') + len('Temp. (nihalka zg.): ')
			endIndex = data.index('\xc2\xb0C')
			nihalkaTemp = data[startIndex : endIndex].strip()
			data = data[endIndex:]
		except:
			nihalkaTemp = 'N/A'
		
		try:
			startIndex = data.index('Veter (nihalka zg.): ') + len('Veter (nihalka zg.): ')
			endIndex = data.index('\r\t\t')
			nihalkaWind = data[startIndex : endIndex].strip()
		except:
			nihalkaWind = 'N/A'

		self.dataLabels = [nihalkaTemp + u"°C", orloveTemp + u"°C", nihalkaWind, orloveWind, snowHeight, ""]
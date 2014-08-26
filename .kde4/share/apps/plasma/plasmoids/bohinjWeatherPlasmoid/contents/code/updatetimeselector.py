# -*- coding: utf-8 -*-

from PyKDE4.plasma import Plasma
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsLinearLayout

class UpdateTimeSelector:
	def __init__(self):
		self.layout = QGraphicsLinearLayout(Qt.Horizontal)
		self.updateCheckBox = Plasma.CheckBox()
		self.updateCheckBox.setText(u'&Samodejno osveževanje:')

		self.updateTimeSpin = Plasma.SpinBox()
		self.updateTimeSpin.setRange(0,60)
		self.updateTimeSpin.setValue(5)
		self.updateTimeSpin.valueChanged.connect(self.updateTimeChanged)

		self.intervalSelector = Plasma.ComboBox()
		[self.intervalSelector.addItem(i) for i in ('s', 'min', 'h')]

		self.layout.addItem(self.updateCheckBox)
		self.layout.addStretch()
		self.layout.addItem(self.updateTimeSpin)
		self.layout.addItem(self.intervalSelector)
		self.layout.itemAt(1).setMaximumWidth(45)
		self.layout.itemAt(2).setMaximumWidth(45)
	
	def updateTimeChanged(self):
		if self.updateTimeSpin.value() == 60:
			if self.intervalSelector.nativeWidget().currentIndex() < 2:
				self.intervalSelector.nativeWidget().setCurrentIndex(self.intervalSelector.nativeWidget().currentIndex() + 1)
				self.updateTimeSpin.setValue(1)
				return
		if self.updateTimeSpin.value() == 0:
			if self.intervalSelector.nativeWidget().currentIndex() > 0:
				self.intervalSelector.nativeWidget().setCurrentIndex(self.intervalSelector.nativeWidget().currentIndex() - 1)
				self.updateTimeSpin.setValue(59)
				return
			else:
				self.updateTimeSpin.setValue(1)

	def setDefaultTime(self, time):
		self.updateTimeSpin.setValue(time)

	def setDefaultInterval(self, interval):
		try:
			self.intervalSelector.setCurrentIndex(0)
		except:
			self.intervalSelector.nativeWidget().setCurrentItem("s")
		if interval == 'min':
			try:
				self.intervalSelector.setCurrentIndex(1)
			except:
				self.intervalSelector.nativeWidget().setCurrentItem("min")
		if interval == 'h':
			try:
				self.intervalSelector.setCurrentIndex(2)
			except:
				self.intervalSelector.nativeWidget().setCurrentItem("h")
	
	def getTime(self):
		return self.updateTimeSpin.value()
	def getInterval(self):
		return self.intervalSelector.text()
	def isChecked(self):
		return self.updateCheckBox.isChecked()
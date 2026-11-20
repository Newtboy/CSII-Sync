import pytest

from LAB_12.television import *

class TestTelevision: # {
	def setup_method(self):
		self.tv = Television()

	def testInit(self): # {
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

	def testPower(self): # {
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
		self.tv.power()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.power()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

	def testMute(self): # {
		self.tv.power()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
		self.tv.mute()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"
		self.tv.power()
		self.tv.mute()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 2"

	def testChannelUp(self):
		self.tv.channel_up()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
		self.tv.power()
		self.tv.channel_up()
		assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"
		self.tv.channel_up()
		assert str(self.tv) == "Power = True, Channel = 2, Volume = 0"
		self.tv.channel_up()
		assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"
		self.tv.channel_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

	def testChannelDown(self):
		self.tv.channel_down()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
		self.tv.power()
		self.tv.channel_down()
		assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"
		self.tv.channel_down()
		assert str(self.tv) == "Power = True, Channel = 2, Volume = 0"
		self.tv.channel_down()
		assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"
		self.tv.channel_down()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

	def testVolUp(self):
		self.tv.volume_up()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
		self.tv.power()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
		self.tv.mute()
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

	def testVolDown(self):
		self.tv.volume_down()
		assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
		self.tv.power()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.volume_down()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
		self.tv.volume_up()
		self.tv.volume_up()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"
		self.tv.volume_down()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
		self.tv.mute()
		self.tv.volume_down()
		assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
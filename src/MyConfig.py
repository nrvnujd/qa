# -*- coding: utf-8 -*-

import ConfigParser

class MyConfig:

	_instance = ConfigParser.ConfigParser()
	_instance.read("conf/config.conf")

	@classmethod
	def get(self, section, item):
		return self._instance.get(section, item)

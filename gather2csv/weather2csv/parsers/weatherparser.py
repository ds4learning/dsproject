import json
import time

class WeatherParser(object):
	def __init__(self):
		pass

	def parse_JSON(self,json_string):
		"""
        parses weather data from the json_string
		"""
		print(json_string)
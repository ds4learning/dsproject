import requests as req
import gather2csv.constants as constants


class LocationData(object):

	"""
		LocationData class , will provide methods that gather data from OpenWeatherMap data given a name.
		
		:param parsers: contains an instance of the parser used to parse the location data from OpenWeatherMap
    	:type parsers: class instance
	"""
	def __init__(self,parser):
		self.parser_ = parser

		
	def lat_lon_weather(self,lat,lon):
		"""
		Sends a query to OpenWeatherMap for the weather at (lon,lat)
		and returns the weather data.
		
		:param lat: the location's latitude, must be between -90.0 and 90.0
        :type lat: int/float
        :param lon: the location's longitude, must be between -180.0 and 180.0
        :type lon: int/float
        :returns: parsed data 

		"""
		#https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22
		uri = constants.WEATHER_URL
		resp = requests.get(uri).text

		return resp





from api_request import Weather_API, WeatherRequest

class GeoData():
	def __init__(self, weather_request: WeatherRequest):
		self.weather_request = weather_request

		self.data = {"min_temp":[],
					 "max_temp":[],
					 "avg_temp":[],
					 "humidity":[],
					 "icon":[],
					 "location":[],
					 "current":[],
					 "days":[],
					 "image":""}

		weather_api_object = Weather_API(weather_request)
		self.response = weather_api_object.get_api_json()


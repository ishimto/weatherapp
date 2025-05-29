from pathlib import Path
from typing import Union, Dict
from datetime import date, timedelta
from modules.consts import Images, InvalidApiKey
from modules.basemodels import ForeCast, Location
from modules.api_request import Weather_API, WeatherRequest



class GeoData():
	def __init__(self, weather_request: WeatherRequest):
		self.weather_request = weather_request
		self.json_response, self.status_code = self.get_api_values()	

		if self.status_code == 403:
			raise InvalidApiKey(self.json_response)

		if "error" in self.json_response:
			return

		self.forecast = ForeCast(**self.json_response["forecast"])	
		

		self.data = {"min_temp":[],
					 "max_temp":[],
					 "avg_temp":[],
					 "humidity":[],
					 "icon":[],
					 "location":[],
					 "current":[],
					 "days":[],
					 "image":self.get_background_image()}

		self.parse_api_forecastday()
		self.pasre_api_location()
		self.string_format_weekdays()
		self.get_background_image()


	def get_api_values(self) -> Union[Dict, int]:
		api = Weather_API(self.weather_request)
		return api.json_response, api.status_code


	def parse_api_forecastday(self) -> None:	
		"""
		in for loop:
		using pydantic to parse data, look for basemodels module
		each index in json have class that represent it.
		current temp_c below for loop added to save the order in the "current" list, for later.
		"""

		current_date = date.today()
		
		for forecastday in self.forecast.forecastday:
			fday = forecastday.day

			self.data["min_temp"].append(fday.mintemp_c)
			self.data["max_temp"].append(fday.maxtemp_c)
			self.data["avg_temp"].append(fday.avgtemp_c)
			self.data["humidity"].append(fday.avghumidity)
			self.data["icon"].append(fday.condition.icon)
		
		self.data["current"].append(self.json_response["current"]["temp_c"])
		self.data["current"].append(self.forecast.forecastday[0].day.condition.text)
	

	def pasre_api_location(self) -> None:
		location = Location(**self.json_response["location"])
		self.data["location"].append(location.name)
		self.data["location"].append(location.country)
		self.data["location"].append(location.tz_id)	


	def string_format_weekdays(self) -> None:
		"""
		api returns date,
		thats function make it human readable and return weekdays for client in weather.html
		"""
		
		current_date = date.today()

		# sets relevant days in the list
		for i in range(self.weather_request.amount_of_days):
			self.data["days"].append(current_date + timedelta(days=i))

		# convert the date to weekday name i.e Sunday, Monday etc...
		for i in range(1, self.weather_request.amount_of_days):
			self.data["days"][i] = self.data["days"][i].strftime("%A")


		self.data["days"][0] = "Today"
		try:
			self.data["days"][1] = "Tomorrow"

		finally:
			return


	def get_background_image(self) -> str:
		
		"""
		background for weather.html depend on state in user location input
		"""
		first_day_state = self.forecast.forecastday[0].day.condition.text

		for state in Images.STATES.value:
			if state.lower() in first_day_state.lower():
				return Path(Images.BACKGROUD_ROOT_PATH.value / f'{state}.txt').read_text()

		return Path(Images.BACKGROUD_ROOT_PATH.value / f'sunny.txt').read_text()

import sys
import requests
from pathlib import Path
from dataclasses import dataclass
#import logging
from modules.envs import API_KEY

#logger = logging.getLogger()

@dataclass
class WeatherRequest():
	city: str
	amount_of_days: int


class Weather_API():
	def __init__(self, weather_request: WeatherRequest):
		self.weather_request = weather_request
		self.json_response, self.status_code = self.get_api_json()
		
	def get_api_json(self) -> dict:

		url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={self.weather_request.city}&days={self.weather_request.amount_of_days}&aqi=no&alerts=no"

		response = requests.get(url)
		#logger.info(f"api response in 'api_request' module: {response.json()}")
		return response.json(), response.status_code

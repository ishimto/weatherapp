import sys
import requests
from pathlib import Path
from dataclasses import dataclass

@dataclass
class WeatherRequest():
	city: str
	amount_of_days: int


class Weather_API():
	def __init__(self, weather_request: WeatherRequest):
		self.weather_request = weather_request
		self.json_response = self.get_api_json()
		
	def get_api_json(self) -> dict:
		api_key_path = Path("api_key.txt")

		api_key = api_key_path.read_text()

		url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={self.weather_request.city}&days={self.weather_request.amount_of_days}&aqi=no&alerts=no"

		response = requests.get(url)
		return response.json()

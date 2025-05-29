import pytest
from pathlib import Path
from api_mock import valid_response, invalid_location_response
from basemodels import ForeCast, Location, Current



def test_forecastdays_parse(valid_response):
	forecast = ForeCast(**valid_response["forecast"])
	
	assert forecast.forecastday[0].date == "2025-01-19", "excpected 2025-01-19, str"
	assert forecast.forecastday[0].day.maxtemp_c == 17.3, "excpected 17.3"
	assert forecast.forecastday[0].day.mintemp_c == 13.8, "excpected 13.8"
	assert forecast.forecastday[0].day.avgtemp_c == 15.6, "excpected 15.6"
	assert forecast.forecastday[0].day.avghumidity == 63, "excpected 63"
	assert forecast.forecastday[0].day.condition.text == "Partly Cloudy ", "excpected Partly Cloudy"

	assert forecast.forecastday[1].date == "2025-01-20", "excpected 2025-01-20, str"
	assert forecast.forecastday[1].day.maxtemp_c == 17.4, "excpected 17.4"
	assert forecast.forecastday[1].day.mintemp_c == 13.8, "excpected 13.8"
	assert forecast.forecastday[1].day.avgtemp_c == 15.7, "excpected 15.7"
	assert forecast.forecastday[1].day.condition.text == "Partly Cloudy ", "excpected Partly Cloudy"

def test_location_parse(valid_response):
	location = Location(**valid_response["location"])
	
	assert location.name == "Tel Aviv-Yafo"
	assert location.country == "Israel"
	assert location.tz_id == "Asia/Jerusalem"


def test_current_pasre(valid_response):
	current = Current(**valid_response["current"])

	assert current.temp_c == 13.1, "excpected 13.1"



def test_invalid_location(invalid_location_response):
	assert invalid_location_response["error"]["message"] == "No matching location found.", "excpected non location"


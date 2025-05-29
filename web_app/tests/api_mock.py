import pytest
from unittest.mock import patch
from backend_weather import GeoData
from api_request import Weather_API, WeatherRequest

api_valid_json = {
	"location": {
		"name": "Tel Aviv-Yafo",
		"country": "Israel",
		"tz_id": "Asia/Jerusalem",
	},
	"current": {
		"temp_c": 13.1,
	},
	"forecast": {
		"forecastday": [
		{
			"date": "2025-01-19",
			"day": {
				"maxtemp_c": 17.3,
				"mintemp_c": 13.8,
				"avgtemp_c": 15.6,
				"avghumidity": 63,
				"condition": {
					"text": "Partly Cloudy ",
					"icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
					}
				},
			},
			{
				"date": "2025-01-20",
				"day": {
					"maxtemp_c": 17.4,
					"mintemp_c": 13.8,
					"avgtemp_c": 15.7,
					"avghumidity": 68,
					"condition": {
						"text": "Partly Cloudy ",
						"icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
						"code": 1003
						}
					},
				}
					]
				}
}


api_invalid_location_response = {
					"error": {
						"code": 1006,
						"message": "No matching location found."
						}
}

#mock_invalid_response = Mock(return_value=invalid_response)

@pytest.fixture
def valid_response():

	weather_request = WeatherRequest("Tel Aviv-Yafo", 2)
	
	with patch.object(Weather_API, "get_api_json") as mock_method:
		mock_method.return_value = api_valid_json
		forecast = GeoData(weather_request)
	
	return forecast.response


@pytest.fixture
def invalid_location_response():

	weather_request = WeatherRequest("fdgdfgdfgdgfddfg", 2)

	with patch.object(Weather_API, "get_api_json") as mock_method:
		mock_method.return_value = api_invalid_location_response
		forecast = GeoData(weather_request)

	return forecast.response


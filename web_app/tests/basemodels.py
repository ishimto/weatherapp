from pydantic import BaseModel
from typing import List

class Current(BaseModel):
	temp_c: float


class Location(BaseModel):
	name: str
	country: str
	tz_id: str

class Condition(BaseModel):
	icon: str
	text: str

class Day(BaseModel):
	maxtemp_c: float
	mintemp_c: float
	avgtemp_c: float
	avghumidity: float
	condition: Condition

class ForeCastDays(BaseModel):
	day: Day
	date: str

class ForeCast(BaseModel):
	forecastday: List[ForeCastDays]

import os
import sys
from enum import Enum
from pathlib import Path

class Images(Enum):
	BACKGROUD_ROOT_PATH = Path('background')
	STATES = ['snow', 'rain', 'overcast', 'cloudy', 'sunny']


class InvalidApiKey(Exception):
	def __init__(self, msg: str):
		super().__init__(msg)

import pytest
import requests


def test_status_code():
    assert requests.get("http://127.0.0.1:8000/").status_code == 200, "Excpected 200"

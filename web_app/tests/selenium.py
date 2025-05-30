import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def test_index_html(driver):
    driver.get("http://127.0.0.1:1234/")
    assert driver.title == ""
    assert driver.find_element(By.NAME, "city")
    assert driver.find_element(By.NAME, "forecast_days")


def test_weather_html(driver):
    driver.get("http://127.0.0.1:1234/")
    assert driver.title == ""
    select = Select(driver.find_element(By.NAME, "forecast_days"))
    select.select_by_value("3")
    search_bar = driver.find_element(By.NAME, "city")
    search_bar.send_keys("haifa")
    search_bar.send_keys(Keys.RETURN)
    assert driver.title == "weather"


def test_empty_city(driver):
    driver.get("http://127.0.0.1:1234/")
    assert driver.title == ""
    select = Select(driver.find_element(By.NAME, "forecast_days"))
    select.select_by_value("3")
    search_bar = driver.find_element(By.NAME, "city")
    search_bar.send_keys(Keys.RETURN)
    assert driver.title == ""


def test_invalid_city(driver):
    driver.get("http://127.0.0.1:1234/")
    search_bar = driver.find_element(By.NAME, "city")
    search_bar.send_keys("dflgjfdlkgjfdlkgdfjlkdfjlkjkdflsdfdfgdfgfdgdffdg")
    search_bar.send_keys(Keys.RETURN)
    assert "no matching location found" in driver.page_source.lower()
    assert driver.title == "Error"


def test_404_html(driver):
    driver.get("http://127.0.0.1:1234/sdfsdf")
    assert "404" in driver.page_source
    assert driver.title == "Error"


def test_contact_us_html(driver):
    driver.get("http://127.0.0.1:1234/contact_us")
    assert driver.title == "Contact US"
    assert driver.find_element(By.NAME, "user_email")
    assert driver.find_element(By.NAME, "subject")
    assert driver.find_element(By.NAME, "user_message")

    email = driver.find_element(By.NAME, "user_email")
    subject = driver.find_element(By.NAME, "subject")
    message = driver.find_element(By.NAME, "user_message")
    email.send_keys("testemail@gmai.com")
    subject.send_keys("test")
    message.send_keys("this is test with selenium")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.title == ""

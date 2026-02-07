import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader

@pytest.fixture
def driver():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    config = ConfigReader.read_config()
    driver.maximize_window()
    driver.get(config['url'])
    yield driver

    driver.quit()
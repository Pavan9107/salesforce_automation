from datetime import datetime

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')

        if driver:
            timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)





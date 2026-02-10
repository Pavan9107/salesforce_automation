from Pages.login_page import LoginPage
from utils.config_reader import ConfigReader

def test_login(driver):
    config = ConfigReader.read_config()
    login_page = LoginPage(driver)
    login_page.login(config['username'], config['password'])

    assert login_page.is_login_successful()




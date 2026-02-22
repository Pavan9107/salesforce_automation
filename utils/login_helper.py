from utils.config_reader import ConfigReader
from Pages.login_page import LoginPage

def todo_login(driver):
    config = ConfigReader.read_config()
    login_page = LoginPage(driver)
    login_page.login(config['username'], config['password'])

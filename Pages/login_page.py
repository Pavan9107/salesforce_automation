from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
logger = get_logger("Login_test")

class LoginPage:

    User_name = (By.ID, 'username')
    Password = (By.ID, 'password')
    Login = (By.ID, 'Login')
    verification_code = (By.XPATH, '//input[@id="emc"]')
    verify_button = (By.XPATH, '//input[@type="submit"]')


    def __init__(self, driver):
        self.driver = driver
        logger.info("driver initialized")
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.User_name)).clear()
        logger.info("entering username")
        self.driver.find_element(*self.User_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.Password).clear()
        self.driver.find_element(*self.Password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.Login).click()


    def wait_for_otp(self):
        wait = WebDriverWait(self.driver, 60)
        otp_field = wait.until(EC.visibility_of_element_located(self.verification_code))
        otp = input("enter OTP: ")
        otp_field.send_keys(otp)
        wait.until(lambda driver: otp_field.get_attribute('value')== otp)
        self.driver.find_element(*self.verify_button).click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.wait_for_otp()













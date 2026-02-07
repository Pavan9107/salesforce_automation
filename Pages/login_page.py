from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class loginPage:

    User_name = (By.ID, 'username')
    Password = (By.ID, 'password')
    Login = (By.ID, 'Login')
    Welcome_page = (By.XPATH, '//span[text()= "Welcome"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.User_name)).clear()
        self.driver.find_element(*self.User_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.Password).clear()
        self.driver.find_element(*self.Password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.Login).click()

    def wait_for_otp(self):
        print("Waiting for OTP")
        input("Press enter to continue...")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.wait_for_otp()

    def is_login_successful(self):
        return self.wait.until(EC.presence_of_element_located(self.Welcome_page))













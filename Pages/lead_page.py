from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeadPage:
    lead_tab = (By.XPATH, '(//span[text()="Leads"])[1]')
    new_button = (By.XPATH, "//button[text()='New']")
    salutation = (By.XPATH, "(//span[contains(text(), '{}')])[1]")
    lastname = (By.XPATH, "//input[@name='lastName']")
    company = (By.XPATH, "//input[@id='input-315']")
    lead_status = (By.XPATH, "(//span[contains(text(),'Open - Not Contacted')])[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.lead_tab = (By.XPATH, '(//span[text()="Leads"])[1]')

    def lead_page_inputs(self):
        self.wait.until(EC.element_to_be_clickable(self.lead_tab)).click()
        self.driver.find_element(*self.new_button).click()
        self.driver.find_element(*self.new_button).click()
        self.driver.find_element(*self.salutation).send_keys("Mr.")
        self.driver.find_element(*self.lastname).send_keys("test")
        self.driver.find_element(*self.company).send_keys("abc")
        self.driver.find_element(*self.lead_status).click()





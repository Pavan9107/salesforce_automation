from selenium import webdriver


class DriverSingleton:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            # Create only one object
            cls._instance = super().__new__(cls)

            # Create driver only once
            cls._instance.driver = webdriver.Chrome()

        return cls._instance


    def get_driver(self):
        return self.driver


# Usage
driver1 = DriverSingleton().get_driver()
driver2 = DriverSingleton().get_driver()

print(driver1 is driver2)   # True
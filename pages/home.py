from selenium.webdriver.common.by import By

base_url = "https://www.alten.es/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.button_accept_cookies = "//button[@id='tarteaucitronPersonalize2']"
        self.button_search = "//a[@class='search-btn']"
        self.input_search = "//input[@type='search']"

    def get_button_accept_cookies(self):
        return self.driver.find_element(By.XPATH, self.button_accept_cookies)

    def find_button_accept_cookies(self):
        if self.driver.find_element(By.XPATH, self.button_accept_cookies):
            return True
        return False

    def get_button_search(self):
        return self.driver.find_element(By.XPATH, self.button_search)

    def get_input_search(self):
        return self.driver.find_element(By.XPATH, self.input_search)

    @staticmethod
    def get_base_url():
        return base_url

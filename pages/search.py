from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.div_search_page = "//div[@class='search-page']"
        self.first_position_list_search = "(//a[contains(@class, 'result')])[2]"
        self.results_number = ".nb > span"

    def get_list_search_page(self):
        return self.driver.find_element(By.XPATH, self.div_search_page)

    def get_second_position_list_search(self):
        return self.driver.find_element(By.XPATH, self.first_position_list_search)

    def get_number_results(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.results_number)

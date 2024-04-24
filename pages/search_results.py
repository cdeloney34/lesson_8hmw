from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPAge(Page):
    Verify_items = (By.XPATH, "//span[text()='Added to cart']")

    def verify_search_resluts(self):
    context.self.driver.find_element(*self.Verify_items)
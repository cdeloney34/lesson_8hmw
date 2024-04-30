from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    enter_coffee = (By.ID, 'search')
    click_search = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, item):
        self.input_text(item,self.enter_coffee)
        self.click(self.click_search)
        sleep(5)
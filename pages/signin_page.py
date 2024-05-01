from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):
    verify_signin_form = (By.CSS_SELECTOR, (By.XPATH, "//span[text()='Sign into your Target account']")


    def verify_signin(self):
        self.find_element(self.verify_signin_form)
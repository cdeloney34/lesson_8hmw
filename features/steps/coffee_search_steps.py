from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


enter_coffee = (By.ID, 'search')
click_search = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
verify_coffee = (By.XPATH, "//span[text()='coffee']")


@given('Open Target home-page')
def open_Target(context):
    context.driver.get('https://www.target.com/')

@when('Type Coffee in search')
def type_Coffee(context):
    context.find_element(enter_coffee).send_keys('coffee')

@when('click search button')
def click_Search(context):
    context.find_element(click_search).click()

@then('Verify coffee page appears')
def verify_coffee_page(context):
    context.find_element(verify_coffee)




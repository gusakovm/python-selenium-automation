from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SEARCH_FIELD = (By.CSS_SELECTOR, '#helpsearch')
SEARCH_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#helpSearchSubmit input[type="submit"]')
CONTENT_H1 = (By.CSS_SELECTOR, '.help-content h1')


@when('Input {search_text} to the search field')
def input_search_field(context, search_text):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.click()
    search_field.clear()
    sleep(0.5)
    search_field.send_keys(search_text)
    sleep(0.5)


@when('Click on search button')
def submit_search(context):
    submit = context.driver.find_element(*SEARCH_SUBMIT_BUTTON)
    submit.click()
    sleep(1)


@then('Search block shows {text} in the title')
def search_block_shows_expected_text(context, text):
    title = context.driver.find_element(*CONTENT_H1)
    assert title.text == text
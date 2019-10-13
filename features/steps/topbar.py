from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


CART_BUTTON = (By.CSS_SELECTOR, '#nav-cart')


@when('Click to Shopping Cart button')
def click_shoping_cart(context):
    button = context.driver.find_element(*CART_BUTTON)
    button.click()
    sleep(1.5)
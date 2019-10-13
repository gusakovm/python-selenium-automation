from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


CART_CONTENT_H1 = (By.CSS_SELECTOR, '#sc-active-cart .sc-empty-cart-header')


@then('Amazon Cart page title is {text}')
def cart_is_empty(context, text):
    cart_h1 = context.driver.find_element(*CART_CONTENT_H1)
    assert text in cart_h1.text
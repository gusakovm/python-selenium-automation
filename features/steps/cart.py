from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


CART_CONTENT_H1 = (By.CSS_SELECTOR, '#sc-active-cart .sc-empty-cart-header')
NAV_CART = (By.CSS_SELECTOR, '#nav-cart')
NAV_CART_COUNTER = (By.CSS_SELECTOR, '#nav-cart #nav-cart-count')
CART_ITEMS = (By.CSS_SELECTOR, '.a-row .sc-list-item')

@then('Make sure the cart isn\'t empty (by counter)')
def check_cart_isnt_empty_in_nav(context):
    cart_counter = context.driver.find_element(*NAV_CART_COUNTER)
    cart_counter_num = cart_counter.text
    assert int(cart_counter_num) > 0, f"Actual items in cart is {cart_counter_num}"


@then('Make sure the item shows at the Cart page')
def check_cart_isnt_empty_on_cart_page(context):
    nav_cart = context.driver.find_element(*NAV_CART)
    nav_cart.click()
    sleep(3)
    cart_items = context.driver.find_elements(*CART_ITEMS)
    assert len(cart_items) > 0


@then('Amazon Cart page title is {text}')
def cart_is_empty(context, text):
    cart_h1 = context.driver.find_element(*CART_CONTENT_H1)
    assert text in cart_h1.text
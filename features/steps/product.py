from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, then
from time import sleep


AMAZON_SEARCH_FIELD = (By.CSS_SELECTOR, '#nav-belt #twotabsearchtextbox')
FOUND_GOODS = (By.CSS_SELECTOR, '.s-result-list .s-result-item')
ITEM_LINK = (By.CSS_SELECTOR, 'span[data-component-type="s-product-image"] a.a-link-normal')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '#desktop_qualifiedBuyBox #add-to-cart-button[name="submit.add-to-cart"]')
POPOVER_BTN = (By.CSS_SELECTOR, '#abb-intl-pop-cta .a-button-primary[id*=a-autoid]')


@when('Search {search_text} product')
def lets_search(context, search_text):
    search_field = context.driver.find_element(*AMAZON_SEARCH_FIELD)
    search_field.clear()
    search_field.send_keys(search_text)
    sleep(0.3)
    search_field.send_keys(Keys.RETURN)
    sleep(3)


@when('Add {index} index product to the cart')
def add_product_into_cart(context, index):
    found_items = context.driver.find_elements(*FOUND_GOODS)
    if (len(found_items) == 0):
        context.driver.quit()
        return false
    else:
        item_link = found_items[0].find_element(*ITEM_LINK)
        item_link.click()
        sleep(3)
    add_cart_btn = context.driver.find_element(*ADD_TO_CART_BTN)
    add_cart_btn.click()
    sleep(3)
    continue_popover_btns = context.driver.find_elements(*POPOVER_BTN)
    if len(continue_popover_btns) > 0:
        continue_popover_btns[0].click()
        sleep(3)
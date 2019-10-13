from selenium.webdriver.common.by import By
from behave import when,then
from time import sleep


SANDWICH = (By.CSS_SELECTOR, 'a#nav-hamburger-menu')
SANDWICH_MENUAREA_JS = 'document.getElementById("hmenu-content").getElementsByClassName("hmenu-visible")[0]'
HELP_LINK = (By.CSS_SELECTOR, '#hmenu-content .hmenu-visible li a[href*="help/customer/display.html"]')


@when('Open sandwich menu')
def open_menu(context):
    sandwich_btn = context.driver.find_element(*SANDWICH)
    sandwich_btn.click()
    sleep(1.5)


@when('Scroll down sandwich menu')
def scroll_down_menu(context):
    sandwich_scroll_height = context.driver.execute_script(f'return {SANDWICH_MENUAREA_JS}.scrollHeight')
    sandwich_client_height = context.driver.execute_script(f'return {SANDWICH_MENUAREA_JS}.clientHeight')
    sleep(0.3)
    sandwich_scroll_to = sandwich_scroll_height - sandwich_client_height
    context.driver.execute_script(f'{SANDWICH_MENUAREA_JS}.scrollTo(0, {sandwich_scroll_to})')
    sleep(1.5)


@then('Help item is visible in sandwich menu')
def help_is_shown_in_menu(context):
    sandwich_menu_help_link = context.driver.find_element(*HELP_LINK)
    assert sandwich_menu_help_link.is_displayed()


@when('Click to the Help item in the menu list')
def click_on_help_in_menu(context):
    sandwich_menu_help_link = context.driver.find_element(*HELP_LINK)
    sandwich_menu_help_link.click()
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Init driver
options = Options()
options.add_argument("--window-size=1024,800")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

# Locators
_sandwich = (By.XPATH, '//a[@id="nav-hamburger-menu"]')
_sandwich_menu_area = 'document.getElementById("hmenu-content").getElementsByClassName("hmenu-visible")[0]'
_sandwich_menu_help_link = (By.XPATH, '//*[@id="hmenu-content"]//*[contains(@class, "hmenu-visible")]//li//a[contains(@href, "help/customer/display.html")]')
_help_search_field = (By.XPATH, '//input[@id="helpsearch"]')
_help_search_submit = (By.XPATH, '//*[@id="helpSearchSubmit"]//input[@type="submit"]')
_help_content_h1 = (By.XPATH, '//*[@class="help-content"]//h1')

# Test

driver.get('https://www.amazon.com/')
sleep(2)

sandwich_btn = driver.find_element(*_sandwich)
sandwich_btn.click()
sleep(2)

sandwich_scroll_height = driver.execute_script(f'return {_sandwich_menu_area}.scrollHeight')
sleep(0.5)
sandwich_client_height = driver.execute_script(f'return {_sandwich_menu_area}.clientHeight')
sleep(0.5)
sandwich_scroll_to = sandwich_scroll_height - sandwich_client_height
driver.execute_script(f'{_sandwich_menu_area}.scrollTo(0, {sandwich_scroll_to})')
sleep(1.5)

sandwich_menu_help_link = driver.find_element(*_sandwich_menu_help_link)
sandwich_menu_help_link.click()
sleep(2)

help_search_field = driver.find_element(*_help_search_field)
help_search_field.click()
sleep(0.5)

help_search_field.send_keys("cancel order")
sleep(0.5)

help_search_submit = driver.find_element(*_help_search_submit)
help_search_submit.click()
sleep(2)

help_content_h1 = driver.find_element(*_help_content_h1)

assert help_content_h1.text == 'Cancel Items or Orders'

driver.quit()
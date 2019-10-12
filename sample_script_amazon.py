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

# Hover (just an experiment)
def hover(el):
    action.move_to_element(el).perform()

# Locators
ls_try_prime_btn = (By.XPATH, '//*[@id="nav-link-prime"]/*[contains(@class,"nav-line-2")]')
ls_try_prime_banner_btn = (By.XPATH, '//*[@id="nav-flyout-prime"]//*[@class="prime-button-try"]//a[contains(@href,"prime")]')

# Test

driver.get('https://www.amazon.com/')
sleep(6) # I must use long sleeps because "US VPN", I see another Amazon.com from Russian IP :(

try_prime_btn = driver.find_element(*ls_try_prime_btn)
try_prime_btn.click()
sleep(3)

try_prime_banner_btn = driver.find_element(*ls_try_prime_banner_btn)
try_prime_banner_btn.click()
sleep(3)

assert 'amazon.com/amazonprime' in driver.current_url

driver.quit()
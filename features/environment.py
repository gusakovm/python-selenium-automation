from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def browser_init(context):
    """
    :param context: Behave context
    """
    # Init driver
    options = Options()
    options.add_argument("--window-size=1024,800")

    context.driver = webdriver.Chrome(options=options)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.action = ActionChains(context.driver)
    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

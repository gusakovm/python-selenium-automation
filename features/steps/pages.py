from behave import given, then
from time import sleep


pages = {
    'Amazon': 'https://www.amazon.com',
    'AmazonHelpCenter': 'https://www.amazon.com/gp/help/customer/display.html',
    'AmazonCart': 'https://www.amazon.com/gp/cart/view.html',
}


@given('Open {page_name} page')
def open_amazon_page(context, page_name):
    context.driver.get(pages[page_name])
    sleep(1)


@then('The page {page_name} is shown')
def page_is_expected(context, page_name):
    assert pages[page_name] in context.driver.current_url
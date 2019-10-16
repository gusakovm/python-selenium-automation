from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


INFO_BOXES = (By.CSS_SELECTOR, '.benefit-box')

@then('There are {num} info-boxes on the page')
def exp_numb_of_inf_boxes(context, num):
    inf_boxes = context.driver.find_elements(*INFO_BOXES)
    num_boxes = len(inf_boxes)
    assert num_boxes == int(num), f"Actual number of boxes are {num_boxes}, {num} are expected"
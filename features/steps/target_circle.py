from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then, Then
from time import sleep

from features.steps.header_steps import CART_ICON
from features.steps.search_results_steps import ADD_TO_CART_BTN


@given('Open Target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(15)

@when('User opens Target Circle page')
def opens_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="@web/GlobalHeader/UtilityHeader/TargetCircle"]').click()
    sleep(10)

@when('User can add {product} to cart')
def add_to_cart(context, product):
    context.driver.find_element()

@when('Click on Add to Cart Button')
def click_add_to_cart_icon(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Confirm Add to Cart Button')
def confirm_add_to_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="content-wrapper"] button[id*="addToCartButtonOrTextIdFor"]').click()
    sleep(10)
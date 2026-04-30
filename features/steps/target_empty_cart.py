from cucumber_tag_expressions.model import And
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then, Then
from time import sleep


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(10)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_msg_text(context):
    actual = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    expected = "Your cart is empty"
    assert actual == expected, f'Expected {expected} did not match actual {actual}'


@when('Click Account button')
def click_account_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
@when('Click Sign in')
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then("Verify 'Sign in or create account' message is shown")
def verify_user_log_in(context):
    actual = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]").click()
    expected = "You are logged out"
    assert actual == expected, f'Expected {expected} did not match {acutal}'






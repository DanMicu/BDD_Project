import time
from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)


@when('I introduce the correct username')
def step_impl(context):
    username = context.browser.type_username()
    username.send_keys('tomsmith')
    time.sleep(2)


@when('I introduce the correct password')
def step_impl(context):
    password = context.browser.type_password()
    password.send_keys('SuperSecretPassword!')
    time.sleep(2)


@then('I click the login button')
def step_impl(context):
    login_button = context.browser.get_login()
    login_button.click()
    time.sleep(2)


@then('I am successfully logged in')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/secure"
    assert context.browser.get_current_url() == expected_url


@when('I introduce a wrong username')
def step_impl(context):
    wrong_username = context.browser.type_username()
    wrong_username.send_keys('random')
    time.sleep(2)


@when('I introduce a wrong password')
def step_impl(context):
    wrong_password = context.browser.type_password()
    wrong_password.send_keys('SuperSecretPassword!')
    time.sleep(2)


@then("The 'Your username is invalid!' error appears")
def step_impl(context):
    error_message = context.browser.error_message_is_displayed()
    error_message.is_displayed()




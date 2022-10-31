import time
from behave import *


# @given('I am on the login page') ### ASK ABOUT  AmbiguousStep: I used "i am on the login page in both secure_page.feature and login_page.feature is it correct to not include the first @Given "I am on the login page" step?
# def step_impl(context):
#     context.browser.driver.get("https://the-internet.herokuapp.com/login")
#     time.sleep(2)

@Given('I enter the correct login credentials')
def step_impl(context):
    username = context.browser.type_username()
    username.send_keys('tomsmith')
    password = context.browser.type_password()
    password.send_keys('SuperSecretPassword!')
    time.sleep(2)


@Given('I click login')
def step_impl(context):
    login_button = context.browser.get_login()
    login_button.click()


@Given('I am on the Secure page')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/secure"
    assert context.browser.get_current_url() == expected_url


@When('I click the logout button')
def step_impl(context):
    logout_button = context.browser.log_out()
    logout_button.click()


@Then('I am successfully logged out')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/login"
    assert context.browser.get_current_url() == expected_url


@When('I am redirected to the Secure page')
def step_impl(context):
    expected_url = "https://the-internet.herokuapp.com/secure"
    assert context.browser.get_current_url() == expected_url


@Then("'You logged into a secure area! is displayed")
def step_impl(context):
    secure_area_message = context.browser.secure_area_message_is_displayed()
    secure_area_message.is_displayed()



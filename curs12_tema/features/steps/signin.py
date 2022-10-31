from behave import *
from selenium.webdriver.common.keys import Keys
import time


@given("We are on the Sign-In page")
def step_impl(context):
    context.signin_page.go_home()
    time.sleep(2)


@when('We enter the correct email')
def step_impl(context):
    email = context.signin_page.input_correct_email()
    email.send_keys("gmail@gmail.com")
    time.sleep(2)


@when("We leave the password empty")
def step_impl(context):
    password = context.signin_page.input_password()
    password.send_keys("a")
    password.send_keys(Keys.BACKSPACE)
    time.sleep(2)


@then("Log In button is disabled")
def step_impl(context):
    assert context.signin_page.is_login_button_enabled() == False
    time.sleep(2)


@then('The Please enter your password error is present')
def step_impl(context):
    error_message = context.signin_page.password_missing_error().text
    assert error_message == 'Please enter your password!'
    time.sleep(2)

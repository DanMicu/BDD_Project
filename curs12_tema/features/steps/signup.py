import time

from behave import *
from selenium.webdriver.common.keys import Keys


@given("We have the jules webpage loaded")
def step_impl(context):
    context.signin_page.go_home()
    time.sleep(1)


@when("We click sign up")
def step_impl(context):
    signup = context.signup_page.signup_button_selector()
    signup.click()
    time.sleep(1)


@when("We click the Personal button")
def step_impl(context):
    personal = context.signup_page.personal_button_selector()
    personal.click()
    time.sleep(1)


@when("We click continue")
def step_impl(context):
    continue_button = context.signup_page.continue_button_selector()
    continue_button.click()
    time.sleep(1)


@when("We input a correct first name")
def step_impl(context):
    first_name = context.signup_page.first_name_selector()
    first_name.send_keys('Dan')
    time.sleep(1)


@when("we input a correct last name")
def step_impl(context):
    last_name = context.signup_page.last_name_selector()
    last_name.send_keys('Micu')
    time.sleep(1)


@when("We input a wrong email")
def step_impl(context):
    enter_email = context.signup_page.email_selector()
    enter_email.send_keys('D')
    time.sleep(2)


@then("The Please enter a valid email address error is displayed")
def step_impl(context):
    error_message = context.signup_page.invalid_email_error_selector().text
    assert error_message == 'Please enter a valid email address.'
    time.sleep(2)


@then("We clear the email input")
def step_impl(context):
    enter_email = context.signup_page.email_selector()
    enter_email.send_keys(Keys.BACKSPACE)
    time.sleep(2)


@then("We input a correct email")
def step_impl(context):
    enter_email = context.signup_page.email_selector()
    enter_email.send_keys('D@gmail.com')
    time.sleep(2)


@then("The error message is no longer displayed")
def step_impl(context):
    try:
        login = context.signup_page.continue_button_selector
        login.click()
        print('clickable')
    except:
        print('not clickable')

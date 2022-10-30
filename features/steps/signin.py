from behave import *
from selenium.webdriver.common.keys import Keys


@given("We are on the Sign-In page")
def step_impl(context):
    context.signin_page.go_home()


@when('We enter the correct email')
def step_impl(context):
    email = context.signin_page.input_correct_email()
    email.send_keys("gmail@gmail.com")


@when("We leave the password empty")
def step_impl(context):
    password = context.signin_page.input_password()
    password.send_keys("a")
    password.send_keys(Keys.BACKSPACE)


@then("Log In button is disabled")
def step_impl(context):
    try:
        login = context.signin_page.login_button()
        login.click()
        print('clickable')
    except:
        print('not clickable')


@then('The Please enter your password error is present')
def step_impl(context):
    error_message = context.signin_page.password_missing_error().text
    assert error_message == 'Please enter your password!'

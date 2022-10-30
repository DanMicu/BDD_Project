import time

from behave import *


@then("We are redirected to the sign up page")
def step_impl(context):
    expected_url = context.signup_page.URL
    assert expected_url == context.browser.get_current_url()


@then("We click log in")
def step_impl(context):
    login = context.signup_page.login_button_selector()
    login.click()
    time.sleep(2)


@then("We are redirected to the sign in page")
def step_impl(context):
    expected_url = context.signin_page.URL
    assert expected_url == context.browser.get_current_url()

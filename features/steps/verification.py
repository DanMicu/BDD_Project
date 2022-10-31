import time

from behave import *


@then("We are redirected to the sign up page")
def step_impl(context):
    assert context.signup_page.verify_url


@then("We click log in")
def step_impl(context):
    login = context.signup_page.login_button_selector()
    login.click()
    time.sleep(2)


@then("We are redirected to the sign in page")
def step_impl(context):
    assert context.signin_page.verify_url
